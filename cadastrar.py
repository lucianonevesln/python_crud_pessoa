from flask import Flask, request, render_template, jsonify
from flaskext.mysql import MySQL
import config


mysql = MySQL()


app = Flask(__name__)


app.config['MYSQL_DATABASE_DB'] = config.DB
app.config['MYSQL_DATABASE_USER'] = config.USER
app.config['MYSQL_DATABASE_PASSWORD'] = config.PASS
app.config['MYSQL_DATABASE_HOST'] = config.DB_URL


mysql.init_app(app)


def cadastrar_pessoas2(nome, cpf):
    if nome and cpf:
         conn = mysql.connect()
         cursor = conn.cursor()
         cursor.execute(
             'insert into python_crud_pessoas.pessoas (nome, cpf) values (%s, %s);', 
             (nome, cpf)
             )
         conn.commit()
         cursor.close()
         conn.close()
         return render_template('pessoas.html')


def cadastrar_contatos2(id_pessoas, telefone, email):
    if id_pessoas and telefone and email:
         conn = mysql.connect()
         cursor = conn.cursor()
         cursor.execute(
             'insert into python_crud_pessoas.contatos (id_pessoas, telefone, email) values (%s, %s, %s);', 
             (id_pessoas, telefone, email)
             )
         conn.commit()
         cursor.close()
         conn.close()
         return render_template('contatos.html')