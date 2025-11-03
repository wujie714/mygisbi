from utilmeta.conf import Env


class ServiceEnvironment(Env):
    DEBUG: bool = False
    PRODUCTION: bool = False
    DJANGO_SECRET_KEY: str = "mapyeah_001"
    DJANGO_ALLOWED_HOSTS: list =  ["127.0.0.1", "localhost","192.168.2.26","bi.fahua.vip"]
    DB_ENGINE: str = "mysql"
    
    DB_NAME: str = "mygisbi"
    DB_USER: str = "mygisbi"
    DB_PASSWORD: str = "mapyeah"
    DB_PORT: int = 3306
    DB_HOST: str = "192.168.2.236"

    REDIS_HOST="bt.fahua.vip"
    REDIS_PORT:int=6379
    REDIS_DB=10
    REDIS_PASSWORD="mapyeah"



env = ServiceEnvironment(sys_env="UTILMETA_")
