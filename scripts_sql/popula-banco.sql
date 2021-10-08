use sextoandar;

#------------- Corretores --------------------#

INSERT INTO login(email, senha, permissao) VALUES ('bernadoManuel@example.com', '12345', 'corretor');
INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('85022602', 'Rua Douglas Rodrigo Sanquetta', 'Boqueirão', 'Guarapuava', 'parana', 947, 'apt 202');
INSERT INTO corretor(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login, horario_trabalho_inicio, horario_trabalho_final) VALUES
('89733127400','Bernardo Manuel Paulo Caldeira', '1997-09-21', 'masculino', 1, 1, '10:00', '19:00');

INSERT INTO login(email, senha, permissao) VALUES ('flaviacatarina@example.com', '12345', 'corretor');
INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('79032440', 'Rua João Félix Gonçalves', 'Vila do Polonês', 'Campo Grande', 'mato grosso do sul', 570, 'apt 12');
INSERT INTO corretor(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login, horario_trabalho_inicio, horario_trabalho_final) VALUES
('23842822472','Flávia Catarina Josefa Gomes', '2000-03-07', 'feminino', 2, 2, '10:00', '19:00');

INSERT INTO login(email, senha, permissao) VALUES ('oliviagalvao@example.com', '12345', 'corretor');
INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('55299490', 'Rua Professora Cecília Rodrigues', 'Severiano Moraes Filho', 'Garanhus', 'pernambuco', 700, 'apt 42');
INSERT INTO corretor(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login, horario_trabalho_inicio, horario_trabalho_final) VALUES
('84223746928','Olivia Mariane Galvão', '1998-12-17', 'feminino', 3, 3, '08:00', '16:00');

#------------- Clientes --------------------#

INSERT INTO login(email, senha, permissao) VALUES ('gionunes@example.com', '12345', 'cliente');
INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('78559129', 'Rua Santa Margarete', 'Residencial São Francisco', 'Sinop', 'mato grosso', 859, 'apt 541');
INSERT INTO cliente(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login) VALUES
('87919993164','Giovana Sandra Nunes', '2000-12-10', 'feminino', 4, 4);

INSERT INTO login(email, senha, permissao) VALUES ('geraldo@example.com', '12345', 'cliente');
INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('76824260', 'Rua Francisco Barros', 'Igrapé', 'Porto Velho', 'rondonia', 341, 'casa verde');
INSERT INTO cliente(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login) VALUES
('03764923091', 'Geraldo Raimundo Monteiro', '1966-06-01', 'outros', 5, 5);

INSERT INTO login(email, senha, permissao) VALUES ('benicio.gabriel@example.com', '12345', 'cliente');
INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('66913070', 'Travessa Eurico Romariz', 'Chapéu Virado (Mosqueiro)', 'Belém', 'para', 757, 'apt 109');
INSERT INTO cliente(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login) VALUES
('03475805138', 'Benício Gabriel Joaquim Figueiredo', '1977-03-14', 'masculino', 6, 6);

#------------- Proprietarios --------------------#

INSERT INTO login(email, senha, permissao) VALUES ('marlisantos@example.com', '12345', 'proprietario');
INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('77427002', 'Rua B2', 'Residencial Jardim América', 'Gurupi', 'tocantins', 812, 'apt 15');
INSERT INTO proprietario(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login) VALUES
('21481577794', 'Marli Mirella dos Santos', '1980-01-09', 'feminino', 7, 7);

INSERT INTO login(email, senha, permissao) VALUES ('marcelomoreira@example.com', '12345', 'proprietario');
INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('33010240', 'Rua de Santana', 'Centro', 'Santa Luzia', 'minas gerais', 706, 'apt 652');
INSERT INTO proprietario(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login) VALUES
('70324744897', 'Marcelo Anderson Moreira', '1967-12-19', 'masculino', 8, 8);

INSERT INTO login(email, senha, permissao) VALUES ('margot@example.com', '12345', 'proprietario');
INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('77060304', 'Rua dos Colibris', 'Jardim Santa Bárbara', 'Palmas', 'tocantins', 177, 'apt 5');
INSERT INTO proprietario(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login) VALUES
('70600205860', 'Margot Elise Robbie', '1990-06-02', 'feminino', 9, 9);

#------------- ADM's --------------------#

INSERT INTO login(email, senha, permissao) VALUES ('duda@adm.com', '12345', 'adm');
INSERT INTO login(email, senha, permissao) VALUES ('gui@adm.com', '12345', 'adm');

select * from login;
select * from permissao;
select * from endereco;
select * from corretor;
select * from cliente;
select * from proprietario;


