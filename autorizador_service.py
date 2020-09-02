import urllib3
import json


class AutorizadorService():

    def validar_email(self, email):
        if email:
            http = urllib3.PoolManager()
            url = 'https://api.evaluationroom.com/candidato_email_validar/'
            response = http.request('GET',
                                    url,
                                    headers={'Content-Type': 'application/json', 'Authorization': email},
                                    retries=False)
            print('Resultado de API: {} {}'.format(response.status, response.data))
            if response.status == 200:
                return True, 'Usuario valido', response.status
            return False, json.loads(response.data.decode('utf-8'))['mensaje'], response.status
        return False, 'Usuario no valido.', 404