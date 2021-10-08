from app.models.usuario_dao import Usuario

class Cliente(Usuario):
    def __init__(self, cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login):
        super().__init__(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login)

# Cliente Padrao Data Access Object
class ClienteDAO:
    def __init__(self):
        pass

    def create(self, cursor, cliente):
        data = {'cpf': cliente.cpf, 'nome': cliente.nome, 'data_de_nascimento': cliente.data_de_nascimento,
                'sexo': cliente.sexo, 'fk_endereco': cliente.fk_endereco, 'fk_login': cliente.fk_login}
        sql = "INSERT INTO cliente VALUES (%(cpf)s, %(nome)s, %(data_de_nascimento)s, %(sexo)s, %(fk_endereco)s, %(fk_login)s)"
        cursor.execute(sql, data)

    def update(self, cursor, cliente, cpf):
        data = {'cpf': cpf, 'nome': cliente.nome, 'data_de_nascimento': cliente.data_de_nascimento,
                'sexo': cliente.sexo, 'fk_endereco': cliente.fk_endereco, 'fk_login': cliente.fk_login}
        sql = "UPDATE cliente SET nome = %(nome)s, data_de_nascimento = %(data_de_nascimento)s, \
               sexo = %(sexo)s, fk_endereco = %(fk_endereco)s, fk_login = %(fk_login)s  WHERE cpf = %(cpf)s"
        cursor.execute(sql, data)

    def delete(self, cursor, cpf):
        sql = f"DELETE FROM cliente WHERE cpf = '{cpf}'"
        cursor.execute(sql)

    def find_by_id(self, cursor, cpf):
        sql = f"SELECT * FROM cliente WHERE cpf = '{cpf}'"
        cursor.execute(sql)
        result = cursor.fetchone()

        cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login = result
        cliente = Cliente(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login)
        return cliente

    def find_by_fk(self, cursor, fk_login):
        sql = f"SELECT * FROM cliente WHERE fk_login = {fk_login}"
        cursor.execute(sql)
        result = cursor.fetchone()

        cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login = result
        cliente = Cliente(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login)
        return cliente

    def find_all(self, cursor):
        sql = "SELECT * FROM cliente"
        cursor.execute(sql)
        result = cursor.fetchall()

        # depois ver como retornar
        return result


