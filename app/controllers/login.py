from app import app, cnx
from flask import request, render_template, session, g
from werkzeug.utils import redirect
from app.models.cliente_dao import Cliente, ClienteDAO
from app.models.corretor_dao import Corretor, CorretorDAO

from app.models.usuario_dao import Usuario
from app.models.login_dao import Login, LoginDAO
from app.models.endereco_dao import Endereco, EnderecoDAO
from app.models.proprietario_dao import ProprietarioDAO
from app.decorators import auth

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    # transformar para so um if
    if request.method == 'POST':
        # fazer a validacao dos dados para colocar no BD

        usuario = from_form_to_usuario(request)
        login = from_form_to_login(request)
        endereco = from_form_to_endereco(request)             
        
        try:
            cursor = cnx.connection.cursor()
            LoginDAO().create(cursor, login)
            EnderecoDAO().create(cursor, endereco)
            usuario.fk_endereco = endereco.codigo
            usuario.fk_login = login.codigo

            if login.permissao == 'cliente':
                ClienteDAO().create(cursor, usuario)

            elif login.permissao == 'corretor':
                horario_inicio = request.form.get("InputHorarioInicialCorretor")
                horario_final = request.form.get("InputHorarioFinalCorretor")
                corretor = Corretor(usuario.cpf, usuario.nome, usuario.data_de_nascimento, usuario.sexo,
                                    usuario.fk_endereco, usuario.fk_login, horario_inicio, horario_final)
                CorretorDAO().create(cursor, corretor)
                
            else:
                ProprietarioDAO().create(cursor, usuario)

            cnx.connection.commit()

        except Exception as ex:
            print(ex)
            return render_template('sign_up.html', error_statement=ex)
            
        return render_template('sign_up_sucesso.html')

    return render_template('sign_up.html')

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == 'POST':
        if 'sign_up' in request.form:
            return redirect("/sign_up")
        else:
            # pega o usuario e senha do login.html

            login = from_form_to_login(request)

            # deleta a sessao de usuario online
            session.pop('user_id', None)    

            #verifica email == senha
            try:
                cursor = cnx.connection.cursor()

                login = LoginDAO().find_without_id(cursor, login.email, login.senha)

                if not login:
                    return render_template("login.html", error_statement='Login invalido!')                

                session['user_id'] = login.codigo
                session['user_email'] = login.email
                session['user_permission'] = login.permissao
                
                return render_template("login_sucesso.html", user=login.email)
            
            except Exception as ex:
                return render_template("login.html", error_statement=ex)
    else:
        return render_template("login.html")

@app.route('/logout')
@auth.is_authenticated
def logout():
    session.pop('user_id', None)
    return render_template('logout.html', user=session['user_email'])


def from_form_to_usuario(request):
    nome = request.form.get("InputName")
    cpf = request.form.get("InputCPF")
    data_de_nascimento = request.form.get("InputDateBirth")
    fk_endereco = None
    fk_login = None

    radio = request.form.get('radiosexo')

    if radio == 'Feminino': sexo = "feminino" 
    elif radio == 'Masculino': sexo = "masculino"
    else: sexo = "Outro"

    return Usuario(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login)

def from_form_to_login(request):
    codigo = None
    email = request.form.get("InputEmail")
    senha = request.form.get("InputPassword")
    tipo_usuario = request.form.get("tipo_usuario")
            
    if tipo_usuario == 'Cliente': permissao = "cliente"
    elif tipo_usuario == 'Corretor': permissao = "corretor"
    else: permissao = "proprietario"       

    return Login(codigo, email, senha, permissao)

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