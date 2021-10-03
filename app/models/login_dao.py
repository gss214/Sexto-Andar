class Login:
    def __init__(self, codigo, email, senha):
        self.codigo = codigo
        self.email = email
        self.senha = senha

# Login Padrao Data Access Object
class LoginDAO:
    def __init__(self):
        pass

    def create(self, cursor, login):
        data = {'email': login.email, 'senha': login.senha}
        sql = "INSERT INTO login(email, senha) VALUES (%(email)s, %(senha)s)"
        cursor.execute(sql, data)

        # verificar necessidade do MAX
        sql_max = f"SELECT MAX(codigo) from login"
        cursor.execute(sql_max)
        id_login = cursor.fetchone()
        login.codigo = id_login[0]

    def update(self, cursor, login, codigo):
        data = {'codigo': codigo, 'email': login.email, 'senha': login.senha}
        sql = "UPDATE login SET email = %(email)s, senha = %(senha)s WHERE codigo = %(codigo)s"
        cursor.execute(sql, data)

    def delete(self, cursor, login, codigo):
        sql = f"DELETE FROM login WHERE codigo = '{codigo}'"
        cursor.execute(sql)

    def find_by_id(self, cursor, codigo):
        sql = f"SELECT * FROM login WHERE codigo = '{codigo}'"
        cursor.execute(sql)
        result = cursor.fetchone()

        codigo, email, senha = result
        login = Login(codigo, email, senha)
        return login

    def find_all(self, cursor):
        sql = "SELECT * FROM login"
        cursor.execute(sql)
        result = cursor.fetchall()

        # depois ver como retornar
        return result


