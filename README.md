npm# Bem vindo ao Sistema de rebalanceamento de carteira FinanceApp

 - Esse sistema foi desenvolvido com a intenção de facilitar meus aportes em minha carteira de investimentos, sempre tive a dificuldade de calcular quanto comprar de cada cota, sendo acão, Fii, BDR ou Renda Fixa, para respeitar meu balanceamento, então desenvolvi este projeto inicialmente com uma tabela em excel e depois como hobbie e desafio utilizando angular e django.


 ![Home](https://github.com/GuilhermeUchoa/WalletUp/blob/main/frontEnd/src/assets/Home.png)

 # Para instalar este projeto eu seu PC:

 - tenha instalado python e nodejs
 - node
 - pip install -r requirements.txt
 - node start

 # Para iniciar este projeto eu seu PC:
 
 - cd backEndApiFinanceApp
 - python manage.py makemigrations
 - python manage.py migrate
 - python manage.py runserver (sua api estara rodando porta:8000)

 - ng start (para instalar os repositorios node_modules)
 - ng serve para iniciar o projeto (porta:4200)

# Rodar atualizacao de cotacao

estou usando o celery


# Metas

[x] - Criar Buscador

[x] - criar uma api que manda as cotacoes

[x] - criar um back end com django restFramework

[x] - Arrumar Porcentagens e metas bugadas no buscador

[x] - Se nao tiver como atualizaliar entao devo criar um novo ativo, criar essa feature

[x] - BackEnd Excel para carteira com erro

[x] - Sinalizar compra quando o preco medio e a porcentagem meta sinalizar

[x] - Sincronizar com o OneDrive

[x] - preco medio anual calculado

[x] - preco medio acumulativo 

[x] - Ajustar o Login

[x] - Ajustar o banco de dados


[x] - Ajustar algoritmo que coloca ativo na carteira

[x] - Ajustar Banco de dados com uma central, onde os clientes apenas copiam os valores atualizados, sem exceder a requisição a Api

[x] - Django djoser vai ser mais facil implementar a parte de backend

[ ] - Refatorar e refatorar

[x] - Criar registro de novas contas

[ ] - Criar recuperacao de senha

[ ] - Ajustar as informacoes de DY e valuation em geral

[x] - Ajustar dashboard detalhe

[ ] - Colocar o celery para atualizar as cotacoes