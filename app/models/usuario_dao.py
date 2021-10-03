class Usuario:
    def __init__(self, cpf, nome, data_de_nascimento, sexo, fk_endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.sexo = sexo
        self.fk_endereco = fk_endereco