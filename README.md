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

- [ ] Terminar CRUD cliente, proprientario, endereço

- [ ] Adicionar try em todos os metodos que acessa o BD

- [ ] Criar as views

- [ ] Adicionar o blob da img do apt no BD

- [ ] Implementar a procedure

## Bugs

- [ ] Bug do delete que fica pra sempre quando deleta algo do BD

- [x] Bug no login, quando loga errado o retorno da msg eh o proprio erro

- [x] Bug no botão voltar na página sign_up, ele não volta pro login

- [ ] Bug no sexo 🤪 (masculino ta sendo cadastrados como outros)

- [ ] Bug no check do corretor, os horarios não somem quando muda o check pra cliente ou proprietario

## Extras

- [ ] Adicionar confirmação ao remover do BD (tipo: "Vc tem certeza? Sim Nao")

- [ ] Fazer uma página de anuncios

- [ ] Exibir a img que ta no BD na pagina de anuncios

## Thoughts

- Quando adiciona um usuario via CRUD tem que adicionar o endereço antes, pensar em um jeito de deixar dinamico para nao dar ruim com os códigos de PK e FK

- A ana falou para trocar sexo por gênero