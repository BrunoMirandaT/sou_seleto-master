from flask import Flask, render_template, request, flash, redirect, url_for, session
import random, string
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase

from google.cloud.firestore_v1 import FieldFilter

def lenght(list):
    size = len(list)
    return size

app = Flask(__name__, template_folder = 'pages')
app.jinja_env.filters.update(lenght = lenght)
app_options = {'projectId': 'souseleto-33d19'}
default_app = firebase_admin.initialize_app(options=app_options)

config = {
    "apiKey": "AIzaSyDMS7dH3iwxf5vTaz4Ir40iZ04r-mxgc0U",
    "authDomain": "souseleto-33d19.firebaseapp.com",
    "databaseURL": "",
    "storageBucket": "souseleto-33d19.firebasestorage.app"
}

firebase = pyrebase.initialize_app(config)

db = firestore.client()

def get_cadastros(input):
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
        

    result = [v for v in val1 if input in v]

    print(input)

    final = []

    for x in range(len(result)) :
        final.append(result[x])
        final.append(val2[x])
        final.append(val3[x])
        final.append(x)

    print(final)

    return final

def get_users(input):
    info = db.collection('Usuarios').where(filter=FieldFilter('userAtv', '==', True))
    user_docs = info.stream()

    val1 = []
    val2 = []
    val3 = []

    for user in user_docs:
        user_data = user.to_dict()
        user_data['id'] = user.id  # Inclui o ID do documento no aluno
        val1.append(user_data["NomeUser"])
        val2.append(user_data["Nvl"])
        val3.append(user_data["id"])
        
    val1 = list(map(str.upper,val1))
        
    
    result = [v for v in val1 if input in v]

    print(input)

    final = []

    for x in range(len(result)) :
        final.append(result[x])
        final.append(val2[x])
        final.append(val3[x])

    return final


@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        searchbar = request.form.get('searchbar')
    else:
        searchbar = ""
    
    final = get_cadastros(searchbar.upper())

    print(type(session["userInfo"]))
       
    return render_template('index.html',  alunos=final, mode='CADASTROS ATIVOS', popup=0, aux="REMOVER", infos=0, default = searchbar, user = session['userInfo'], test = session)

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

    return render_template('index.html', alunos=alunos, mode='CADASTROS INATIVOS', aux='RESTAURAR', infos=0, user = session['userInfo'])
@app.route("/<cadastro>", methods=['GET', 'POST'])
def get_cad(cadastro):
    if request.method == 'POST':
        searchbar = request.form.get('searchbar')
    else:
        searchbar = ""
    docRef = db.collection('Alunos').document(cadastro)
    idAluno = docRef.id
    print(idAluno)

    alunos_ref = db.collection('Alunos')

    alunos_docs = alunos_ref.stream()

    info = []
    for aluno in alunos_docs:

        aluno_data = aluno.to_dict()
        aluno_data['id'] = aluno.id  # Inclui o ID do documento no aluno
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

        lista_aluno = get_cadastros(searchbar.upper())
        print(searchbar)
    
    return render_template('index.html', alunos=lista_aluno, infos=info, popup=1, aux="REMOVER", mode='CADASTROS ATIVOS', default=searchbar, user = session['userInfo'])

@app.route("/usuarios/<id>", methods=['GET', 'POST'])
def get_user(id):
    if request.method == 'POST':
        searchbar = request.form.get('searchbar')
    else:
        searchbar = ""
    docRef = db.collection('Usuarios').document(id)
    idUser = docRef.id
    print(idUser)

    users_ref = db.collection('Usuarios')

    users_docs = users_ref.stream()

    info = []
    for user in users_docs:

        user_data = user.to_dict()
        user_data['id'] = user.id  # Inclui o ID do documento no aluno
        if user_data['id'] == id:

            info.append(user_data.get('NomeUser'))
            info.append(user_data.get('Cpf'))
            data = (user_data.get('DataNasc'))
            info.append(datetime.strptime(data, '%d/%m/%Y').strftime('%Y-%m-%d'))
            info.append(user_data.get('UserEmail'))
            info.append(user_data.get('Nvl'))
            info.append(user_data.get('id'))

            print(info)

            lista_users = get_users(searchbar.upper())
            print(searchbar)
    
    return render_template('users.html', users=lista_users, infos=info, popup=1, aux="REMOVER", default=searchbar, user = session['userInfo'])

@app.route("/usuarios", methods=['GET', 'POST'])
def list_users():
    if request.method == 'POST':
       searchbar = request.form.get('searchbar')
        
    else:
        searchbar = ""

    final = get_users(searchbar.upper())

    return render_template('users.html', users=final, infos="", user = session['userInfo']) # Renderiza página de lista de usuários,
                                                                        # passando resultado de pesquisa sql para exibição no html

