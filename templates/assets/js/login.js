const loginBtn = document.getElementById('login-btn');
const emailValue = document.getElementById('form3Example1c');
const passwordValue = document.getElementById('form3Example4c');
const passErrMsg = document.getElementById('pass-err-msg-id');
const userNotFoundErrMsg = document.getElementById('user-not-found-msg-id');

loginBtn.onclick = () => {
    const requestData = {
        email: emailValue.value,
        password: passwordValue.value,
    };


    fetch(loginUrl, {
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
    console.log(responseJSON)

    })
        .catch(error => {
        console.log('Error:', error);
    });

};
