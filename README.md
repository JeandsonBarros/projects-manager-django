# Gerenciamento de projetos com Django
Site para gerenciamento de projetos, desenvolvido com o framework web Python Django.

O site conta com as seguintes funcionalidades:<br />
[1. Gerenciamento de projetos](#1-gerenciamento-de-projetos)<br />
[2. Gerenciamento de serviços de projetos](#2-gerenciamento-de-serviços-de-projetos)<br />
[3. Autenticação.](#3-autenticação)<br />

![Alt Text](https://media3.giphy.com/media/DCfMf73sT3awhZTCD2/giphy.gif?cid=790b7611498168649508e45e4577644a2f7f14c8375895d7&rid=giphy.gif&ct=g)
![](./e.gif)

## Execução
Esse projeto foi desenvolvido com o uso do ambiente virtual venv, recomendo que faça o mesmo para exultar o projeto, para diminuir as chances de erro.

### 1. Instalação de dependências
Execute o comando `pip install -r requirements.txt` no seu terminal de comandos para instalar as dependências necessárias.

### 2. Configuração das variáveis de ambiente
Crie um arquivo .env na pasta /django_project e passe as seguintes variáveis para ele:
`SECRET_KEY=''`
`DEBUG=True`

SECRET_KEY é a chave secreta usada na produção, a mantenha em segredo.
DEBUG é a variável responsável por definir se as opções de depuração estarão ativas ou não, recomendo que deixe ativada somente em desenvolvimento.

Se quiser ver como o arquivo .env deve ser veja o .env.exemple em /django_project. 

### 3. Configuração do banco de dados
O projeto foi desenvolvido com o uso do MySQL, mas você também pode usar o SQLite ou instalar e configurar um banco de dados de sua preferência.

#### - Banco de dados MySQL
Caso queira usar o MySQL crie um banco de dados com o nome project_manager e passe as informações do seu banco de dados para a variável DATABASES em /django_project/settings.py como mostra na imagem a seguir:
![Alt Text](./readme_files/print_mysql_configuri.png)
Em seguida execute os seguintes comandos: <br/>
`python manage.py makemigrations` <br/>
`python manage.py migrate`

#### - Banco de dados SQLite
Caso queira usar o SQLite, descomente a variável com as configurações do SQLite e comente as configurações do MySQL em /django_project/settings.py com mostra a imagem a seguir:
![Alt Text](./readme_files/print_sqlite3_configuri.png)
Em seguida execute os seguintes comandos: <br/>
`python manage.py makemigrations` <br/>
`python manage.py migrate`

### 4. Executar servidor
Se os passos anteriores foram executados com sucesso basta executar o comando `python manage.py runserver` e abrir no navegador a URL http://127.0.0.1:8000/
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



