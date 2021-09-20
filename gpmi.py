# ---------- Aula 19/09
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

#Configuração do Banco de Dados
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "root"
app.config['MYSQL_DB'] = "gpmio"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)

# Definição dos Comandos SQL para o Banco de Dados        
SQL_LISTA_JOGOS = 'SELECT id, nome, descricao from projeto'
SQL_CREATE_JOGO = 'INSERT into projeto (nome, descricao) values (%s, %s)'

#Definicição das Classes que vai trabalhar
class Projeto:
    def __init__(self, nome, descricao, id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao

#Organiza os dados que recebe do Banco de Dados em lista de Tuplas
def traduz_projetos(projetos):
    def cria_projeto_com_tupla(tupla):
        return Projeto(tupla[1], tupla[2], id=tupla[0])
    return list(map(cria_projeto_com_tupla, projetos))

# Rotas que identificam as diferentes requisiçoes para o FLASK
@app.route('/')
def index():
    cursor = db.connection.cursor()
    cursor.execute(SQL_LISTA_JOGOS)
    listaProjetos = traduz_projetos(cursor.fetchall())
    tituloTabela =  "Lista de Projetos"
    return render_template('lista.html', titulo = tituloTabela, projetos=listaProjetos)

#----- Aula de 20/09 --------------
@app.route('/new')
def new():
    titulo = "Inserir Novo Projeto"
    return render_template('create.html', titulo=titulo)

@app.route('/create', methods=['POST'])  
def create():
    nome = request. form['nome']
    descricao = request. form['descricao']
    projeto = Projeto(nome, descricao)
    cursor = db.connection.cursor()
    cursor.execute(SQL_CREATE_JOGO, (projeto.nome, projeto.descricao))
    db.connection.commit()
    return redirect(url_for('index'))
    
#------ Aula 20/09 ----------------

@app.route('/update')  
def update():
    return render_template('update.html')

@app.route('/delete')  
def delete():
    return render_template('delete.html')

app.run(debug=True)
