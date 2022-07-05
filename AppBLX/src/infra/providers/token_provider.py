#-----------------------
# BIBLIOTECAS
#-----------------------
import os
import configparser
from jose import jwt
from datetime import datetime, timedelta
#-----------------------
# CONSTANTES
#-----------------------
NOME_ARQUIVO = "file.ini";
ARQUIVO_INI = (
    f"{NOME_ARQUIVO}"
);
if(not os.path.isfile(ARQUIVO_INI)):
    mensagem:str = (
        f"O arquivo {NOME_ARQUIVO} "
        f"não existe "
    );
    raise FileExistsError(mensagem);

CONFIG = configparser.ConfigParser();
CONFIG.read(ARQUIVO_INI);
SECRET_KEY:str = CONFIG.get("token","SECRET_KEY");
ALGORITHM = "HS256";
EXPIRES_IN_MINUTES = (((60*24)*360)*5);
#-----------------------
# CLASSES
#-----------------------
#-----------------------
# FUNÇÕES()
#-----------------------
def create_access_token(data:dict) -> str:
    dados = data.copy();
    
    hora_agora = datetime.utcnow();
    hora_relativa = timedelta(
        minutes=EXPIRES_IN_MINUTES
    );
    
    expiracao =  hora_agora + hora_relativa;
    
    dados.update({"exp":expiracao});

    token_jwt = jwt.encode(
        dados,
        SECRET_KEY,
        algorithm=ALGORITHM
    );

    return token_jwt;

def verificar_access_token(token:str):
    payload:dict = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=ALGORITHM
    );
    return payload.get("sub");
#-----------------------
# Main()
#-----------------------
#-----------------------