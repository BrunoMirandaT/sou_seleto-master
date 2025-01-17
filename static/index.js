window.onload = function togglePopup(){
    link = window.location.href;
    mode = document.getElementById("overlay").getAttribute("value")
    if(mode == 1){
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
    overlay.value = '0'
}

function validateForm(event) {
    nvl = document.getElementById("nvl").innerText
                console.log(nvl)
                document.getElementById("copy").setAttribute('value',nvl)
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

document.addEventListener("click", toggleDrop);

function toggleDrop(event) {
    var dropdown = document.getElementById("drop");
    
if (event.target.classList.contains('nvl')){
    dropdown.style.visibility = "visible"
} else {
  dropdown.style.visibility = "hidden" 
}
}

function nvlAcesso(button){
    option = document.getElementById(button).innerHTML
    console.log(option)
    document.getElementById('nvl').innerHTML = option + "<img src='/static/25243.png' id='caretIcon'>"
}