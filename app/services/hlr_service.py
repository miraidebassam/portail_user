import requests

class HLRService:
    HLR_API_BASE_URL = 'http://localhost:8080/api/hlr'
    
    def create_subscriber(self, data):
        try:
            # Appelez l'API du microservice HLR
            url = f"{self.HLR_API_BASE_URL}/activate"
            response = requests.post(url, data=data)
            # Vérifiez la réponse HTTP pour détecter d'éventuelles erreurs
            response.raise_for_status()

            # response_data = response.json()

        except requests.RequestException as e:
            # Gérez les erreurs liées à la requête HTTP
            print(f"Erreur lors de la requête vers le microservice HLR : {str(e)}")
            raise  # Propagez l'exception pour la gestion d'erreur dans la vue Flask


    def generete_cdr(self, data):
        try:
            # Appelez l'API du microservice HLR
            print(data, "\nGenerer CDRRRRRRRRR\n\n", data, "\n\n\n")
            url = f"{self.HLR_API_BASE_URL}/generateCDR"
            response = requests.post(url, json=data)
            # Vérifiez la réponse HTTP pour détecter d'éventuelles erreurs
            response.raise_for_status()

            # response_data = response.json()

        except requests.RequestException as e:
            # Gérez les erreurs liées à la requête HTTP
            print(f"Erreur lors de la requête vers le microservice HLR : {str(e)}")
            raise  # Propagez l'exception pour la gestion d'erreur dans la vue Flask



    def deactivate_subscriber(self, data):
        try:
            # Appelez l'API du microservice HLR
            url = f"{self.HLR_API_BASE_URL}/deactivate"
            response = requests.post(url, data=data)
            # Vérifiez la réponse HTTP pour détecter d'éventuelles erreurs
            response.raise_for_status()
            print("Deactivate One Router")

            # response_data = response.json()

        except requests.RequestException as e:
            # Gérez les erreurs liées à la requête HTTP
            print(f"Erreur lors de la requête vers le microservice HLR : {str(e)}")
            raise  # Propagez l'exception pour la gestion d'erreur dans la vue Flask



    def activateOne_subscriber(self, data):
        try:
            # Appelez l'API du microservice HLR
            print('Dataaaaa:\n\n', data)
            url = f"{self.HLR_API_BASE_URL}/activateOne"
            response = requests.post(url, data=data)
            # Vérifiez la réponse HTTP pour détecter d'éventuelles erreurs
            response.raise_for_status()

            print("Activate One Router")
            # response_data = response.json()

        except requests.RequestException as e:
            # Gérez les erreurs liées à la requête HTTP
            print(f"Erreur lors de la requête vers le microservice HLR : {str(e)}")
            raise  # Propagez l'exception pour la gestion d'erreur dans la vue Flask




    def display_subscriber(self, data):
        try:
            # Appelez l'API du microservice HLR
            url = f"{self.HLR_API_BASE_URL}/display/{data}"
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


    def display_all_subscribers(self):
        try:
            # Appelez l'API du microservice HLR
            url = f"{self.HLR_API_BASE_URL}/display"
            response = requests.get(url)
            # Vérifiez la réponse HTTP pour détecter d'éventuelles erreurs
            response.raise_for_status()

            # Vérifiez la réponse HTTP
            if response.status_code == 200:
                subscriber_data = response.json()  # Convertissez la réponse JSON en un objet Python
                # print("\nHelo Mi tu as recuper tous les subscribers\n")
                return subscriber_data

            print("\n\n Coucouuu mi \n\n ")
            # response_data = response.json()

        except requests.RequestException as e:
            # Gérez les erreurs liées à la requête HTTP
            print(f"Erreur lors de la requête vers le microservice HLR : {str(e)}")
            raise  # Propagez l'exception pour la gestion d'erreur dans la vue Flask



    def display_all_services(self):
        try:
            # Appelez l'API du microservice HLR
            url = f"{self.HLR_API_BASE_URL}/services"
            response = requests.get(url)
            # Vérifiez la réponse HTTP pour détecter d'éventuelles erreurs
            response.raise_for_status()

            # Vérifiez la réponse HTTP
            if response.status_code == 200:
                subscriber_data = response.json()  # Convertissez la réponse JSON en un objet Python
                print("\nHelo Mi tu as recuper tous les services\n", subscriber_data)
                return subscriber_data

            print("\n\n Coucouuu mi \n\n ")
            # response_data = response.json()

        except requests.RequestException as e:
            # Gérez les erreurs liées à la requête HTTP
            print(f"Erreur lors de la requête vers le microservice HLR : {str(e)}")
            raise  # Propagez l'exception pour la gestion d'erreur dans la vue Flask


    def display_cdr(self):
        try:
            # Appelez l'API du microservice HLR
            url = f"{self.HLR_API_BASE_URL}/displayCdr"
            response = requests.get(url)
            # Vérifiez la réponse HTTP pour détecter d'éventuelles erreurs
            response.raise_for_status()

            # Vérifiez la réponse HTTP
            if response.status_code == 200:
                subscriber_data = response.json()  # Convertissez la réponse JSON en un objet Python
                print("\nHelo Mi tu as recuper tous les cdrs\n", subscriber_data)
                return subscriber_data

            print("\n\n Coucouuu mi \n\n ")
            # response_data = response.json()

        except requests.RequestException as e:
            # Gérez les erreurs liées à la requête HTTP
            print(f"Erreur lors de la requête vers le microservice HLR : {str(e)}")
            raise  # Propagez l'exception pour la gestion d'erreur dans la vue Flask

    def add_service_to_subscriber(self, number, activate, serviceToAdd):
        try:
            data = {
                'number': number,
                'activate': activate,
                'servicesToActivate': serviceToAdd
            }
            print("\n\n","Ola Mi on regarde les services: ", data, "\n\n")
            # Appelez l'API du microservice HLR
            url = f"{self.HLR_API_BASE_URL}/modifyservice"
            response = requests.post(url, data=data)
            # Vérifiez la réponse HTTP pour détecter d'éventuelles erreurs
            response.raise_for_status()

            # response_data = response.json()

        except requests.RequestException as e:
            # Gérez les erreurs liées à la requête HTTP
            print(f"Erreur lors de la requête vers le microservice HLR : {str(e)}")
            raise  # Propagez l'exception pour la gestion d'erreur dans la vue Flask
