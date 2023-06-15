const getCookie = (name) => {
    return document.cookie.split(';').reduce((prev, c) => {
        let arr = c.split('=');
        return (arr[0].trim() === name) ? arr[1] : prev;
    }, undefined);
};



function handleErrors(response) {
    if (response.ok) {
        return response.json();
    } else if (response.status === 404) {
        throw new Error('Страница не найдена');
    } else if (response.status === 500) {
        throw new Error('Внутренняя ошибка сервера');
    } else {
        throw new Error('Некорректный ответ сервера');
    }
}



