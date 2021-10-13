from app.models.usuario_dao import Usuario

class Proprietario(Usuario):
    def __init__(self, cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login):
        super().__init__(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login)

# Proprietario Padrao Data Access Object
class ProprietarioDAO:
    def __init__(self):
        pass

    def create(self, cursor, proprietario):
        try:
            data = {'cpf': proprietario.cpf, 'nome': proprietario.nome, 'data_de_nascimento': proprietario.data_de_nascimento,
                    'sexo': proprietario.sexo, 'fk_endereco': proprietario.fk_endereco, 'fk_login': proprietario.fk_login}
            sql = "INSERT INTO proprietario VALUES (%(cpf)s, %(nome)s, %(data_de_nascimento)s, %(sexo)s, %(fk_endereco)s, %(fk_login)s)"
            cursor.execute(sql, data)
        except Exception as ex:
            print(ex)

    def update(self, cursor, proprietario, cpf):
        try:
            data = {'cpf': cpf, 'nome': proprietario.nome, 'data_de_nascimento': proprietario.data_de_nascimento,
                    'sexo': proprietario.sexo, 'fk_endereco': proprietario.fk_endereco, 'fk_login': proprietario.fk_login}
            sql = "UPDATE proprietario SET nome = %(nome)s, data_de_nascimento = %(data_de_nascimento)s, \
                sexo = %(sexo)s, fk_endereco = %(fk_endereco)s, fk_login = %(fk_login)s WHERE cpf = %(cpf)s"
            cursor.execute(sql, data)
        except Exception as ex:
            print(ex)

    def delete(self, cursor, cpf):
        try:
            sql = f"DELETE FROM proprietario WHERE cpf = '{cpf}'"
            cursor.execute(sql)
        except Exception as ex:
            print(ex)

    def find_by_id(self, cursor, cpf):
        try:
            sql = f"SELECT * FROM proprietario WHERE cpf = '{cpf}'"
            cursor.execute(sql)
            result = cursor.fetchone()

            cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login = result
            proprietario = Proprietario(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login)
            return proprietario
        except Exception as ex:
            print(ex)
            return None

    def find_all(self, cursor):
        try:
            sql = "SELECT * FROM proprietario"
            cursor.execute(sql)
            result = cursor.fetchall()

            # depois ver como retornar
            return result
        except Exception as ex:
            print(ex)
            return None


