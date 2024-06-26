from flask import Flask, render_template, request, flash, redirect, url_for
import secrets, json, re
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from mysql.connector import connect
from sqlalchemy.orm import relationship

app = Flask(__name__, template_folder = 'pages')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teste.db'

db = connect(
      user = 'root',
      password = '',
      host = '127.0.0.1',
      database = 'SouSeleto')

secret_key = secrets.token_hex(32)

app.config['SECRET_KEY'] = secret_key

#app.app_context().push()
#db = SQLAlchemy(app)

"""class Aluno(db.Model):
    id = db.Column('studentId',db.Integer, primary_key=True)
    nome = db.Column(db.String(200))
    info1 = db.Column(db.String(100))
    info2 = db.Column(db.String(100))
    info3 = db.Column(db.String(20))

    def __init__(self,nome_aux,info1_aux,info2_aux,info3_aux):
        self.nome = nome_aux
        self.info1 = info1_aux
        self.info2 = info2_aux
        self.info3 = info3_aux"""

@app.route("/")
def main_page():
    cursor = db.cursor()
    search = 'select idCadastro, nomeCadastro, nascimentoCadastro from cadastros'
    cursor.execute(search)
    results = cursor.fetchall()

    id = results[0]
    aux = id[0]
    print(aux)

    return render_template('index.html', info=results)

def show_cad():
    cursor = db.cursor()
    search = 'select * from cadastros'
    cursor.execute(search)
    results = cursor.fetchall()

    return render_template('index.html', cad= 1)


@app.route("/cadastro", methods=['GET', 'POST'])
def get_cad():

    print(help)
    print("bodia")
    test = "bodia"
    print(test)
    return render_template('index.html', cad=test)

@app.route("/new", methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['nome'] or not request.form['info1'] or not request.form['info2'] or not request.form['info3']:
            flash("Preencha todos os campos", "Erro")
        else:
            cursor = db.cursor()
            add = 'insert into cadastros (nomeCadastro, cpfCadastro, nascimentoCadastro, nomeResponsavel, cpfResponsavel, rgResponsavel, nomeMae, nomePai, dataEntrada, tipoSanguineo) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            info = request.form['nome'], request.form['info1'], request.form['info2'], request.form['info3'], request.form['info4'], request.form['info5'], request.form['info6'], request.form['info7'], request.form['info8'], request.form['info9']
            cursor.execute(add, info)
            db.commit()

            return redirect(url_for('main_page'))

    return render_template('new.html')

@app.route("/update/<int:id>", methods = ['GET','POST'])
def update(id):
    aluno = Aluno.query.get(id)
    if request.method == 'POST':
        if not request.form['nome'] or not request.form['cidade'] or not request.form['email'] or not request.form['pin']:
            flash("Preencha todos os campos", "Erro")
        else:
            aluno.nome = request.form['nome']
            aluno.cidade = request.form['cidade']
            aluno.email = request.form['email']
            aluno.pin = request.form['pin']
            db.session.add(aluno)
            db.session.commit()
            return redirect(url_for('show_all'))

    return render_template('update.html', aluno=aluno)

@app.route("/delete/<int:id>")
def delete(id):
    aluno = Aluno.query.get(id)
    db.session.delete(aluno)
    db.session.commit()
    return redirect(url_for('main_page'))


if __name__ == '__main__':

    app.run(port=3000, debug=True)
