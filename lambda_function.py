from dynamodb_config import dynamodb
from autorizador_service import AutorizadorService
from candidato_respuesta_service import CandidatoRespuestaService

autorizador_service = AutorizadorService()
candidato_respuesta_service = CandidatoRespuestaService()

def lambda_handler(event, context):

    email = event['headers']['Authorization']
    flag, respuesta, codigo = autorizador_service.validar_email(email)
    if not flag:
        return {
            'statusCode': codigo,
            'body': respuesta
        }

    idcandidato = event['idcandidato']
    idtestpsicologico_idparte_idpregunta = event['idtestpsicologico_idparte_idpregunta']
    idtestpsicologico = event['idtestpsicologico']
    idparte = event['idparte']
    idpregunta = event['idpregunta']
    respuesta = event['respuesta']

    flag, respuesta, codigo = candidato_respuesta_service.registrar_respuesta_candidato(idcandidato, idtestpsicologico_idparte_idpregunta, idtestpsicologico, idparte, idpregunta, respuesta, dynamodb)
    if flag:
        return {
            'statusCode': codigo,
            'body': respuesta
        }

    return {
        'statusCode': 500,
        'body': 'Error al registrar respuesta del candidato.'
    }