@app.route("/cadastros/novo", methods=['GET', 'POST'])
def new_cad():
    date = datetime.now()
    if request.method == 'POST':
        info = {"CadAtv": True, "NomeAluno": request.form['info0'], "CpfAluno": request.form['info1'],"DataNasc": datetime.strptime(request.form['info2'] , '%Y-%m-%d').strftime("%d/%m/%Y"),
                "NomeResp": request.form['info3'],"CpfResp": request.form['info4'],"RgResp": request.form['info5'],
                "NomeMae": request.form['info6'], "NomePai": request.form['info7'], "DataEnt": datetime.strptime(request.form['info8'] , '%Y-%m-%d').strftime("%d/%m/%Y"),
                "Sangue": request.form['info9'], "CellResp": request.form['info10'],"TelResp": request.form['info10']}
        
        document = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=20))

        db.collection('Alunos').document(document).set(info)

        img = request.files.get('foto_cad', '')

        


        return redirect(url_for('main_page')) # Retorna para rota main_page

    return render_template('new.html', d = date.strftime("%Y-%m-%d"), user = session['userInfo']) # Renderiza página de cadastro

@app.route("/new", methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        info = {"userAtv": True, "NomeUser": request.form['info0'], "Cpf": request.form['info1'],"DataNasc": datetime.strptime(request.form['info2'] , '%Y-%m-%d').strftime("%d/%m/%Y"),
                "Nvl": request.form['copy']}
        
        document = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=20))

        db.collection('Usuarios').document(document).set(info)

        return redirect(url_for('list_users'))

    return render_template('new_user.html', user = session['userInfo'])

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    error = ''
    if request.method == 'POST':
        email = request.form['cpfUser']
        senha = request.form['passwordUser']
        if not email or not senha:
            error="CPF ou Senha invalidos!"
        else:
            try:
                sign_user = firebase.auth().sign_in_with_email_and_password(email, senha)
                
                sign_user = firebase.auth().refresh(sign_user['refreshToken'])
                
                session['user'] = sign_user['idToken']
                
                docRef = db.collection('Usuarios').where(filter=FieldFilter('UserEmail', '==', email))
    
                users_docs = docRef.stream()

                for user in users_docs:

                    user_data = user.to_dict()
                    user_data['id'] = user.id  # Inclui o ID do documento no aluno
                    print(user_data)

                    userInfo = [user_data.get('NomeUser'), user_data.get('Nvl'), user_data.get('UserEmail'), user_data.get('Cpf'), user_data.get('DataNasc'), user_data['id']]

                    session['userInfo'] = userInfo
                    '''
                    session['nameUser'] = (user_data.get('NomeUser'))
                    session['userRole'] = user_data.get('Nvl')
                    session['emailUser'] = user_data.get('UserEmail')
                    session['cpfUser'] = user_data.get('Cpf')
                    session['nascUser'] = user_data.get('DataNasc')
                    print("yay")'''

                    print(userInfo)

                    def is_master(session):
                        return session['userInfo'][1] == "Master"
    
                    session['func'] = is_master(session)
                
                return redirect(url_for('main_page'))
            except:
                error="CPF ou Senha invalidos!"
                print("no works")

    

    return render_template('login.html', error=error)


@app.route('/auth', methods=['GET', 'POST'])
def auth(email):
    docRef = db.collection('Usuarios').document(id)
    idUser = docRef.id
    print(idUser)

    users_ref = db.collection('Usuarios')

    users_docs = users_ref.stream()

    info = []
    for user in users_docs:

        user_data = user.to_dict()
        user_data['id'] = user.id  # Inclui o ID do documento no aluno
        if user_data['id'] == id:

            info.append(user_data.get('NomeUser'))
            info.append(user_data.get('Cpf'))
            info.append(user_data.get('DataNasc'))
            info.append(user_data.get('Nvl'))
            


@app.route("/update/<cad>", methods = ['POST'])
def update_cad(cad):
    if request.method == 'POST':
        info = {"CadAtv": True, "NomeAluno": request.form['nome'], "CpfAluno": request.form['cpf'],"DataNasc": datetime.strptime(request.form['nasc'] , '%Y-%m-%d').strftime("%d/%m/%Y"),
                "NomeResp": request.form['resp'],"CpfResp": request.form['cpf2'],"RgResp": request.form['rg'],
                "NomeMae": request.form['mae'], "NomePai": request.form['pai'],
                "Sangue": request.form['tiposangue'], "CellResp": request.form['celular'],"TelResp": request.form['telefone']}

        aluno = db.collection('Alunos').document(cad)
        aluno.update(info)
        print(cad)

        return redirect(url_for('main_page')) # Retorna para rota main_page

    return render_template('index.html', user = session['userInfo']) # Renderiza página de cadastro

@app.route("/update_user/<user>", methods = ['GET','POST'])
def update_user(user):
    if request.method == 'POST':
        info = {"userAtv": True, "NomeUser": request.form['nome'], "Cpf": request.form['cpf'],"DataNasc": datetime.strptime(request.form['nasc'] , '%Y-%m-%d').strftime("%d/%m/%Y"),
                "Nvl": request.form['copy'], "UserEmail": request.form['email']}

        usuario = db.collection('Usuarios').document(user)
        usuario.update(info)

        return redirect(url_for('list_users'))

    return render_template('users.html', user = session['userInfo'])

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
