from flask import Flask, render_template, request, flash, redirect, url_for
import random, string
from mysql.connector import connect

app = Flask(__name__, template_folder = 'pages')

db = connect(
      user = 'root',
      password = '',
      host = '127.0.0.1',
      database = 'SouSeleto')


@app.route("/")
def main_page():
    cursor = db.cursor()
    search = 'select idCadastro, nomeCadastro, nascimentoCadastro from cadastros limit 13'
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
    link = request.base_url
    cursor = db.cursor()
    if(link == 'http://127.0.0.1:3000/usuarios'):
        search = 'select * from usuarios where idUsuario = %s'
        cursor.execute(search, tuple(cadastro))
    else:
        search = 'select * from cadastros where idCadastro = %s'
        cursor.execute(search, tuple(cadastro))
        results = cursor.fetchall()

    return render_template('index.html', cad=results)

@app.route("/usuarios", methods=['GET', 'POST'])
def get_users():
    cursor = db.cursor()
    search = 'select * from usuarios where idUsuario'
    cursor.execute(search)
    results = cursor.fetchall()

    return render_template('index.html', info=results)

@app.route("/new", methods=['GET', 'POST'])
def new_cad():
    if request.method == 'POST':
        cursor = db.cursor()
        add = 'insert into cadastros (nomeCadastro, cpfCadastro, nascimentoCadastro, nomeResponsavel, cpfResponsavel, rgResponsavel, nomeMae, nomePai, dataEntrada, tipoSanguineo, celular, telefone) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        info = request.form['info0'], request.form['info1'], request.form['info2'], request.form['info3'], request.form['info4'], request.form['info5'], request.form['info6'], request.form['info7'], request.form['info8'], request.form['info9'], request.form['info10'], request.form['info10']
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

            return redirect(url_for('login_user'))

    return render_template('index.html')


@app.route("/update/<cad>", methods = ['GET','POST'])
def update_cad(cad):
    if request.method == 'POST':
        cursor = db.cursor()
        add = 'update cadastros set nomeCadastro = %s, cpfCadastro = %s, nascimentoCadastro = %s, nomeMae = %s, nomePai = %s, nomeResponsavel = %s, cpfResponsavel = %s, rgResponsavel = %s, tipoSanguineo = %s, telefone = %s, celular = %s where idCadastro = %s'
        info = request.form['nome'], request.form['cpf'], request.form['nasc'], request.form['mae'], request.form['pai'], request.form['resp'], request.form['cpf2'], request.form['rg'], request.form['tiposangue'], request.form['telefone'], request.form['celular'], cad
        cursor.execute(add, info)
        db.commit()

        return redirect(url_for('main_page'))

    return render_template('index.html')

@app.route("/delete/<id>")
def delete(id):
    cursor = db.cursor()
    remove = 'delete from cadastros where idCadastro = %s'
    cursor.execute(remove, tuple(id))
    db.commit()

    return redirect(url_for('main_page'))

if __name__ == '__main__':

    app.run(port=3000, debug=False)
