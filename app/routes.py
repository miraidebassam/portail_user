from functools import wraps
from flask import Blueprint, render_template, redirect, request, session, url_for, flash
from app.forms import *
from app.services.authService import AuthentificationService
from app.services.facturationService import FacturationService
from app.services.hlr_service import HLRService
from app.services.in_service import INService


bp = Blueprint('main', __name__)

# Instanciation le service HLR
hlr_service = HLRService()

# Instanciation le service IN
in_service = INService()

# Instanciation le service Facturation
fact_service = FacturationService()

# Instanciation le service Facturation
auth_service = AuthentificationService()


# Décorateur pour vérifier si l'utilisateur est authentifié
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' in session:
            return f(*args, **kwargs)  # Autoriser l'accès si l'utilisateur est déjà connecté
        else:
            return redirect(url_for('main.login'))  # Rediriger vers la page de connexion sinon
    return decorated_function

@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('login.html')


@bp.route('/create_subscriber', methods=['GET', 'POST'])
@login_required
def create_subscriber():
    if request.method == 'POST':
        # Capturer les données du formulaire
        number = request.form.get('addNumber')
        subscriber_type = request.form.get('addSubscriberType')
        services_to_activate = request.form.getlist('servicesToActivate[]')

        data = {
            'number': number,
            'subscriberType': subscriber_type,
            'servicesToActivate': services_to_activate
        }
        dataInService = {
            'number': number,
            'subscriberType': subscriber_type,
        }

        if data['subscriberType'] == 'PREPAID':
            #Creation du subscriber dans hlr
            hlr_service.create_subscriber(data)
            #Initiation d'une nouvelle connection avec InSrvice
            in_service.createSubsInService(dataInService)
            
            #Inserer Abonne dans le service Facturation
            fact_service.insert_abonne(data)
            # in_service.newConnection(dataInCreateConnection)
        else:
            #Creation du subscriber dans hlr
            hlr_service.create_subscriber(data)
            
            #Inserer Abonne dans le service Facturation
            fact_service.insert_abonne(data)

        return redirect(url_for('main.subscribers'))

    return render_template('test1.html')


@bp.route('/deactivate_subscriber/<string:number>', methods=['GET', 'POST'])
@login_required
def deactivate_subscriber(number):
    action = request.form.get('action')
    if request.method == 'POST':
        # number = request.form.get('number')
        print('Voici le numero que j\'ai recu du front\n', number)
        if not number:
            flash('Please provide a subscriber number', 'error')
            # return redirect(url_for('error.html'))

        data = {
            'number': number,
        }
        # Appel au service HLR
        hlr_service.deactivate_subscriber(data)

        flash('Subscriber deactivate successfully', 'success')
        
        return render_template('test1.html')


@bp.route('/activate_subscriber/<string:number>/<string:subscriberType>', methods=['GET', 'POST'])
@login_required
def activate_subscriber(number, subscriberType):
    action = request.form.get('action')
    # print("Voila l'action qui a ete choisie\n", action)
    if request.method == 'POST':
        print('Voici le numero que j\'ai recu du front\n', number, subscriberType)
        if not number:
            flash('Please provide a subscriber number', 'error')
            # return redirect(url_for('error.html'))
        if action == 'activate':
            data = {
                'number': number,
            }
            # Appel au service HLR
            hlr_service.activateOne_subscriber(data)

            flash('Subscriber deactivate successfully', 'success')
        elif action == 'deactivate':
            data = {
                'number': number,
            }

            if subscriberType == 'POSTPAID':
                #si l'abonne est de type [POSTPAID] je desactive chez HLR 
                # Appel au service HLR
                hlr_service.deactivate_subscriber(data)
            else:
                #sinon je desactive chez HLR et je TERMINE chez IN
                hlr_service.deactivate_subscriber(data)
                in_service.terminate_subscriber(data)



        flash('Subscriber deactivate successfully', 'success')
        
        subscriber_data = hlr_service.display_subscriber(number)

        return render_template('details_subscriber.html', subscriber=subscriber_data)


