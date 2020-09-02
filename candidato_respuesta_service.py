from datetime import datetime
from botocore.exceptions import ClientError


class CandidatoRespuestaService():

    def registrar_respuesta_candidato(self, idcandidato, idtestpsicologico_idparte_idpregunta, idtestpsicologico,
                                      idparte, idpregunta, respuesta, dynamodb=None):

        try:
            tabla = dynamodb.Table('Candidato_Respuesta')
            response = tabla.put_item(
                Item={
                    'idcandidato': idcandidato,
                    'idtestpsicologico_idparte_idpregunta': idtestpsicologico_idparte_idpregunta,
                    'idtestpsicologico': idtestpsicologico,
                    'idparte': idparte,
                    'idpregunta': idpregunta,
                    'respuesta': respuesta,
                    'fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
            return False, e.response['Error']['Message'], 500
        else:
            return True, 'Respuesta guardada con éxito.', 200