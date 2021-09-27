from flask_mysqldb import MySQL

class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '2001'
    MYSQL_DB = 'sextoandar'

config = {
    'development': DevelopmentConfig
}