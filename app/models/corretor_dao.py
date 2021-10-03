from app.models.usuario_dao import Usuario

class Corretor(Usuario):
    def __init__(self, cpf, nome, data_de_nascimento, sexo, fk_endereco, horario_trabalho_inicio, horario_trabalho_final):
        super.__init__(cpf, nome, data_de_nascimento, sexo, fk_endereco)
        self.horario_trabalho_inicio = horario_trabalho_inicio
        self.horario_trabalho_final = horario_trabalho_final

# Corretor Padrao Data Access Object
class CorretorDAO:
    def __init__(self):
        pass

    def create(self, cursor, corretor):
        data = {'cpf': corretor.cpf, 'nome': corretor.nome, 'data_de_nascimento': corretor.data_de_nascimento,
                'sexo': corretor.sexo, 'fk_endereco': corretor.fk_endereco, 
                'horario_trabalho_inicio': corretor.horario_trabalho_inicio, 'horario_trabalho_final': corretor.horario_trabalho_final}
        sql = "INSERT INTO corretor VALUES (%(cpf)s, %(nome)s, %(data_de_nascimento)s, %(sexo)s, %(fk_endereco)s, \
               %(horario_trabalho_inicio)s, %(horario_trabalho_final)s)"
        cursor.execute(sql, data)

    def update(self, cursor, corretor, cpf):
        data = {'cpf': corretor.cpf, 'nome': corretor.nome, 'data_de_nascimento': corretor.data_de_nascimento,
                'sexo': corretor.sexo, 'fk_endereco': corretor.fk_endereco, 
                'horario_trabalho_inicio': corretor.horario_trabalho_inicio, 'horario_trabalho_final': corretor.horario_trabalho_final}
        sql = "UPDATE corretor SET nome = %(nome)s, data_de_nascimento = %(data_de_nascimento)s, \
               sexo = %(sexo)s, fk_endereco = %(fk_endereco)s, horario_trabalho_inicio = %(horario_trabalho_inicio)s, \
               horario_trabalho_final = %(horario_trabalho_final)s WHERE cpf = %(cpf)s"
        cursor.execute(sql, data)

    def delete(self, cursor, cpf):
        sql = f"DELETE FROM corretor WHERE cpf = '{cpf}'"
        cursor.execute(sql)

    def find_by_id(self, cursor, cpf):
        sql = f"SELECT * FROM corretor WHERE cpf = '{cpf}'"
        cursor.execute(sql)
        result = cursor.fetchone()

        cpf, nome, data_de_nascimento, sexo, fk_endereco, horario_trabalho_inicio, horario_trabalho_final = result
        corretor = Corretor(cpf, nome, data_de_nascimento, sexo, fk_endereco, horario_trabalho_inicio, horario_trabalho_final)
        return corretor

    def find_all(self, cursor):
        sql = "SELECT * FROM corretor"
        cursor.execute(sql)
        result = cursor.fetchall()

        # depois ver como retornar
        return result


