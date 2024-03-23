from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SubscriberForm(FlaskForm):
    numAppelant = StringField('Numéro Appelant', validators=[DataRequired()])
    numAppele = StringField('Numéro Appelé', validators=[DataRequired()])
    # Ajoutez d'autres champs pour les informations de l'abonné
    submit = SubmitField('Créer Abonné')

class CreateSubscriberForm(FlaskForm):
    number = StringField('Numéro Abonne', validators=[DataRequired()])
    subscriberType = StringField('Type Abonne', validators=[DataRequired()])
    # Ajoutez d'autres champs pour les informations de l'abonné
    submit = SubmitField('Créer Abonné')

class DeactivateSubscriberForm(FlaskForm):
    number = StringField('Numéro Abonne', validators=[DataRequired()])
    submit = SubmitField('Désactiver Abonné')

class ActivateSubscriberForm(FlaskForm):
    number = StringField('Numéro Abonne', validators=[DataRequired()])
    submit = SubmitField('Activer Abonné')

class DisplaySubscriberForm(FlaskForm):
    number = StringField('Numéro Abonne', validators=[DataRequired()])
    submit = SubmitField('Activer Abonné')