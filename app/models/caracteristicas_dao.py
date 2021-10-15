class Caracteristicas:
    def __init__(self, codigo, descricao, quantidade_de_quartos, quantidade_de_banheiros, quantidade_de_suites,
area, vaga_garagem):
        self.codigo = codigo
        self.descricao = descricao
        self.quantidade_de_quartos = quantidade_de_quartos
        self.quantidade_de_banheiros = quantidade_de_banheiros
        self.quantidade_de_suites = quantidade_de_suites
        self.area = area
        self.vaga_garagem = vaga_garagem

class CaracteristicasDAO:
    def __init__(self):
        pass

    def find_by_id(self, cursor, codigo):
        try:
            sql = f"SELECT * FROM caracteristicas WHERE codigo = '{codigo}'"
            cursor.execute(sql)
            result = cursor.fetchone()

            codigo, descricao, quantidade_de_quartos, quantidade_de_banheiros, quantidade_de_suites, area, vaga_garagem = result
            caracteristicas = Caracteristicas(codigo, descricao, quantidade_de_quartos, quantidade_de_banheiros, quantidade_de_suites, area, vaga_garagem)
            return caracteristicas
        except Exception as ex:
            print(ex)
            return None

    def find_all(self, cursor):
        try:
            sql = "SELECT * FROM caracteristicas"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as ex:
            print(ex)
            return None


