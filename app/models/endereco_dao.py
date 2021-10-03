class Endereco:
    def __init__(self, codigo, CEP, rua, bairro, cidade, numero, complemento):
        self.codigo = codigo
        self.CEP = CEP
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.numero = numero
        self.complemento = complemento

# Endereco Padrao Data Access Object
class EnderecoDAO:
    def __init__(self):
        pass

    def create(self, cursor, endereco):
        print(1)
        data = {'CEP': endereco.CEP, 'rua': endereco.rua, 'bairro': endereco.bairro,
                'cidade': endereco.cidade, 'numero': endereco.numero, 'complemento': endereco.complemento}
        print(2)
        sql = "INSERT INTO endereco(CEP, rua, bairro, cidade, numero, complemento) \
               VALUES (%(CEP)s, %(rua)s, %(bairro)s, %(cidade)s, %(numero)s, %(complemento)s)"
        print(3)
        cursor.execute(sql, data)
        print(4)

        sql_max = f"SELECT MAX(codigo) from endereco"
        print(5)
        cursor.execute(sql_max)
        print(6)
        id_adress = cursor.fetchone()
        print(7)
        endereco.codigo = id_adress[0]
        print(8)

    def update(self, cursor, endereco, codigo):
        data = {'codigo': codigo, 'CEP': endereco.CEP, 'rua': endereco.rua, 'bairro': endereco.bairro,
                'cidade': endereco.cidade, 'numero': endereco.numero, 'complemento': endereco.complemento}
        sql = "UPDATE endereco SET CEP = %(CEP)s, rua = %(rua)s, bairro = %(bairro)s, \
               cidade = %(cidade)s, numero = %(numero)s, complemento = %(complemento)s \
               WHERE codigo = %(codigo)s"
        cursor.execute(sql, data)

    def delete(self, cursor, codigo):
        sql = f"DELETE FROM endereco WHERE codigo = '{codigo}'"
        cursor.execute(sql)

    def find_by_id(self, cursor, codigo):
        sql = f"SELECT * FROM endereco WHERE codigo = '{codigo}'"
        cursor.execute(sql)
        result = cursor.fetchone()

        codigo, CEP, rua, bairro, cidade, numero, complemento = result
        endereco = Endereco(codigo, CEP, rua, bairro, cidade, numero, complemento)
        return endereco

    def find_all(self, cursor):
        sql = "SELECT * FROM endereco"
        cursor.execute(sql)
        result = cursor.fetchall()

        # depois ver como retornar
        return result


