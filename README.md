<img src="https://github.com/gss214/Sexto-Andar/blob/main/app/static/imgs/logo.png" width="300" height="50">

Projeto final da disciplina de Banco de Dados da UnB em 2021.1

## Criando e acessando o ambiente virtual
É preciso primeiro ter o python instalado em sua máquina. O projeto foi realizado em Python na versão 3.9.7

Em seu terminal, entre no diretório desejado.
Digite o comando `python -m venv env`, isso criará a pasta `env`. Após isso, entre no ambiente virtual executando o arquivo `Activate.ps1` que está na pasta `Scripts`, você pode fazer isso digitando o comando `.\env\Scripts\Activate.ps1` se você estiver utilizando o terminal `Powershell`.

No Microsoft Windows, pode ser necessário ativar o script Activate.ps1, definindo a política de execução para o usuário. Você pode fazer isso executando o seguinte comando do PowerShell:

`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

## Instalando bibliotecas utilizadas

Em seu terminal, entre no diretório desejado.
Digite o comando `pip install -r requirements.txt`, isso deverá instalar todas as bibliotecas utilizadas no projeto.

## Criando o banco de dados

Nesse projeto foi usado o programa MySQL Workbrench, nele execute o script [banco-de-dados.sql](scripts_sql/banco-de-dados.sql) para gerar o banco de dados. 

No arquivo [config.py](confg.py) preencha os valores do `user` e `password` segundo sua conexão com MySQL

## Populando o banco de dados

No MySQL Workbrench execute o comando `SELECT @@secure_file_priv;`, copie todas as imagens da pasta [imagens](imagens/) para o caminho exibido. Em seguida execute o script [popula-banco.sql](scripts_sql/popula-banco.sql) para popular o banco.

## Executando o Projeto

Em seu terminal, digite o comando `python run.py` e acesse em seu navegador o endereço `http://127.0.0.1:5000/` que será disponibilizado no próprio terminal ao executar o comando.
