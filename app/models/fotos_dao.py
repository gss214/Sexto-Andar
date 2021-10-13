class Fotos:
    def __init__(self, codigo, fk_imovel, foto, data_foto, descricao):
        self.codigo = codigo
        self.fk_imovel = fk_imovel
        self.foto = foto
        self.data_foto = data_foto
        self.descricao = descricao
        
class FotosDAO:
    def __init__(self):
        pass

    def find_by_imovel(self, cursor, fk_imovel):
        try:
            sql = f"SELECT * FROM fotos WHERE fk_imovel = '{fk_imovel}'"
            cursor.execute(sql)
            result = cursor.fetchone()
            codigo, fk_endereco, foto, data_foto, descricao = result
            fotos = Fotos(codigo, fk_endereco, foto, data_foto, descricao)
            print(foto)
            return fotos
        except Exception as ex:
            print(ex)
            return None

    def find_all(self, cursor):
        try:
            sql = "SELECT * FROM fotos"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as ex:
            print(ex)
            return None