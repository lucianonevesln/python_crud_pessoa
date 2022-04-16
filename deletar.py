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


def deletar_pessoas2(cpf):
    if cpf:
         conn = mysql.connect()
         cursor = conn.cursor()
         cursor.execute(
             f'delete from python_crud_pessoas.pessoas where cpf = "{cpf}";'
             )
         conn.commit()
         cursor.close()
         conn.close()
         return render_template('pessoas_deletar.html')


def deletar_contatos2(cpf):
    if cpf:
         conn = mysql.connect()
         cursor = conn.cursor()
         cursor.execute(
             f'delete c from python_crud_pessoas.pessoas as p inner join python_crud_pessoas.contatos as c on c.id_pessoas = p.id where cpf = "{cpf}";'
             )
         conn.commit()
         cursor.close()
         conn.close()
         return render_template('contatos_deletar.html')