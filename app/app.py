from flask import Flask, jsonify, request, render_template, session, g
from flask_mysqldb import MySQL
from werkzeug.utils import redirect
from confg import config

app=Flask(__name__)
app.secret_key = '123456789'

cnx = MySQL(app)

def get_users():
    try: 
        cursor = cnx.connection.cursor()
        sql = 'SELECT * FROM usuarios'
        cursor.execute(sql)
        data = cursor.fetchall()
        return data        
    except Exception as ex:
        return None


def get_apts():
    try:
        cursor = cnx.connection.cursor()
        sql = 'SELECT * FROM apartamentos'
        cursor.execute(sql)
        dados = cursor.fetchall()
        apts = []
        for i in dados:
            apt = {'ID':i[0], 'Nome':i[1], 'Quartos':i[2]}
            apts.append(apt)
        return apts
    except Exception as ex:
        return None


@app.before_request
def before_request():
    if 'user_id' in session:
        users = get_users()
        if users == None:
            return
        user = [x for x in users if x[0] == session['user_id']]
        #print(user)
        g.user = user


@app.route('/')
def index():
    return render_template("index.html")
    

@app.route('/sobre')
def sobre():
    lista = ["Guilherme", "Duda"]
    return render_template("sobre.html", names=lista)


@app.route('/CRUD')
def CRUD():
    if session and g.user[0][3] == 'admin':
        apts = get_apts()
        users = get_users()
        if apts == None or users == None:
            return jsonify({'Msg':'Erro'})
        return render_template("CRUD.html", apts=apts, users=users)
    return "Você não tem permissão pra isso"


@app.route('/adicionar_usuario', methods=['GET', 'POST'])
def add_user():
    if session and g.user[0][3] == 'admin':
        if request.method == 'POST':
            print(request.form)
            if 'cadastrar' in request.form:
                nome = request.form.get("InputUsuario")
                senha = request.form.get("InputSenha")
                funcao = request.form.get("InputFuncao")
                try:
                    cursor = cnx.connection.cursor()
                    sql = f"INSERT INTO usuarios (nome, senha, permissao, login) VALUES ('{nome}', '{senha}', '{funcao}', {0})"
                    cursor.execute(sql)
                    cnx.connection.commit()
                except Exception as ex:
                    print(ex)
            
                return redirect('/CRUD')
            else:
                return redirect('/CRUD')
        else:
            return render_template('adicionar_usuario.html')
    return "Você não tem permissão pra isso"


@app.route('/logout')
def logout():
    user = g.user[0][1]
    Id = g.user[0][0]
    session.pop('user_id', None)
    try:
        cursor = cnx.connection.cursor()
        sql = f"UPDATE usuarios SET login = 0 WHERE id = '{Id}'"
        cursor.execute(sql)
        cnx.connection.commit()
    except Exception as ex:
        print('erro ao atualizar login')

    return render_template('logout.html', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get("InputUsuario")
        senha = request.form.get("InputSenha")
        session.pop('user_id', None)
        data = get_users()

        if data == None:
            return jsonify({'Msg':'Erro'})

        user = [x for x in data if x[2] == senha and x[1] == user]
        print(user)

        if user:
            session['user_id'] = user[0][0]
            try:
                cursor = cnx.connection.cursor()
                sql = f"UPDATE usuarios SET login = 1 WHERE id = '{user[0][0]}'"
                cursor.execute(sql)
                cnx.connection.commit()
            except Exception as ex:
                print('erro ao atualizar login')
            return render_template("login_sucesso.html", user=user[0][1])
            
        error = "Login invalido!"
        return render_template("login.html",
        error_statement = error,
        user=user)
    else:
        return render_template("login.html")


@app.route('/apartamentos', methods=['GET'])
def mostrar_apts():
    apts = get_apts()
    if apts == None:
        return jsonify({'Msg':'Erro'})
    return render_template("apartamentos.html", apts=apts)


@app.route('/apartamentos/<id>', methods=['GET'])
def apartamento(id):
    try:
        cursor = cnx.connection.cursor()
        sql = "SELECT id, nome, qnt_quartos FROM apartamentos WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        dados = cursor.fetchone()
        if dados != None:
            apt = {'ID':dados[0], 'Nome':dados[1], 'Quartos':dados[2]}

        return jsonify({'Apartamentos':apt, 'Msg':'Apartamento encontrado'})
    except Exception as ex:
        return jsonify({'Msg':'Apartamento não encontrado'})


@app.route('/apartamentos', methods=['POST'])
def criar_apt():
    try:
        cursor = cnx.connection.cursor()
        sql = """INSERT INTO apartamentos (id, nome, qnt_quartos) 
                 VALUES ('{0}', '{1}', '{2}')""".format(request.json['id'], request.json['nome'], request.json['qnt_quartos'],)
        cursor.execute(sql)
        cnx.connection.commit()
        return jsonify({'Msg':'Apartamento cadastrado com sucesso!'})
    except Exception as ex:
        return jsonify({'Msg':'Apartamento não cadastrado ):'})


@app.route('/apartamentos/<id>', methods=['DELETE'])
def deletar_apt(id):
    try:
        cursor = cnx.connection.cursor()
        sql = "DELETE FROM apartamentos WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        cnx.connection.commit()
        return jsonify({'Msg':'Apartamento deletado com sucesso!'})
    except Exception as ex:
        return jsonify({'Msg':'Erro'})


def pagina_404(erro):
    return '<h1> Essa página não existe ): </h1>', 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_404)
    app.run()