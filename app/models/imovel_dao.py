class Imovel:
    def __init__(self, codigo, fk_endereco, fk_proprietario, fk_categoria, fk_preco, situacao, fk_caracteristicas):
        self.codigo = codigo
        self.fk_endereco = fk_endereco
        self.fk_proprietario = fk_proprietario
        self.fk_categoria = fk_categoria
        self.fk_preco = fk_preco
        self.situacao = situacao
        self.fk_caracteristicas = fk_caracteristicas

class ImovelDAO:
    def __init__(self):
        pass

    def find_by_id(self, cursor, codigo):
        try:
            sql = f"SELECT * FROM imovel WHERE codigo = '{codigo}'"
            cursor.execute(sql)
            result = cursor.fetchone()

            codigo, fk_endereco, fk_proprietario, fk_categoria, fk_preco, situacao, fk_caracteristicas = result
            imovel = Imovel(codigo, fk_endereco, fk_proprietario, fk_categoria, fk_preco, situacao, fk_caracteristicas)
            return imovel
        except Exception as ex:
            print(ex)
            return None

    def find_all(self, cursor):
        try:
            sql = "SELECT * FROM imovel"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as ex:
            print(ex)
            return None