const registerBtn = document.getElementById('register-btn');
const EmailInput = document.getElementById('email_id');
const firstNameInput = document.getElementById('first_name_id');
const lastNameInput = document.getElementById('last_name_id');
const birthDateInput = document.getElementById('birthdate_id');
const passwordInput = document.getElementById('pass_id');
const repeatPasswordInput = document.getElementById('repeat_pass_id');

const emailNumberErrMsg = document.getElementById('phone-number-err-id');
const firstNameErrMsg = document.getElementById('first-name-err-id');
const lastNameErrMsg = document.getElementById('last-name-err-id');
const birthDateErrMsg = document.getElementById('birthdate-err-id');
const passwordErrMsg = document.getElementById('password-err-id');
const repeatPasswordErrMsg = document.getElementById('repeat-password-err-id');

registerBtn.onclick = () => {
    const requestData = {
        email: EmailInput.value,
        first_name: firstNameInput.value,
        last_name: lastNameInput.value,
        date_of_birth: birthDateInput.value,
        password: passwordInput.value,
        repeatPassword: repeatPasswordInput.value
    }



    fetch(registerUrl, {
        method: 'POST',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify(requestData),
    })
    .then(handleErrors)
    .then(responseJSON => {
        console.log(responseJSON['detail'])
        if (responseJSON['detail']['email']) {
            emailNumberErrMsg.style.display = 'block';
        } else if (responseJSON['detail']['first_name']) {
            firstNameErrMsg.style.display = 'block';
        } else if (responseJSON['detail']['last_name']) {
            lastNameErrMsg.style.display = 'block';
        } else if (responseJSON['detail']['date_of_birth']) {
            birthDateErrMsg.style.display = 'block';
        } else if (responseJSON['detail']['password']) {
            passwordErrMsg.style.display = 'block';
        } else if (responseJSON['detail']['repeatPassword']) {
            repeatPasswordErrMsg.style.display = 'block';
        }

    })
    .catch(error => console.log(error));
}

