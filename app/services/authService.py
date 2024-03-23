import requests

class AuthentificationService:

    AUTHENTIFICATION_API_BASE_URL = 'http://localhost:8085/api/users'

    def display_all_users(self):
        try:
            # Appelez l'API du microservice HLR
            url = f"{self.HLR_API_BASE_URL}/displayUsers"
            response = requests.get(url)
            # Vérifiez la réponse HTTP pour détecter d'éventuelles erreurs
            response.raise_for_status()

            # Vérifiez la réponse HTTP
            if response.status_code == 200:
                subscriber_data = response.json()  # Convertissez la réponse JSON en un objet Python
                return subscriber_data

            # response_data = response.json()

        except requests.RequestException as e:
            # Gérez les erreurs liées à la requête HTTP
            print(f"Erreur lors de la requête vers le microservice HLR : {str(e)}")
            raise  # Propagez l'exception pour la gestion d'erreur dans la vue Flask


    def display_user(self, data):
        try:
            # Appelez l'API du microservice HLR
            # print("///////////////////////\n\n", data, "\n\n////////////")
            url = f"{self.AUTHENTIFICATION_API_BASE_URL}/display/"
            response = requests.get(url, params={'username': data})
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