@bp.route('/suspend_or_restore_subscriber', methods=['GET', 'POST'])
@login_required
def suspend_or_restore_subscriber():
    form = SubscriberForm()
    if form.validate_on_submit():
        # data = {
        #     'numAppelant': form.numAppelant.data,
        #     # Ajoutez les autres données de l'abonné ici
        # }
        # Appel au service HLR
        hlr_service.create_subscriber()
        # Appel au service IN
        # in_service.create_subscriber()
        flash('Subscriber created successfully', 'success')
        return redirect(url_for('main.test'))
    
    return render_template('index.html', form=form)

@bp.route('/add_services_to_subscriber/<string:number>/<string:activate>', methods=['GET', 'POST'])
@login_required
def add_services_to_subscriber(number, activate):
    if request.method == 'POST':
        serviceToAdd = request.form.getlist('servicesToActivate[]')
        hlr_service.add_service_to_subscriber(number, activate, serviceToAdd)

        return redirect(url_for('main.datails_subscriber', number=number))
    

@bp.route('/genererCdr/<string:number>', methods=['GET', 'POST'])
@login_required
def genererCdr(number):
    #Je passe le numero de l'abonne
    # #Retrouver toutes les infos de abonne 
    info_abonne = hlr_service.display_subscriber(number)

    if request.method == 'POST':
        # Capturer les données du formulaire
        numero = request.form.get('editNumber')
        numeAppele = request.form.get('numeAppele')
        # services_to_activate = request.form.getlist('servicesToActivate[]')
        duree = request.form.get('duree')

        data = {
            'callerNumber': info_abonne['number'],
            'imsi': info_abonne['imsi'],
            'calleeNumber': numeAppele,
            'callDuration': duree,
            'subscriberType': info_abonne['subscriberType'],
        }

        # print("\n\n\n\n", "Generation de CDR Aleatoire: ", info_abonne['imsi'],info_abonne['subscriberType'], "\n\n\n\n")
        hlr_service.generete_cdr(data)

    return render_template('test3.html')


@bp.route('/generate_invoice/<string:number>', methods=['GET', 'POST'])
@login_required
def generate_invoice(number):
    #Je passe le numero de l'abonne
    # #Retrouver toutes les infos de abonne 
    # info_abonne = hlr_service.display_subscriber(number)

    # print("\n\n\n\n", info_abonne, "\n\n\n\n")
    fact_service.generer_facture(number)

    return render_template('test3.html')


@bp.route('/get_invoices', methods=['GET'])
@login_required
def get_invoices():
    factures = fact_service.display_all_invoices()
    
    print("\n\n"f"Service: {factures}","\n\n")

    return render_template('factures.html', factures=factures)



@bp.route('/get_cdr', methods=['GET'])
@login_required
def get_cdr():
    cdrs = hlr_service.display_cdr()
    # print("\n\n"f"CDRs: {cdrs}","\n\n")
    return render_template('cdr.html', cdrs=cdrs)


@bp.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    print("\n\n\nTou s'est bien passe Mi\n\n\n")
    return render_template('test1.html')


@bp.route('/subscribers', methods=['GET', 'POST'])
@login_required
def subscribers():
    subscribers = hlr_service.display_all_subscribers()
    services = hlr_service.display_all_services()
    return render_template('subscriber.html', subscribers=subscribers, services=services)
    # return render_template('test.html')


@bp.route('/factures', methods=['GET', 'POST'])
@login_required
def factures():

    print("Le numero de l'abonne est: ")
    fact_service.test()

    return render_template('test1.html')



@bp.route('/cdr', methods=['GET', 'POST'])
@login_required
def cdr():
    print("\n\n\nTou s'est bien passe Mi\n\n\n")
    return render_template('test5.html')


@bp.route('/signOut', methods=['GET', 'POST'])
@login_required
def signOut():
    print("\n\n\nTou s'est bien passe Mi\n\n\n")
    return render_template('test4.html')


