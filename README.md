# Desafio Backend

## Objetivo do projeto

O objetivo do projeto é criar uma interface web que aceite upload de arquivo CNAB, interpretar (parsear) o arquivo recebido
e exibir as operações resumidas pelo nome da empresa e o totalizador do saldo dessa empresa.

## Tecnologias utilizadas

Python (django), JavaScript, HTML

## Passos de instalação:

#### Instalar dependências:

`pip install -r requirements.txt`

#### Gerar banco de dados db.sqlite3:

`python manage.py migrate`

#### Rodar o server

`python manage.py runserver`

URL para testar aplicação: http://127.0.0.1:8000/api/

Um arquivo modelo .txt está na pasta assets para eventuais testes (txt_modelo.txt)

## Passos para execução em ambiente de desenvolvimento:

Para testar, por exemplo pelo Insomnia ir em http://127.0.0.1:8000/api/company/

Para GET não enviar body.

Para POST enviar arquivo binary file com content-type text/plain
