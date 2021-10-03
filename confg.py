from flask_mysqldb import MySQL

class DevelopmentConfigDuda():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '2001'
    MYSQL_DB = 'sextoandar'

class DevelopmentConfigGui():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '141500'
    MYSQL_DB = 'sextoandar'

config = {
    'developmentDuda': DevelopmentConfigDuda,
    'developmentGui': DevelopmentConfigGui
}