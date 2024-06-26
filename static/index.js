function togglePopup(){
    const overlay = document.getElementById('overlay');
    overlay.classList.toggle('show');
    fetch('/cadastro')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
}

function closePopup(){
    const overlay = document.getElementById('overlay');
    overlay.classList.remove('show');
}

 function validateForm(event) {
            var submitButton = event.submitter;

            // Verifica se o botão clicado foi o de Submit
            if (submitButton && submitButton.value === 'Submit') {
                // Verifica se todos os campos estão preenchidos
                var inputs = document.querySelectorAll('.info input');
                for (var i = 0; i < inputs.length; i++) {
                    if (inputs[i].value.trim() === '') {
                        // Mostra a mensagem de aviso
                        document.getElementById('warningMessage').style.display = 'block';
                        return false; // Impede o envio do formulário
                    }
                }
            }

            return true; // Permite o envio do formulário se todos os campos estiverem preenchidos
        }

        function goBack() {
            // Função para voltar (simulada)

            // Exemplo de redirecionamento
            window.history.back();
        }

