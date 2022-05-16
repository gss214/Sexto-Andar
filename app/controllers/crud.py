from app import app, cnx
from flask import request, render_template, session
from werkzeug.utils import redirect
from app.models.cliente_dao import Cliente, ClienteDAO
from app.models.login_dao import LoginDAO
from app.models.endereco_dao import Endereco, EnderecoDAO
from app.decorators import auth
from app.models.corretor_dao import Corretor, CorretorDAO
from app.models.proprietario_dao import Proprietario, ProprietarioDAO

@app.route("/crud")
@auth.has_permission(['adm'])
def crud():
    return render_template("crud.html")

@app.route("/crud_corretor", methods = ['GET', 'DELETE', 'PUT', 'POST'])
@auth.has_permission(['adm'])
def crud_corretor():

    cursor = cnx.connection.cursor()       

    if request.method == 'DELETE':
        data = request.get_json()
        CorretorDAO().delete(cursor, data['cpf'])
        cnx.connection.commit()
        return '304'

    if request.method == 'POST':
        print("entrou")
        data = request.get_json()
        print(data)
        corretor = Corretor(data['p0'], data['p1'], data['p2'], data['p3'], None, None, data['p6'], data['p7'])
        
        c = CorretorDAO().find_by_id(cursor, corretor.cpf)
        corretor.fk_endereco = c.fk_endereco
        corretor.fk_login = c.fk_login

        CorretorDAO().update(cursor, corretor, corretor.cpf)
        cnx.connection.commit()
        print("entrou")
        return '201'

    corretores = CorretorDAO().find_all(cursor)

    return render_template("crud_corretor.html", corretores = corretores) 

@app.route("/crud_cliente", methods = ['GET', 'DELETE', 'PUT', 'POST'])
@auth.has_permission(['adm'])
def crud_cliente():
    cursor = cnx.connection.cursor()       

    if request.method == 'DELETE':
        data = request.get_json()
        ClienteDAO().delete(cursor, data['cpf'])
        cnx.connection.commit()
        return '304'

    if request.method == 'POST':
        data = request.get_json()
        print(data)
        cliente = Cliente(data['p0'], data['p1'], data['p2'], data['p3'], None, None)

        c = ClienteDAO().find_by_id(cursor, cliente.cpf)
        cliente.fk_endereco = c.fk_endereco
        cliente.fk_login = c.fk_login

        ClienteDAO().update(cursor, cliente, cliente.cpf)

        cnx.connection.commit()
        return '201'
    

    clientes = ClienteDAO().find_all(cursor)

    return render_template("crud_cliente.html", clientes = clientes)


@app.route("/crud_proprietario", methods = ['GET', 'DELETE', 'PUT', 'POST'])
@auth.has_permission(['adm'])
def crud_proprietario():
    cursor = cnx.connection.cursor()       

    if request.method == 'DELETE':
        data = request.get_json()
        ProprietarioDAO().delete(cursor, data['cpf'])
        cnx.connection.commit()
        return '304'

    if request.method == 'POST':
        data = request.get_json()
        proprietario = Proprietario(data['p0'], data['p1'], data['p2'], data['p3'], None, None)

        c = ProprietarioDAO().find_by_id(cursor, proprietario.cpf)
        proprietario.fk_endereco = c.fk_endereco
        proprietario.fk_login = c.fk_login

        ProprietarioDAO().update(cursor, proprietario, proprietario.cpf)

        cnx.connection.commit()
        return '201'
    

    proprietarios = ProprietarioDAO().find_all(cursor)

    return render_template("crud_proprietario.html", proprietarios = proprietarios)



@app.route("/crud_endereco", methods = ['GET', 'DELETE', 'PUT', 'POST'])
@auth.has_permission(['adm'])
def crud_endereco():
    cursor = cnx.connection.cursor()       

    if request.method == 'DELETE':
        data = request.get_json()
        EnderecoDAO().delete(cursor, data['codigo'])
        cnx.connection.commit()
        return '304'

    if request.method == 'POST':
        data = request.get_json()
        endereco = Endereco(data['p0'], data['p1'], data['p2'], data['p3'], data['p4'], data['p5'], data['p6'], data['p7'])
        EnderecoDAO().update(cursor, endereco, endereco.codigo)
        cnx.connection.commit()
        return '201'
    

    enderecos = EnderecoDAO().find_all(cursor)

    return render_template("crud_endereco.html", enderecos = enderecos)


@app.route("/adicionar_endereco", methods = ['GET', 'DELETE', 'PUT', 'POST'])
@auth.has_permission(['adm'])
def adicionar_endereco():
    voltar = request.referrer.split('/')[3]
    if request.method == 'POST':
        cursor = cnx.connection.cursor()      
        endereco = from_form_to_endereco(request)   
        EnderecoDAO().create(cursor, endereco)
        cnx.connection.commit()
        enderecos = EnderecoDAO().find_all(cursor)

        return render_template('crud_endereco.html', enderecos = enderecos, add_sucess=True)
    return render_template('adicionar_endereco.html', voltar=voltar)

def from_form_to_endereco(request):
    codigo = None
    CEP = request.form.get("InputZipcode")
    rua = request.form.get("InputStreet")
    bairro = request.form.get("InputRegion")
    cidade = request.form.get("InputCity")
    estado = request.form.getlist('estado')[0]
    numero = request.form.get("InputNumber")
    complemento = request.form.get("InputAddressComplement")

    return Endereco(codigo, CEP, rua, bairro, cidade, estado, numero, complemento)

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
