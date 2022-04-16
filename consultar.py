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


def consultar_pessoas2():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select * from python_crud_pessoas.pessoas;')
    autores = cursor.fetchall()
    conn.commit()
    return jsonify(autores)
    cursor.close()
    conn.close()


def consultar_contatos2():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select * from python_crud_pessoas.contatos;')
    nomes = cursor.fetchall()
    conn.commit()
    return jsonify(nomes)
    cursor.close()
    conn.close()


def consultar_pessoas_contatos2():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select p.nome, p.cpf, c.telefone, c.email from python_crud_pessoas.pessoas as p inner join python_crud_pessoas.contatos as c on c.id_pessoas = p.id;')
    nomes = cursor.fetchall()
    conn.commit()
    return jsonify(nomes)
    cursor.close()
    conn.close()