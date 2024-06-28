from flask import Flask, render_template, request, flash, redirect, url_for
import secrets, json, re, random, string
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

def random_senha():
    random_senha = ''.join(random.choice(string.ascii_letters) for i in range(6))

@app.route("/")
def main_page():
    cursor = db.cursor()
    search = 'select idCadastro, nomeCadastro, nascimentoCadastro from cadastros limit 15'
    cursor.execute(search)
    results = cursor.fetchall()
    print("yu")

    return render_template('index.html', info=results, cad='o')

def show_cad():
    cursor = db.cursor()
    search = 'select * from cadastros'
    cursor.execute(search)
    results = cursor.fetchall()

    return render_template('index.html', blob='')

@app.route("/<cadastro>", methods=['GET', 'POST'])
def get_cad(cadastro):
    cursor = db.cursor()
    search = 'select * from cadastros where idCadastro = %s'
    cursor.execute(search, tuple(cadastro))
    results = cursor.fetchall()

    return render_template('index.html', cad=results)

@app.route("/usuarios", methods=['GET', 'POST'])
def get_users():
    cursor = db.cursor()
    search = 'select idUsuario, nomeUsuario, nascimentoUsuario from usuarios'
    cursor.execute(search)
    results = cursor.fetchall()
    print("oi")
    print(results)

    return render_template('index.html', info=results)

@app.route("/new", methods=['GET', 'POST'])
def new_cad():
    if request.method == 'POST':
        cursor = db.cursor()
        add = 'insert into cadastros (nomeCadastro, cpfCadastro, nascimentoCadastro, nomeResponsavel, cpfResponsavel, rgResponsavel, nomeMae, nomePai, dataEntrada, tipoSanguineo) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        info = request.form['nome'], request.form['info1'], request.form['info2'], request.form['info3'], request.form['info4'], request.form['info5'], request.form['info6'], request.form['info7'], request.form['info8'], request.form['info9']
        cursor.execute(add, info)
        db.commit()

        return redirect(url_for('main_page'))

    return render_template('new.html')

@app.route("/new", methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        if not request.form['nome'] or not request.form['nasc'] or not request.form['cpf'] or not request.form['celular'] or not request.form['nvlAcesso']:
            flash("Preencha todos os campos", "Erro")
        else:
            cursor = db.cursor()
            add = 'insert into usuarios (nomeUsuario, nascimentoUsuario, cpfUsuario, hashSenha, celularUsuario, nvlAcesso) values (%s, %s, %s, %s, %s, %s)'
            info = request.form['nome'], request.form['nasc'], request.form['cpf'], random_senha(), request.form['celular'], request.form['nvlAcesso']
            cursor.execute(add, info)
            db.commit()

            return redirect(url_for('main_page'))

    return render_template('new_user.html')

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        if not request.form['cpf_User'] or not request.form['password_User']:
            flash("Preencha todos os campos", "Erro")
        else:
            cursor = db.cursor()
            search = 'select cpfUsuario, hashSenha from usuarios where cpfUsuario = %s'
            info = request.form['cpfUser']
            cursor.execute(search, info)
            results = cursor.fetchall()
            print('oi')
            print(results)

            return redirect(url_for('login_user'))

    return render_template('index.html')


@app.route("/update/<cad>", methods = ['GET','POST'])
def update_cad(cad):
    print("yahu")
    if request.method == 'POST':
        print("guhh")

        cursor = db.cursor()
        add = 'update cadastros set nomeCadastro = %s, cpfCadastro = %s, nascimentoCadastro = %s, nomeMae = %s, nomePai = %s, nomeResponsavel = %s, cpfResponsavel = %s, rgResponsavel = %s, tipoSanguineo = %s where idCadastro = %s'
        info = request.form['nome'], request.form['cpf'], request.form['nasc'], request.form['mae'], request.form['pai'], request.form['resp'], request.form['cpf2'], request.form['rg'], request.form['tiposangue'], cad
        cursor.execute(add, info)
        db.commit()
        print("brabo")

        return redirect(url_for('main_page'))

    return render_template('index.html')

@app.route("/delete/<int:id>")
def delete(id):
    aluno = Aluno.query.get(id)
    db.session.delete(aluno)
    db.session.commit()
    return redirect(url_for('main_page'))


if __name__ == '__main__':

    app.run(port=3000, debug=True)
