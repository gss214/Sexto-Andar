class Endereco:
    def __init__(self, codigo, CEP, rua, bairro, cidade, estado, numero, complemento):
        self.codigo = codigo
        self.CEP = CEP
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.numero = numero
        self.complemento = complemento

# Endereco Padrao Data Access Object
class EnderecoDAO:
    def __init__(self):
        pass

    def create(self, cursor, endereco):
        try:
            data = {'CEP': endereco.CEP, 'rua': endereco.rua, 'bairro': endereco.bairro,
                    'cidade': endereco.cidade, 'estado': endereco.estado, 'numero': endereco.numero, 'complemento': endereco.complemento}
            sql = "INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) \
                VALUES (%(CEP)s, %(rua)s, %(bairro)s, %(cidade)s, %(estado)s, %(numero)s, %(complemento)s)"
            cursor.execute(sql, data)

            sql_max = f"SELECT MAX(codigo) from endereco"
            cursor.execute(sql_max)
            id_adress = cursor.fetchone()
            endereco.codigo = id_adress[0]
        except Exception as ex:
            print(ex)

    def update(self, cursor, endereco, codigo):
        try:
            data = {'codigo': codigo, 'CEP': endereco.CEP, 'rua': endereco.rua, 'bairro': endereco.bairro,
                    'cidade': endereco.cidade, 'estado': endereco.estado, 'numero': endereco.numero, 'complemento': endereco.complemento}
            sql = "UPDATE endereco SET CEP = %(CEP)s, rua = %(rua)s, bairro = %(bairro)s, \
                cidade = %(cidade)s, estado = %(estado)s, numero = %(numero)s, complemento = %(complemento)s \
                WHERE codigo = %(codigo)s"
            cursor.execute(sql, data)
        except Exception as ex:
            print(ex)

    def delete(self, cursor, codigo):
        try:
            sql = f"DELETE FROM endereco WHERE codigo = '{codigo}'"
            cursor.execute(sql)
        except Exception as ex:
            print(ex)

    def find_by_id(self, cursor, codigo):
        try:
            sql = f"SELECT * FROM endereco WHERE codigo = '{codigo}'"
            cursor.execute(sql)
            result = cursor.fetchone()

            codigo, CEP, rua, bairro, cidade, estado, numero, complemento = result
            endereco = Endereco(codigo, CEP, rua, bairro, cidade, estado, numero, complemento)
            return endereco
        except Exception as ex:
            print(ex)
            return None

    def find_all(self, cursor):
        try:
            sql = "SELECT * FROM endereco"
            cursor.execute(sql)
            result = cursor.fetchall()

            # depois ver como retornar
            return result
        except Exception as ex:
            print(ex)
            return None


