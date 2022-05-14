from app import app
from config import config

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(host='0.0.0.0')