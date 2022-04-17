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


def _select_sql(raw_sql)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(raw_sql)
    result = cursor.fetchall()
    # conn.commit()
    cursor.close()
    conn.close()
    return result


def consultar_pessoas2():
    autores = _select_sql('SELECT * FROM PYTHON_CRUD_PESSOAS.PESSOAS;')
    return jsonify(autores)


def consultar_contatos2():
    nomes = _select_sql('SELECT * FROM PYTHON_CRUD_PESSOAS.CONTATOS;')
    return jsonify(nomes)


def consultar_pessoas_contatos2():
    SQL_STATEMENT = 'SELECT P.NOME, P.CPF, C.TELEFONE, C.EMAIL '\
        'FROM PYTHON_CRUD_PESSOAS.PESSOAS AS P '\
        'INNER JOIN PYTHON_CRUD_PESSOAS.CONTATOS AS C ON C.ID_PESSOAS = P.ID;'
    nomes = _select_sql(SQL_STATEMENT)
    return jsonify(nomes)
