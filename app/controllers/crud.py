from app import app, cnx
from flask import request, render_template, session
from werkzeug.utils import redirect
from app.models.cliente_dao import ClienteDAO
from app.models.login_dao import LoginDAO
from app.models.endereco_dao import EnderecoDAO

@app.route("/crud")
def crud():
    return render_template("crud.html")

def editar_endereco():
    pass

@app.route('/perfil', methods=['GET', 'POST'])
def perfil():

    if request.method == 'GET':
        cursor = cnx.connection.cursor()

        login = LoginDAO().find_by_id(cursor, session['user_id'])
        login = [login.email, login.senha]

        sql = f"SELECT * FROM cliente WHERE fk_login = '{session['user_id']}'"
        cursor.execute(sql)
        cliente = cursor.fetchone()

        endereco = EnderecoDAO().find_by_id(cursor, cliente[4])
        endereco = [endereco.CEP, endereco.rua, endereco.bairro, endereco.cidade, endereco.estado, endereco.numero, endereco.complemento]

        return render_template("perfil.html", cliente=cliente, login=login, endereco=endereco)
    else:
        if 'salvarPefil' in request.form:
            print('update perfil')
        return redirect('/perfil')
