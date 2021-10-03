'''
a ideia eh nao usar mais esse arquivo
'''

from flask import Flask, jsonify, request, render_template, session, g
from flask_mysqldb import MySQL
from werkzeug.utils import redirect
from confg import config

app=Flask(__name__)
app.secret_key = '123456789'

cnx = MySQL(app)

@app.before_request
def before_request():
    if 'user_id' in session:
        try:
            cursor = cnx.connection.cursor()
            select = f"SELECT * FROM login where codigo = '{session['user_id']}'"
            cursor.execute(select)
            user =  cursor.fetchone()
            if not user:
                return
            #print(user)
            g.user = user
        except Exception as ex:
            print(ex)

#login falta só olhar se o user tem permissao de admin para habilitar a pagina do CRUD 
@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == 'POST':

        if 'sign_up' in request.form:
            return render_template("sign_up.html")
        else:
            # pega o usuario e senha do login.html
            email = request.form.get("InputEmail")
            password = request.form.get("InputPassword")

            # deleta a sessao de usuario online
            session.pop('user_id', None)    

            #verifica email == senha
            try:
                cursor = cnx.connection.cursor()
                select = f"SELECT * FROM login where email = '{email}' AND senha = '{password}'"
                cursor.execute(select)
                user =  cursor.fetchone()

                print(user)
                print(email, password)

                if not user:
                    return render_template("login.html", error_statement='Login invalido!')

                #cria a sessão do usuario
                session['user_id'] = user[0]

                return render_template("login_sucesso.html", user=user[1])
            
            except Exception as ex:
                return render_template("login.html", error_statement=ex)
    else:
        return render_template("login.html")

@app.route('/logout')
def logout():
    user = g.user[1]
    session.pop('user_id', None)
    return render_template('logout.html', user=user)

if __name__ == '__main__':
    app.config.from_object(config['developmentDuda'])
    app.run()