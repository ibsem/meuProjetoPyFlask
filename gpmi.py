from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "root"
app.config['MYSQL_DB'] = "gpmio"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)
        
SQL_BUSCA_JOGOS = 'SELECT id, nome, descricao from projeto'

class Projeto:
    def __init__(self, nome, descricao, id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao

def traduz_projetos(projetos):
    def cria_projeto_com_tupla(tupla):
        return Projeto(tupla[1], tupla[2], id=tupla[0])
    return list(map(cria_projeto_com_tupla, projetos))


@app.route('/')
def index():
    cursor = db.connection.cursor()
    cursor.execute(SQL_BUSCA_JOGOS)
    listaProjetos = traduz_projetos(cursor.fetchall())
    tituloTabela =  "Lista de Projetos"
    return render_template('lista.html', titulo = tituloTabela, projetos=listaProjetos)

@app.route('/create')  
def create():
    
    return render_template('create.html')

@app.route('/update')  
def update():
    return render_template('update.html')

@app.route('/delete')  
def delete():
    return render_template('delete.html')

app.run(debug=True)
