import re
from .excepciones import EmailInvalidoError

def validar_email(email):
    #validar formato de email
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(patron, email):
        raise EmailInvalidoError(f"El email '{email}' es inválido.")