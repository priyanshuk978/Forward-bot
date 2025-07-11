# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "23685822")
    API_HASH = environ.get("API_HASH", "ff0572e13ff2f63a50f6dc707e0c4c9f")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6725874739').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://envs.sh/e8w.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://priyanshu1234:<d8Nau3FLAe4WwYGm>@cluster0.w7grbtg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002758097378'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "False")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
