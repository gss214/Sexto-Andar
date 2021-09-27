from flask import Flask, jsonify, request, render_template, session, g
from flask_mysqldb import MySQL
from werkzeug.utils import redirect
from confg import config

app=Flask(__name__)
app.secret_key = '123456789'

cnx = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

def get_user():
    try: 
        cursor = cnx.connection.cursor()
        sql = 'SELECT * FROM usuarios'
        cursor.execute(sql)
        data = cursor.fetchall()
        return data        
    except Exception as ex:
        return None

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
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

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == 'POST':

        if 'sign_up' in request.form:
            return render_template("sign_up.html")
        else:
            # pega o usuario e senha do login.html
            user = request.form.get("InputUser")
            password = request.form.get("InputPassword")

            # deleta a sessao de usuario online
            session.pop('user_id', None)    
            data = get_user()

            # caso de erro no banco de dados
            if data == None:
                return jsonify({'Msg':'Erro'})

            user = [x for x in data if x[2] == password and x[1] == user]
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
            error_statement = error, user=user)
    else:
        return render_template("login.html")



if __name__ == '__main__':
    app.config.from_object(config['developmentDuda'])
    app.run()