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

# quando clicar em cadastrar retornar uma tela de sucesso ou erro
# modularizar as funcoes
# se em alguma etapa de insert der erro, nao criar as tabelas anteriores
# commit no final ?
@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        print(request.form)
        if 'cadastrar' in request.form:

            # fazer a validacao dos dados para colocar no BD

            name = request.form.get("InputName")
            cpf = request.form.get("InputCPF")
            email = request.form.get("InputEmail")
            password = request.form.get("InputPassword")
            date_of_birth = request.form.get("InputDateBirth")
            
            #sexo 
            fem = request.form.getlist('Feminino') 
            masc = request.form.getlist('Masculino')
            outro = request.form.getlist('Outro')

            sexo = ""

            if fem.count('on'): sexo = "Feminino" 
            elif masc.count('on'): sexo = "Masculino"
            else: sexo = "Outro"

            #address
            zip_code = request.form.get("InputZipcode")
            street = request.form.get("InputStreet")
            region = request.form.get("InputRegion")
            city = request.form.get("InputCity")
            number = request.form.get("InputNumber")
            adress_complement = request.form.get("InputAddressComplement")

            cliente = request.form.getlist('Cliente') 
            corretor = request.form.getlist('Corretor')
            proprietario = request.form.getlist('Proprietario') 

            print(cliente, corretor, proprietario)

            print(type(corretor))

            
            try:
                cursor = cnx.connection.cursor()
                insert = f"INSERT INTO login(email, senha) VALUES ('{email}', '{password}')"
                cursor.execute(insert)
                cnx.connection.commit()

                select = f"SELECT MAX(codigo) from login"
                cursor.execute(select)
                id_login = cursor.fetchone()
                id_login = id_login[0]

                print(id_login)

                insert = f"INSERT INTO endereco(CEP, rua, bairro, cidade, numero, complemento) \
                           VALUES('{zip_code}', '{street}', '{region}', '{city}', '{number}', '{adress_complement}')"
                cursor.execute(insert)
                cnx.connection.commit()

                print("foi")

                select = f"SELECT MAX(codigo) from endereco"
                cursor.execute(select)
                id_adress = cursor.fetchone()
                id_adress = id_adress[0]


                print(id_adress)


                if cliente.count("ON"):
                    permission = f"INSERT INTO permissao(fk_login, tipo) VALUES ('{id_login}', 'cliente' )"
                    cursor.execute(permission)

                    insert = f"INSERT INTO cliente VALUES ('{cpf}', '{name}', '{date_of_birth}', '{sexo}', \
                              '{id_adress}')"
                    cursor.execute(insert)
                    cnx.connection.commit()

                if corretor.count("ON"):
                    permission = f"INSERT INTO permissao(fk_login, tipo) VALUES ('{id_login}', 'corretor' )"
                    cursor.execute(permission)

                    horario_inicio = request.form.get("InputHorarioInicialCorretor")
                    horario_final = request.form.get("InputHorarioFinalCorretor")

                    insert = f"INSERT INTO corretor VALUES ('{cpf}', '{name}', '{date_of_birth}', '{sexo}', \
                              '{id_adress}', '{horario_inicio}', '{horario_final}')"
                    cursor.execute(insert)
                    cnx.connection.commit()
    
                if proprietario.count("ON"):
                    permission = f"INSERT INTO permissao(fk_login, tipo) VALUES ('{id_login}', 'proprietario')"
                    cursor.execute(permission)

                    insert = f"INSERT INTO cliente VALUES ('{cpf}', '{name}', '{date_of_birth}', '{sexo}', \
                              '{id_adress}')"
                    cursor.execute(insert)
                    cnx.connection.commit()

            except Exception as ex:
                print(ex)
        
            return render_template('sign_up.html')
        else:
            return render_template('sign_up.html')
    else:
        return render_template('sign_up.html')
  
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