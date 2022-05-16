class DevelopmentConfig():
    DEBUG = True
    HOST = '0.0.0.0'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_HOST = 'sextoandar_db'
    MYSQL_DB = 'sextoandar'

config = {
    'development': DevelopmentConfig
}
