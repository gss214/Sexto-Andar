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

INSERT INTO login(email, senha, permissao) VALUES ('daniloEnzo@example.com', '12345', 'corretor');
INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('64939701', 'Rua Primeiro de Maio', 'São José', 'Araguaína', 'tocantins', 2132, 'Casa 7');
INSERT INTO corretor(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login, horario_trabalho_inicio, horario_trabalho_final) VALUES
('16648973218','Danilo Enzo Fernandes', '1995-04-02', 'masculino', 4, 4, '10:00', '19:00');

INSERT INTO login(email, senha, permissao) VALUES ('isacristiane@example.com', '12345', 'corretor');
INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('75095220', 'Rua Limiro de Oliveira', 'Setor Tropical', 'Anápolis', 'goias', 692, 'apt 208');
INSERT INTO corretor(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login, horario_trabalho_inicio, horario_trabalho_final) VALUES
('11429654147','Isabelle Cristiane Duarte', '1993-11-16', 'feminino', 5, 5, '16:00', '23:00');

#------------- Clientes --------------------#

INSERT INTO login(email, senha, permissao) VALUES ('gionunes@example.com', '12345', 'cliente');
INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('78559129', 'Rua Santa Margarete', 'Residencial São Francisco', 'Sinop', 'mato grosso', 859, 'apt 541');
INSERT INTO cliente(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login) VALUES
('87919993164','Giovana Sandra Nunes', '2000-12-10', 'feminino', 6, 6);

INSERT INTO login(email, senha, permissao) VALUES ('geraldo@example.com', '12345', 'cliente');
INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('76824260', 'Rua Francisco Barros', 'Igrapé', 'Porto Velho', 'rondonia', 341, 'casa verde');
INSERT INTO cliente(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login) VALUES
('03764923091', 'Geraldo Raimundo Monteiro', '1966-06-01', 'outros', 7, 7);

INSERT INTO login(email, senha, permissao) VALUES ('benicio.gabriel@example.com', '12345', 'cliente');
INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('66913070', 'Travessa Eurico Romariz', 'Chapéu Virado (Mosqueiro)', 'Belém', 'para', 757, 'apt 109');
INSERT INTO cliente(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login) VALUES
('03475805138', 'Benício Gabriel Joaquim Figueiredo', '1977-03-14', 'masculino', 8, 8);

INSERT INTO login(email, senha, permissao) VALUES ('sabrina.antgav@example.com', '12345', 'cliente');
INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('59063130', 'Rua Barão do Curumataú', 'Lagoa Nova', 'Natal', 'rio grande do norte', 250, 'Casa 23');
INSERT INTO cliente(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login) VALUES
('59854366405', 'Sabrina Antônia Galvão', '2001-12-17', 'feminino', 9, 9);

INSERT INTO login(email, senha, permissao) VALUES ('marli.malu@example.com', '12345', 'cliente');
INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('70302916', 'SCS Quadra 2 Bloco C Lote 226', 'Asa Sul', 'Brasília', 'distrito federal', 253, 'apt 253');
INSERT INTO cliente(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login) VALUES
('57434241101', 'Marli Malu Assunção', '1998-12-20', 'feminino', 10, 10);

#------------- Proprietarios --------------------#

INSERT INTO login(email, senha, permissao) VALUES ('marlisantos@example.com', '12345', 'proprietario');
INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('77427002', 'Rua B2', 'Residencial Jardim América', 'Gurupi', 'tocantins', 812, 'apt 15');
INSERT INTO proprietario(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login) VALUES
('21481577794', 'Marli Mirella dos Santos', '1980-01-09', 'feminino', 11, 11);

INSERT INTO login(email, senha, permissao) VALUES ('marcelomoreira@example.com', '12345', 'proprietario');
INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('33010240', 'Rua de Santana', 'Centro', 'Santa Luzia', 'minas gerais', 706, 'apt 652');
INSERT INTO proprietario(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login) VALUES
('70324744897', 'Marcelo Anderson Moreira', '1967-12-19', 'masculino', 12, 12);

INSERT INTO login(email, senha, permissao) VALUES ('margot@example.com', '12345', 'proprietario');
INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('77060304', 'Rua dos Colibris', 'Jardim Santa Bárbara', 'Palmas', 'tocantins', 177, 'apt 5');
INSERT INTO proprietario(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login) VALUES
('70600205860', 'Margot Elise Robbie', '1990-06-02', 'feminino', 13, 13);

INSERT INTO login(email, senha, permissao) VALUES ('carlos.ferocha@example.com', '12345', 'proprietario');
INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('52081765', 'Rua Olímpio Bazante', 'Vasco da Gama', 'Recife', 'pernambuco', 438, 'apt 305');
INSERT INTO proprietario(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login) VALUES
('94140965401', 'Carlos Felipe Rocha', '1974-03-10', 'masculino', 14, 14);

