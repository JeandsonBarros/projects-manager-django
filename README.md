`python -m venv venv`
`venv\Scripts\activate`
`pip install Django`
`django-admin startproject django_project .`
`python manage.py startapp app_exemplo`
`python manage.py runserver`
`python manage.py makemigrations`
`python manage.py migrate`
`pip freeze > requirements.txt`
`pip install -r requirements.txt`
`python manage.py createsuperuser`

# Gerenciamento de projetos com Django
Site para gerenciamento de projetos, desenvolvido com o framework web Python Django.

O site conta com as seguintes funcionalidades:
[1. Gerenciamento de projetos](#1-gerenciamento-de-projetos)<br />
[2. Gerenciamento de serviços de projetos](#2-gerenciamento-de-serviços-de-projetos)<br />
[3. Autenticação.](#3-autenticação)<br />

![Alt Text](https://media3.giphy.com/media/DCfMf73sT3awhZTCD2/giphy.gif?cid=790b7611498168649508e45e4577644a2f7f14c8375895d7&rid=giphy.gif&ct=g)
![](./e.gif)

## Execução

## Funcionalidades do site

### 1. Gerenciamento de projetos
- Cadastro de projetos.
- Edição de projetos.
- Exclusão de projetos.
- Busca por projetos.
- Listagem de projetos do usuário autenticado.

### 2. Gerenciamento de serviços de projetos
- Cadastrar serviço para o projeto.
- Editar o serviço cadastrado.
- Excluir serviço.
- Listas serviços dos projetos.
- Buscar serviço específico.
- Verificar se o preço do serviço está dentro do orçamento.

### 3. Autenticação
- Login de usuário
- Cadastro de usuário
- Edição de dados de usuário
- Exclusão de conta de usuário



