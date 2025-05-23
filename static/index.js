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
   /* const overlay = document.getElementById('overlay');
    overlay.classList.remove('show');
    overlay.value = '0'*/
    history.back()
}

function setMode(){
  const overlay = document.getElementById('overlay');
    overlay.classList.toggle('show');
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

var pageButton = document.getElementsByClassName("pageButton");
    for(let item of pageButton){
      item.addEventListener("click", pageNav);
    }
var inputPage = document.getElementById('page')

inputPage.addEventListener("keydown", pageNav)

function pageNav(event){
  curPage = document.getElementById("page")
  const keypress = event.key
  const id = event.srcElement.id;

  if(keypress == "Enter"){
    curPage.value++
    return "ok";
  }else if(event.srcElement.classList.contains("pageButton")){
    if(id == "next"){
      curPage.value++
    }else{
      if(curPage.value <= 1 ){
        curPage.value = 1
      }else if(id =="back"){
        curPage.value--
      }
    } 
  }
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
  let activeDiv = event.target.querySelector(".drop");
  console.log(event.target.classList)
  opacity = 1
  position = "translateY(0px)"
  let arrow = document.querySelector('#caretIcon').style.transform
  console.log(arrow)
  let rotation = arrow == 'rotate(0deg)' ? 'rotate(180deg)' : 'rotate(0deg)';

  if(event.target.classList.contains('userBox') || event.target.classList.contains('userButton')|| event.target.classList.contains('fa-user') || event.target.classList.contains('dropdownNvl') ||event.target.classList.contains('nvlAcesso')){
    activeDiv.classList.toggle('hidden')
    if(activeDiv.style.opacity==1){
      opacity = 0
      position = "translateY(-20px)"
    }
    activeDiv.style.opacity= opacity
    activeDiv.style.transform = position
    event.target.querySelector('#caretIcon').style.transform = rotation

  }else{
    activeDiv = document.querySelectorAll('.drop')
    console.log(activeDiv)
    event.target.querySelector('.drop').style.opacity= 0
    for(i=0; i < 2; i++){
      activeDiv[i].classList.add('hidden')
    } 
    event.target.querySelector('#caretIcon').style.transform = rotation
  }
  
}

function nvlAcesso(button){
    option = document.getElementById(button).innerHTML
    console.log(option)
    document.getElementById('nvl').innerHTML = option + "<img src='/static/25243.png' id='caretIcon'>"
}

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