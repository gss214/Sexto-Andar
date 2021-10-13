class Usuario:
    def __init__(self, cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login):
        self.cpf = cpf
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.sexo = sexo
        self.fk_endereco = fk_endereco
        self.fk_login = fk_login

class UsuarioDAO:

    def __init__(self, table_name):
        self.table_name = table_name
        #pass

    def create(self, cursor, usuario):
        try:
            data = {'table_name': self.table_name, 'cpf': usuario.cpf, 'nome': usuario.nome, 'data_de_nascimento': usuario.data_de_nascimento,
                    'sexo': usuario.sexo, 'fk_endereco': usuario.fk_endereco, 'fk_login': usuario.fk_login}
            sql = "INSERT INTO %(table_name)s VALUES (%(cpf)s, %(nome)s, %(data_de_nascimento)s, %(sexo)s, %(fk_endereco)s, %(fk_login)s)"
            cursor.execute(sql, data)
        except Exception as ex:
            print(ex)

    def update(self, cursor, usuario, cpf):
        try:
            data = {'table_name': self.table_name,'cpf': cpf, 'nome': usuario.nome, 'data_de_nascimento': usuario.data_de_nascimento,
                    'sexo': usuario.sexo, 'fk_endereco': usuario.fk_endereco, 'fk_login': usuario.fk_login}
            sql = "UPDATE %(table_name)s SET nome = %(nome)s, data_de_nascimento = %(data_de_nascimento)s, \
                sexo = %(sexo)s, fk_endereco = %(fk_endereco)s, fk_login = %(fk_login)s WHERE cpf = %(cpf)s"
            cursor.execute(sql, data)
        except Exception as ex:
            print(ex)

    def delete(self, cursor, cpf):
        try:
            sql = f"DELETE FROM {self.table_name} WHERE cpf = '{cpf}'"
            cursor.execute(sql)
        except Exception as ex:
            print(ex)

    def find_by_id(self, cursor, cpf):
        try:
            sql = f"SELECT * FROM {self.table_name} WHERE cpf = '{cpf}'"
            cursor.execute(sql)
            result = cursor.fetchone()
            
            '''cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login = result
            proprietario = Proprietario(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login)
            return proprietario'''

            return result
        except Exception as ex:
            print(ex)
            return None

    def find_all(self, cursor):
        try:
            sql = f"SELECT * FROM {self.table_name}"
            cursor.execute(sql)
            result = cursor.fetchall()

            # depois ver como retornar
            return result
        except Exception as ex:
            print(ex)
            return None