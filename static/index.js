window.onload = function togglePopup(){
    link = window.location.href;
    if(link != 'http://127.0.0.1:3000/' && link != 'http://127.0.0.1:3000/usuarios'){
    const overlay = document.getElementById('overlay');
    overlay.classList.toggle('show');
    }
    else{
            return 0;
        }
}

function closePopup(){
    const overlay = document.getElementById('overlay');
    overlay.classList.remove('show');
}

function validateForm(event) {
    var submitButton = event.submitter;
        var inputs = document.querySelectorAll('.info input');
            for (var i = 0; i < inputs.length; i++) {
                if (inputs[i].value.trim() === '') {
                   document.getElementById('warningMessage').style.display = 'block';
                   return false;
                    }
                }
            return true;
            }

function goBack() {
   window.history.back();
}

function toggleLogin(){
    const overlay = document.getElementById('login');
    overlay.classList.toggle('show');
}

function showUsers(){
    fetch('/usuarios')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
}