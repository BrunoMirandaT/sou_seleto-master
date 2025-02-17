from flask import Flask, render_template, request, flash, redirect, url_for
import random, string
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore

from google.cloud.firestore_v1 import FieldFilter


def lenght(list):
    size = len(list)
    return size

app = Flask(__name__, template_folder = 'pages')
app.jinja_env.filters.update(lenght = lenght)
app_options = {'projectId': 'souseleto-33d19'}
default_app = firebase_admin.initialize_app(options=app_options)

db = firestore.client()

@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        searchbar = request.form.get('searchbar').upper()
    else:
        searchbar = ""
    
    info = db.collection('Alunos').where(filter=FieldFilter('CadAtv', '==', True))
    alunos_docs = info.stream()

    val1 = []
    val2 = []
    val3 = []

    for aluno in alunos_docs:
        aluno_data = aluno.to_dict()
        aluno_data['id'] = aluno.id  # Inclui o ID do documento no aluno
        val1.append(aluno_data["NomeAluno"])
        val2.append(aluno_data["DataNasc"])
        val3.append(aluno_data["id"])
        
    val1 = list(map(str.upper,val1))
        
    
    result = [v for v in val1 if searchbar in v]

    print(searchbar)

    final = []

    for x in range(len(result)) :
        final.append(result[x])
        final.append(val2[x])
        final.append(val3[x])
       

    return render_template('index.html',  alunos=final, mode='CADASTROS ATIVOS', popup=0, aux="REMOVER", infos=0)

@app.route('/cadastros/inativos', methods=['GET', 'POST'])
def cadastros_inativos():
    try:
        if request.method == 'POST':
            searchbar = request.form.get('searchbar')
            alunos_ref = db.collection('Alunos').where(filter=FieldFilter('CadAtv', '==', False)).where(filter=FieldFilter('NomeAluno', '==', searchbar))
            
        else:
            alunos_ref = db.collection('Alunos').where(filter=FieldFilter('CadAtv', '==', False))
            print("oi")
        alunos_docs = alunos_ref.stream()

    

        alunos = []
        i = 1
        for aluno in alunos_docs:
            aluno_data = aluno.to_dict()
            aluno_data['id'] = aluno.id  # Inclui o ID do documento no aluno
            alunos.count(id)
            alunos.append(aluno_data.get('NomeAluno'))
            alunos.append(aluno_data.get('DataNasc'))
            alunos.append(aluno_data.get('id'))
    except:
        print("dead")

    return render_template('index.html', alunos=alunos, mode='CADASTROS INATIVOS', aux='RESTAURAR', infos=0)
@app.route("/cadastro/<cadastro>", methods=['GET', 'POST'])
def get_cad(cadastro):
    docRef = db.collection('Alunos').document(cadastro)
    idAluno = docRef.id
    print(idAluno)

    alunos_ref = db.collection('Alunos')

    alunos_docs = alunos_ref.stream()

    info = []
    for alunos in alunos_docs:

        aluno_data = alunos.to_dict()
        aluno_data['id'] = alunos.id  # Inclui o ID do documento no aluno
        if aluno_data['id'] == cadastro:

            info.append(aluno_data.get('NomeAluno'))
            info.append(aluno_data.get('CpfAluno'))
            info.append(aluno_data.get('DataNasc'))
            info.append(aluno_data.get('NomeResp'))
            info.append(aluno_data.get('CpfResp'))
            info.append(aluno_data.get('RgResp'))
            info.append(aluno_data.get('NomeMae'))
            info.append(aluno_data.get('NomePai'))
            info.append(aluno_data.get('DataEnt'))
            info.append(aluno_data.get('Sangue'))
            info.append(aluno_data.get('CellResp'))
            info.append(aluno_data.get('id'))
            print(info)

    return render_template('index.html', infos=info, popup=1)

@app.route("/usuarios", methods=['GET', 'POST'])
def list_users():
    if request.method == 'POST':
       searchbar = request.form.get('searchbar').upper()
        
        
    else:
        searchbar = ""

    info = db.collection('Usuarios').where(filter=FieldFilter('userAtv', '==', True))
    user_docs = info.stream()

    val1 = []
    val2 = []
    val3 = []

    for user in user_docs:
        user_data = user.to_dict()
        user_data['id'] = user.id  # Inclui o ID do documento no aluno
        val1.append(user_data["NomeUser"])
        val2.append(user_data["DataNasc"])
        val3.append(user_data["id"])
        
    val1 = list(map(str.upper,val1))
        
    
    result = [v for v in val1 if searchbar in v]

    print(searchbar)

    final = []

    for x in range(len(result)) :
        final.append(result[x])
        final.append(val2[x])
        final.append(val3[x])
       

    return render_template('users.html', users=final) # Renderiza página de lista de usuários,
                                                                        # passando resultado de pesquisa sql para exibição no html

