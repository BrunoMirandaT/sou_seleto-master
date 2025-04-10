window.onload = function togglePopup(){
    link = window.location.href;
    mode = document.getElementById("overlay").getAttribute("value")
    userRole = document.getElementById("userRole").innerHTML
    if(mode == 1){
      if(userRole == "False"){
        document.getElementById("fieldset").disabled = true;
      }

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
    console.log(dropdown.style.visibility)
    
if (event.target.classList.contains('nvl')){
    if(dropdown.style.visibility == "visible"){
      dropdown.style.visibility = "hidden"
      document.getElementById('caretIcon').style.transform = "rotate(360deg)"
    }else{
      dropdown.style.visibility = "visible"
      document.getElementById('caretIcon').style.transform = "rotate(180deg)"
    }
} else {
  dropdown.style.visibility = "hidden"
  document.getElementById('caretIcon').style.transform = "rotate(360deg)"
}
}

function nvlAcesso(button){
    option = document.getElementById(button).innerHTML
    console.log(option)
    document.getElementById('nvl').innerHTML = option + "<img src='/static/25243.png' id='caretIcon'>"
}

const icon = document.getElementById('togglePassword');
let password = document.getElementById('password');

/* Event fired when <i> is clicked */
icon.addEventListener('click', function() {
  if(password.type === "password") {
    password.type = "text";
    icon.classList.add("fa-eye");
    icon.classList.remove("fa-eye-slash");
  }
  else {
    password.type = "password";
    icon.classList.add("fa-eye-slash");
    icon.classList.remove("fa-eye");
  }
});

function getImgData(file, preview, output) {
    const chooseFile = document.getElementById(file);
const imgPreview = document.getElementById(preview);
    const files = chooseFile.files[0];
    if (files) {
      const fileReader = new FileReader();
      fileReader.readAsDataURL(files);
      fileReader.addEventListener("load", function () {
        imgPreview.style.display = "block";
        imgPreview.src = this.result;
        document.getElementById(output).style.zIndex = 25
        invisible();
      });    
    }
  }

function visible(output, preview){
  document.getElementById(output).style.zIndex = 0
  document.getElementById(preview).style.filter = "brightness(90%)"
}

function invisible(output, preview){
  const imgPreview = document.getElementById(preview);
  if(imgPreview.src != ""){
    document.getElementById(output).style.zIndex = 25
  } 
  document.getElementById(preview).style.filter = "brightness(100%)"

}

function showDocs(){
  document.getElementById("cadastro").style.display = "none"
  document.getElementById("documents").style.display = "grid"
}

function hideDocs(){
  document.getElementById("cadastro").style.display = "flex"
  document.getElementById("documents").style.display = "none"
}

function userDrop(){
  mode = document.getElementById("userDrop").style.visibility
  if(mode == "hidden"){
    document.getElementById("userDrop").style.visibility = "visible"
  }else{
    document.getElementById("userDrop").style.visibility = "hidden"
  }
}