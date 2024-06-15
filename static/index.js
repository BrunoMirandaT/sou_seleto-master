function togglePopup(){
    const overlay = document.getElementById('overlay');
    overlay.classList.toggle('show');
}

function closePopup(){
    const overlay = document.getElementById('overlay');
    overlay.classList.remove('show');
}