INSERT INTO login(email, senha, permissao) VALUES ('tiago.ribeiro@example.com', '12345', 'proprietario');
INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('05653100', 'Rua Gina de Martino', 'Jardim Leonor', 'São Paulo', 'sao paulo', 943, 'apt 906');
INSERT INTO proprietario(cpf, nome, data_de_nascimento, sexo, fk_endereco, fk_login) VALUES
('91396633880', 'Tiago Marcos Ribeiro', '1982-10-23', 'masculino', 15, 15);

#------------- ADM's --------------------#

INSERT INTO login(email, senha, permissao) VALUES ('duda@adm.com', '12345', 'adm');
INSERT INTO login(email, senha, permissao) VALUES ('gui@adm.com', '12345', 'adm');

#------------- Categoria --------------------#

INSERT INTO categoria(descricao) VALUES ('Apartamento'); 
INSERT INTO categoria(descricao) VALUES ('Casa'); 
INSERT INTO categoria(descricao) VALUES ('Kitnet'); 

#------------- Apartamentos --------------------#

INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('77060304', 'Rua dos Colibris', 'Jardim Santa Bárbara', 'Palmas', 'tocantins', 177, 'apt 145');
INSERT INTO precos(aluguel, condominio, iptu, taxas, total) VALUES (1800, 400, 500, 100, 2800);
INSERT INTO caracteristicas(descricao, quantidade_de_quartos, quantidade_de_banheiros, quantidade_de_suites,
area, vaga_garagem) VALUES ('Apartamento em Palmas, com 3 quartos' ,3, 2, 1, 65, 2);
INSERT INTO imovel(fk_endereco, fk_proprietario, fk_categoria, fk_preco, situacao, fk_caracteristicas) VALUES
(16, '70600205860', 1, 1, 'Para alugar', 1);
INSERT INTO fotos(fk_imovel, foto, data_foto, descricao) VALUES
(1, load_file('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\apt1.jpeg'), '2021-10-12', 'Foto do apt');

INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('74365320', 'Rua B 4', 'Setor Novo Horizonte', 'Goiânia', 'Goias', 798, 'apt 146');
INSERT INTO precos(aluguel, condominio, iptu, taxas, total) VALUES (3200, 600, 500, 100, 4400);
INSERT INTO caracteristicas(descricao, quantidade_de_quartos, quantidade_de_banheiros, quantidade_de_suites,
area, vaga_garagem) VALUES ('Apartamento em Goiânia, com 4 quartos', 4, 3, 2, 65, 2);
INSERT INTO imovel(fk_endereco, fk_proprietario, fk_categoria, fk_preco, situacao, fk_caracteristicas) VALUES
(17, '70600205860', 1, 2, 'Para alugar', 2);
INSERT INTO fotos(fk_imovel, foto, data_foto, descricao) VALUES
(2, load_file('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\apt2.jpeg'), '2021-10-12', 'Foto do apt');

INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('04928160', 'Rua Ezequiel Alves Ramos', 'Copacabana', 'São Paulo', 'sao paulo', 871, 'apt 708');
INSERT INTO precos(aluguel, condominio, iptu, taxas, total) VALUES (3500, 500, 210, 100, 4310);
INSERT INTO caracteristicas(descricao, quantidade_de_quartos, quantidade_de_banheiros, quantidade_de_suites,
area, vaga_garagem) VALUES ('Apartamento em São Paulo, com 2 quartos', 2, 2, 2, 70, 2);
INSERT INTO imovel(fk_endereco, fk_proprietario, fk_categoria, fk_preco, situacao, fk_caracteristicas) VALUES
(18, '91396633880', 1, 3, 'Para alugar', 3);
INSERT INTO fotos(fk_imovel, foto, data_foto, descricao) VALUES
(3, load_file('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\apt3.jpeg'), '2021-10-12', 'Foto do apt');

INSERT INTO endereco(CEP, rua, bairro, cidade, estado, numero, complemento) VALUES 
('33147080', 'Rua Dez', 'Castanheira', 'Santa Luzia', 'minas gerais', 903, 'Casa 23');
INSERT INTO precos(aluguel, condominio, iptu, taxas, total) VALUES (2300, 200, 460, 0, 2960);
INSERT INTO caracteristicas(descricao, quantidade_de_quartos, quantidade_de_banheiros, quantidade_de_suites,
area, vaga_garagem) VALUES ('Casa em Santa Luzia, com 3 quartos', 3, 2, 1, 100, 2);
INSERT INTO imovel(fk_endereco, fk_proprietario, fk_categoria, fk_preco, situacao, fk_caracteristicas) VALUES
(19, '70324744897', 2, 4, 'Para alugar', 4);
INSERT INTO fotos(fk_imovel, foto, data_foto, descricao) VALUES
(4, load_file('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\casa1.jpeg'), '2021-10-12', 'Foto da casa');


select * from login;
select * from permissao;
select * from endereco;
select * from corretor;
select * from cliente;
select * from proprietario;
select * from imovel;
select * from caracteristicas;
select * from precos;
select * from fotos;

SELECT @@secure_file_priv;