@bp.route('/edit_subscriber/<string:number>', methods=['GET', 'POST'])
@login_required
def edit_subscriber(number):
    if request.method == 'POST':
        #Recherche du subscriber dans la base de donnes a travers son numero
        subscriber = hlr_service.display_subscriber(number)

        if subscriber:
            print("Le subscriber exite")
        else:
            print("Le subscriber n'existe pas")

        #Si le subscriber existe alors on fait les modifications sinon on n'en fait pas
        print("IDDDDDDD: ", subscriber)
        return render_template('test.html')


@bp.route('/datails_subscriber/<string:number>', methods=['GET', 'POST'])
@login_required
def datails_subscriber(number):
    subscriber_data = hlr_service.display_subscriber(number)
    if subscriber_data:
        print("Le subscriber exite")
        print("\n\nSubscriber in details", subscriber_data, "\n\n")
        all_services = hlr_service.display_all_services()
    else:
        print("Le subscriber n'existe pas")

    return render_template('details_subscriber.html', subscriber=subscriber_data, all_services=all_services)


# Désactivation d’un abonné (résiliation du numéro)
@bp.route('/delete_subscriber/<string:number>')
@login_required
def delete_subscriber(number):
    subscriber_data = hlr_service.display_subscriber(number)
    #print('subscriber_data.subscriberType', subscriber_data['subscriberType'] )
    if subscriber_data['subscriberType'] == 'PREPAID':
        data = {
            'number': number,
        }
        # Appel au service IN pour terminer la session du subscriber
        in_service.terminate_subscriber(data)
        # Desactivation de l'abonne dans hlr
        hlr_service.deactivate_subscriber(data)

        flash('Subscriber deactivate successfully', 'success')
        # print("Je suis PREPAID")
    else:
        hlr_service.deactivate_subscriber(data)
        print("Je suis PostPAID")

    subscribers = hlr_service.display_all_subscribers()
    return render_template('subscriber.html', subscribers=subscribers)


@bp.route('/get_subscriber_info')
@login_required
def get_subscriber_info():
    print("Helo Mi")
    # # request.args.get('number')
    # data = {
    #     'number': request.args.get('number'),
    # }
    # subscriber = hlr_service.display_subscriber(data)
    
    # response_data = {
    #     'number': subscriber.number,
    #     'imsi': subscriber.imsi,
    #     'creationDate': subscriber.creationDate,
    #     'subscriberType': subscriber.subscriberType
    # }
    
    # print("Response data============\n",response_data)  # Ajoutez cette ligne pour imprimer la réponse côté serveur
    
    # return jsonify(response_data)



#===============================Template===============================
@bp.route('/invoices-content')
@login_required
def invoices_content():
    # Ici, vous pouvez récupérer les données liées aux factures depuis votre backend
    # et les passer à votre modèle.
    return render_template('invoices_content.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Ajoutez ici la logique pour valider les identifiants et générer le token JWT
        user = auth_service.display_user(username)

        print("\n\nLes infos user: ", user, password, "\n\n\n")

        # Exemple basique de validation (remplacez-le par votre propre logique d'authentification)
        if user and user['password'] == password:
            # Si les identifiants sont valides, redirigez l'utilisateur vers le tableau de bord
            print("\n\nLes infos sont correctes: Dashboard \n\n")
            session['username'] = username
            return redirect(url_for('main.subscribers'))
        else:
            # Si les identifiants sont invalides, affichez un message d'erreur
            error_message = "Identifiants invalides. Veuillez réessayer."
            return render_template('login.html', error_message=error_message)
        
    return render_template('login.html')


@bp.route('/logout')
@login_required
def logout():
    print("\n\n\n Vous allez etre deconnecte \n\n\n\n")
    session.pop('username', None)  # Supprimez l'utilisateur de la session
    flash('Vous avez été déconnecté avec succès', 'success')
    return redirect(url_for('main.index'))