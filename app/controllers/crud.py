import re
from app import app, cnx
from flask import request, render_template, session
from werkzeug.utils import redirect
from app.models.cliente_dao import ClienteDAO
from app.models.login_dao import LoginDAO
from app.models.endereco_dao import EnderecoDAO
from app.decorators import auth
from app.models.corretor_dao import CorretorDAO
from app.models.proprietario_dao import ProprietarioDAO

@app.route("/crud")
@auth.has_permission(['adm'])
def crud():
    return render_template("crud.html")

@app.route("/crud_corretor", methods = ['GET', 'DELETE', 'PUT', 'POST'])
@auth.has_permission(['adm'])
def crud_corretor():

    cursor = cnx.connection.cursor()       

    if request.method == 'DELETE':
        #data = request.get_data(as_text=True)
        data = request.get_json()
        CorretorDAO().delete(cursor, data['cpf'])
        cnx.connection.commit()
        return '304'

    corretores = CorretorDAO().find_all(cursor)
    #clientes = ClienteDAO().find_all(cursor)
    #proprietarios = ProprietarioDAO().find_all(cursor)
    #enderecos = EnderecoDAO().find_all(cursor)

    return render_template("crud_corretor.html", corretores = corretores) 

@app.route("/crud_cliente", methods = ['GET', 'DELETE', 'PUT', 'POST'])
@auth.has_permission(['adm'])
def crud_cliente():
    cursor = cnx.connection.cursor()       

    if request.method == 'DELETE':
        #data = request.get_data(as_text=True)
        data = request.get_json()
        ClienteDAO().delete(cursor, data['cpf'])
        cnx.connection.commit()
        return '304'
    

    clientes = ClienteDAO().find_all(cursor)
    #proprietarios = ProprietarioDAO().find_all(cursor)
    #enderecos = EnderecoDAO().find_all(cursor)

    return render_template("crud_cliente.html", clientes = clientes)

def editar_endereco():
    pass

@app.route('/perfil', methods=['GET', 'POST'])
def perfil():

    if request.method == 'GET':
        cursor = cnx.connection.cursor()

        login = LoginDAO().find_by_id(cursor, session['user_id'])
        login = [login.email, login.senha]

        cliente = ClienteDAO().find_by_fk(cursor, session['user_id'])
        cliente = [cliente.cpf, cliente.nome, cliente.data_de_nascimento, cliente.sexo, cliente.fk_endereco, cliente.fk_login]

        endereco = EnderecoDAO().find_by_id(cursor, cliente[4])
        endereco = [endereco.CEP, endereco.rua, endereco.bairro, endereco.cidade, endereco.estado, endereco.numero, endereco.complemento]

        return render_template("perfil.html", cliente=cliente, login=login, endereco=endereco)
    else:
        if 'salvarPefil' in request.form:
            print('update perfil')
        return redirect('/perfil')
