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

# Gerencimaneto de projetos com Django
Site para gerenciamento de eventos desenvolvido com o framework web Python Django

![Alt Text](https://media3.giphy.com/media/DCfMf73sT3awhZTCD2/giphy.gif?cid=790b7611498168649508e45e4577644a2f7f14c8375895d7&rid=giphy.gif&ct=g)
![](./e.gif)

## Funcionalidades do site

### 1. Gerencimaneto de projetos
- Cadastro de projetos.
- Editão de projetos.
- Exclução de projetos.
- Busca poo projetos.
- Listagen de projetos do usuário autenticado.

### 2. Gerencimaneto de servições dos projetos
- Cadastrar serviço para o projeto.
- Editar o serviço cadastrado.
- Exluir serviço.
- Listas servições do projetos.
- Buscar servirço especifico.
- Verificar se o preço do serviço está dentro do orsamento.

### 3. Autenticação
- Login de usuário
- Cadastro de usuário
- Edição de dados de usuário
- Exlução de conta de usuário

