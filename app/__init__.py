from flask import Flask, jsonify, request, render_template, session, g
from flask_mysqldb import MySQL
from werkzeug.utils import redirect


app = Flask(__name__)
app.secret_key = '123456789'
cnx = MySQL(app)

from app.models import login_dao, cliente_dao, endereco_dao, usuario_dao
from app.controllers import default, login, crud