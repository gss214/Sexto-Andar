class Login:
    def __init__(self, codigo, email, senha, permissao):
        self.codigo = codigo
        self.email = email
        self.senha = senha
        self.permissao = permissao

# Login Padrao Data Access Object
class LoginDAO:
    def __init__(self):
        pass

    def create(self, cursor, login):
        try:
            data = {'email': login.email, 'senha': login.senha, 'permissao': login.permissao}
            sql = "INSERT INTO login(email, senha, permissao) VALUES (%(email)s, %(senha)s, %(permissao)s)"
            cursor.execute(sql, data)

            # verificar necessidade do MAX
            #sql_max = f"SELECT MAX(codigo) from login"
            #cursor.execute(sql_max)
            #id_login = cursor.fetchone()
            #login.codigo = id_login[0]

            print("------", cursor.lastrowid)
            login.codigo = cursor.lastrowid
        except Exception as ex:
            print(ex)

    def update(self, cursor, login, codigo):
        try:
            data = {'codigo': codigo, 'email': login.email, 'senha': login.senha, 'permissao' : login.permissao}
            sql = "UPDATE login SET email = %(email)s, senha = %(senha)s, permissao = %(permissao)s WHERE codigo = %(codigo)s"
            cursor.execute(sql, data)
        except Exception as ex:
            print(ex)

    def delete(self, cursor, codigo):
        try:
            sql = f"DELETE FROM login WHERE codigo = '{codigo}'"
            cursor.execute(sql)
        except Exception as ex:
            print(ex)

    def find_by_id(self, cursor, codigo):
        try:
            sql = f"SELECT * FROM login WHERE codigo = '{codigo}'"
            cursor.execute(sql)
            result = cursor.fetchone()

            codigo, email, senha, permissao = result
            login = Login(codigo, email, senha, permissao)
            return login
        except Exception as ex:
            print(ex)
            return None

    def find_without_id(self, cursor, email, senha):
        try:
            sql = f"SELECT * FROM login where email = '{email}' AND senha = '{senha}'"
            cursor.execute(sql)
            result = cursor.fetchone()

            codigo, email, senha, permissao = result
            login = Login(codigo, email, senha, permissao)
            return login
        except:
            return None

    def find_all(self, cursor):
        sql = "SELECT * FROM login"
        cursor.execute(sql)
        result = cursor.fetchall()

        # depois ver como retornar
        return result


