import requests

class INService:
    HLR_API_BASE_URL = 'http://localhost:8081/api/in'

    def create_subscriber(self, data):
        # Ajoutez la logique pour créer un abonné dans le HLR
        # Utilisez les données fournies dans le dictionnaire 'data'
        # Vous pouvez appeler le microservice HLR ici ou effectuer toute autre logique nécessaire
        print(f"Création d'un abonné dans le HLR avec les données : {data}")
        # Simulez un succès pour l'exemple
        # Si une exception se produit, elle sera propagée à l'appelant


    def createSubsInService(self, data):
        try:
            # Appelez l'API du microservice HLR
            url = f"{self.HLR_API_BASE_URL}/createSubs"
            response = requests.post(url, data=data)
            print(data)
            # Vérifiez la réponse HTTP pour détecter d'éventuelles erreurs
            response.raise_for_status()
            print("New Connection Subscriber")

            # response_data = response.json()

        except requests.RequestException as e:
            # Gérez les erreurs liées à la requête HTTP
            print(f"Erreur lors de la requête vers le microservice IN : {str(e)}")
            raise  # Propagez l'exception pour la gestion d'erreur dans la vue Flask


    def newConnection(self, data):
        try:
            # Appelez l'API du microservice HLR
            url = f"{self.HLR_API_BASE_URL}/newconnection"
            response = requests.post(url, data=data)
            # Vérifiez la réponse HTTP pour détecter d'éventuelles erreurs
            print("in_serviceeeeeeeeeeeee\n\n\n", data)
            response.raise_for_status()
            print("New Connection Subscriber")

            # response_data = response.json()

        except requests.RequestException as e:
            # Gérez les erreurs liées à la requête HTTP
            print(f"Erreur lors de la requête vers le microservice IN : {str(e)}")
            raise  # Propagez l'exception pour la gestion d'erreur dans la vue Flask



    def terminate_subscriber(self, data):
        try:
            # Appelez l'API du microservice HLR
            url = f"{self.HLR_API_BASE_URL}/termination"
            response = requests.post(url, data=data)
            # Vérifiez la réponse HTTP pour détecter d'éventuelles erreurs
            response.raise_for_status()
            print("Terminate One Subscriber")

            # response_data = response.json()

        except requests.RequestException as e:
            # Gérez les erreurs liées à la requête HTTP
            print(f"Erreur lors de la requête vers le microservice IN : {str(e)}")
            raise  # Propagez l'exception pour la gestion d'erreur dans la vue Flask

