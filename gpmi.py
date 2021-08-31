from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "root"
app.config['MYSQL_DB'] = "gpmio"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)

def funcaoSoma(a,b):
    c = a + b
    return c

@app.route('/')
def index():
    tituloTabela =  "Lista de Projetos"
    return render_template('lista.html', titulo = tituloTabela)

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
