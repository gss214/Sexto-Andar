from app import app
from confg import config

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()