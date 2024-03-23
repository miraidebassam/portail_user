import json
import requests

class FacturationService:
    FACTURATION_API_BASE_URL = 'http://localhost:5000'
    HLR_API_BASE_URL = 'http://localhost:8080/api/hlr'

    def test(self):
        try:
            # Appelez l'API du microservice facturation
            url = f"{self.FACTURATION_API_BASE_URL}/test"
            response = requests.get(url)
            # Vérifiez la réponse HTTP pour détecter d'éventuelles erreurs
            response.raise_for_status()
            # Affichez le contenu de la réponse
            print(response.text)

        except requests.RequestException as e:
            # Gérez les erreurs liées à la requête HTTP
            print(f"Erreur lors de la requête vers le microservice HLR : {str(e)}")
            raise  # Propagez l'exception pour la gestion d'erreur dans la vue Flask




    def insert_abonne(self, data):
        try:
            # Convertir les données en format JSON
            data_json = json.dumps(data)
            
            # Appelez l'API du microservice Facturation
            url = f"{self.FACTURATION_API_BASE_URL}/insertAbonne"
            headers = {'Content-Type': 'application/json'}  # Définir l'en-tête Content-Type
            response = requests.post(url, data=data_json, headers=headers)
            
            # Vérifiez la réponse HTTP pour détecter d'éventuelles erreurs
            response.raise_for_status()

        except requests.RequestException as e:
            # Gérez les erreurs liées à la requête HTTP
            print(f"Erreur lors de la requête vers le microservice Facturation : {str(e)}")
            raise  # Propagez l'exception pour la gestion d'erreur dans la vue Flask







    def generer_facture(self, data):
        try:
            #Appeler API FACTURATION et lui passer les info de ABONNE
            # Appelez l'API du microservice FACTURATION_API_BASE_URL
            url = f"{self.FACTURATION_API_BASE_URL}/generer_facture_abonne/{data}"
            response = requests.get(url)
            # Vérifiez la réponse HTTP pour détecter d'éventuelles erreurs
            response.raise_for_status()

            # Vérifiez la réponse HTTP
            if response.status_code == 200:
                subscriber_data = response.json()  # Convertissez la réponse JSON en un objet Python
                print("\nHelo Mi voici ce que tu cherches, infos de l'abonne est la: \n",subscriber_data)
                return subscriber_data

            # response_data = response.json()
        except requests.RequestException as e:
            print(f"Erreur lors de la génération de la facture pour l'abonné {data}: {str(e)}")
            raise





















    def generer_facture_abonne(self, data):
        try:
            # Récupérer les informations de l'abonné depuis votre service d'abonnement
            abonne_info = self.obtenir_info_abonne(data)
            print("\n\n\n", abonne_info, "\n\n\n")
            # Calculer le montant total de la facture
            montant_total = self.calculer_montant_facture(abonne_info)

            # # Enregistrer la facture dans votre base de données de facturation
            # self.enregistrer_facture(data, montant_total)

            # # Retourner le montant total de la facture
            return montant_total

        except requests.RequestException as e:
            print(f"Erreur lors de la génération de la facture pour l'abonné {data}: {str(e)}")
            raise

    def obtenir_info_abonne(self, data):
        try:
            # Appelez l'API du microservice HLR
            url = f"{self.HLR_API_BASE_URL}/display/{data}"
            response = requests.get(url)
            # Vérifiez la réponse HTTP pour détecter d'éventuelles erreurs
            response.raise_for_status()

            # Vérifiez la réponse HTTP
            if response.status_code == 200:
                subscriber_data = response.json()  # Convertissez la réponse JSON en un objet Python
                print("\nHelo Mi voici toutttttttt\n",subscriber_data)
                return subscriber_data

            # print("Activate One Router")
            # response_data = response.json()

        except requests.RequestException as e:
            # Gérez les erreurs liées à la requête HTTP
            print(f"Erreur lors de la requête vers le microservice HLR : {str(e)}")
            raise  # Propagez l'exception pour la gestion d'erreur dans la vue Flask


    def calculer_montant_facture(self, data):
        montant_total = 0
        for service in data['activeServices']:
            tarif_service = self.obtenir_tarif_service(service)  # Assurez-vous d'implémenter cette fonction
            # montant_total += tarif_service
            montant_total += 2

        return montant_total



    def obtenir_tarif_service(self, service):
        try:
            # Appelez l'API du microservice HLR
            url = f"{self.FACTURATION_API_BASE_URL}/get_services/{service}"
            response = requests.get(url)
            # Vérifiez la réponse HTTP pour détecter d'éventuelles erreurs
            response.raise_for_status()

            # Vérifiez la réponse HTTP
            if response.status_code == 200:
                subscriber_data = response.json()  # Convertissez la réponse JSON en un objet Python
                # print("\nHelo Mi\n",subscriber_data)
                return subscriber_data

            # print("Activate One Router")
            # response_data = response.json()

        except requests.RequestException as e:
            # Gérez les erreurs liées à la requête HTTP
            print(f"Erreur lors de la requête vers le microservice HLR : {str(e)}")
            raise  # Propagez l'exception pour la gestion d'erreur dans la vue Flask

        print("obtenir_tarif_service")




    def enregistrer_facture(self, abonne_id, montant_total):
        # Enregistrez la facture dans votre base de données de facturation
        # Implémentez cette méthode selon votre architecture
        pass


    def display_all_invoices(self):
        try:
            # Appelez l'API du microservice HLR
            url = f"{self.FACTURATION_API_BASE_URL}/invoices"
            response = requests.get(url)
            # Vérifiez la réponse HTTP pour détecter d'éventuelles erreurs
            response.raise_for_status()

            # Vérifiez la réponse HTTP
            if response.status_code == 200:
                invoice_data = response.json()  # Convertissez la réponse JSON en un objet Python
                # print("\nHelo Mi tu as recuper tous les subscribers\n")
                return invoice_data

            # response_data = response.json()

        except requests.RequestException as e:
            # Gérez les erreurs liées à la requête HTTP
            print(f"Erreur lors de la requête vers le microservice HLR : {str(e)}")
            raise  # Propagez l'exception pour la gestion d'erreur dans la vue Flask
