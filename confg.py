from flask_mysqldb import MySQL

class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = ''
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'sextoandar'

config = {
    'development': DevelopmentConfig
}