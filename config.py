class Config:
    SECRET_KEY = 'ola'

class DevelopmentConfig(Config):
    DEGUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'restaurant'

config = {
    'dvelopment' : DevelopmentConfig
}