@app.route("/cadastros/novo", methods=['GET', 'POST'])
def new_cad():
    date = datetime.now()
    if request.method == 'POST':
        info = {"CadAtv": True, "NomeAluno": request.form['info0'], "CpfAluno": request.form['info1'],"DataNasc": request.form['info2'],
                "NomeResp": request.form['info3'],"CpfResp": request.form['info4'],"RgResp": request.form['info5'],
                "NomeMae": request.form['info6'], "NomePai": request.form['info7'], "DataEnt": request.form['info8'],
                "Sangue": request.form['info9'], "CellResp": request.form['info10'],"TelResp": request.form['info10']}
        
        document = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=20))

        db.collection('Alunos').document(document).set(info)

        img = request.files.get('foto_cad', '')

        


        return redirect(url_for('main_page')) # Retorna para rota main_page

    return render_template('new.html', d = date.strftime("%Y-%m-%d")) # Renderiza página de cadastro

@app.route("/new", methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        info = {"userAtv": True, "NomeUser": request.form['info0'], "Cpf": request.form['info1'],"DataNasc": request.form['info2'],
                "Nvl": request.form['copy']}

        db.collection('Usuarios').document("teste").set(info)

        return redirect(url_for('list_users'))

    return render_template('new_user.html')

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    error = ''
    if request.method == 'POST':
        if not request.form['cpf_User'] or not request.form['password_User']:
            error="CPF ou Senha invalidos!"
        else:
            docRef = db.collection('Usuarios').where(filter=FieldFilter('Cpf', '==', request.form['cpf_User']))
            print(docRef)

            user_docs = docRef.stream()

            info = []
            for users in user_docs:

                user_data = users.to_dict()
                if user_data.get('password') == request.form['password_User'] and user_data.get('Cpf') == request.form['cpf_User']:
                    return redirect(url_for('main_page'))
                else:
                    error="CPF ou Senha invalidos!"

           

    return render_template('login.html', error=error)


@app.route("/update/<cad>", methods = ['POST'])
def update_cad(cad):
    if request.method == 'POST':
        info = {"CadAtv": True, "NomeAluno": request.form['nome'], "CpfAluno": request.form['cpf'],"DataNasc": request.form['nasc'],
                "NomeResp": request.form['resp'],"CpfResp": request.form['cpf2'],"RgResp": request.form['rg'],
                "NomeMae": request.form['mae'], "NomePai": request.form['pai'],
                "Sangue": request.form['tiposangue'], "CellResp": request.form['celular'],"TelResp": request.form['telefone']}

        aluno = db.collection('Alunos').document(cad)
        aluno.update(info)
        print(cad)

        return redirect(url_for('main_page')) # Retorna para rota main_page

    return render_template('index.html') # Renderiza página de cadastro

@app.route("/update/<user>", methods = ['GET','POST'])
def update_user(user):
    if request.method == 'POST':
        cursor = db.cursor()
        add = 'update usuarios set nomeUsuario = %s, cpfUsuario = %s, nascimentoUsuario = %s, celularUsuario = %s, nvlAcesso = %s where idCadastro = %s'
        info = request.form['nome'], request.form['cpf'], request.form['nasc'], request.form['celular'], request.form['nivel'], user
        cursor.execute(add, info)
        db.commit()

        return redirect(url_for('main_page'))

    return render_template('index.html')

@app.route("/delete/cadastros/<type>/<id>")
def delete_cad(id, type):
    if type == "CADASTROS ATIVOS":
        info = {"CadAtv": False}
        aluno = db.collection('Alunos').document(id)
        aluno.update(info)
        return redirect(url_for('main_page'))
    else:
        info = {"CadAtv": True}
        aluno = db.collection('Alunos').document(id)
        aluno.update(info)
        return redirect(url_for('cadastros_inativos'))

@app.route("/delete/usuarios/<id>")
def delete_user(id):
    db.collection('Usuarios').document(id).delete()

    return redirect(url_for('list_users')) # Retorna para rota list_users

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(port=3000, debug=True)
