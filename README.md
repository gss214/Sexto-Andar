# Sexto Andar
Projeto final da disciplina de Banco de Dados da UnB em 2021.1

## Criando e acessando o ambiente virtual
 
Em seu terminal, entre no diretório desejado.
Digite o comando `python -m venv env`, isso criará a pasta `env`. Após isso, entre no ambiente virtual executando o arquivo `Activate.ps1` que está na pasta `Scripts`, você pode fazer isso digitando o comando `.\env\Scripts\Activate.ps1` se você estiver utilizando o terminal `Powershell`.

## Instalando bibliotecas utilizadas

Em seu terminal, entre no diretório desejado.
É preciso primeiro ter o python instalado em sua máquina.
Digite o comando `pip install -r requirements.txt`, isso deverá instalar todas as bibliotecas utilizadas no projeto.

## Executando o Projeto

Em seu terminal, entre no diretório `app`.
Digite o comando `python app.py` e acesse em seu navegador o endereço `http://127.0.0.1:5000/` que será disponibilizado no próprio terminal ao executar o comando.

## TODO

- site do diagrama mer [https://www.diagrams.net/](https://www.diagrams.net/)

- [x] Terminar CRUD cliente, proprientario, endereço (Duda)

- [x] Adicionar try em todos os metodos que acessa o BD (Gui)

- [x] Criar modelo relacional (Duda)

- [x] Popular o banco de dados (Duda)

- [x] Criar pagina de anuncios 

- [x] Criar a view e a procedure 

- [x] Adicionar o blob da img do apt no BD 

- [x] Arrumar dados recebidos do CRUD (Duda)

- [ ] Popular contrato (dados antigos) e visita

## Bugs

- [ ] Bug do delete que fica pra sempre quando deleta algo do BD

- [x] Bug no login, quando loga errado o retorno da msg eh o proprio erro

- [x] Bug no botão voltar na página sign_up, ele não volta pro login

- [x] Bug no sexo 🤪 (masculino ta sendo cadastrados como outros)

- [x] Bug CRUD dos botões

- [x] Bug no check do corretor, os horarios não somem quando muda o check pra cliente ou proprietario

## Extras

- [ ] Adicionar confirmação ao remover do BD (tipo: "Vc tem certeza? Sim Nao")

- [ ] Exibir a img que ta no BD na pagina de anuncios

- [ ] Quando criar usuario aparacer um popup de sucesso e voltar para a página anterior

- [ ] Padronizar código

## Thoughts

- A ana falou para trocar sexo por gênero (podemos trocar só o nome no site dps)

- View podia mostrar todos os dados do imoveis

## Duvidas

- Relacionamento nos diagramas MER e MR
- Nao esta excluindo os dados em cascata
- Diagrama da camada de mapeamento
