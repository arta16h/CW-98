// 1
let data = prompt('Anything...')
alert(data)

// 2
let age = prompt('How old are you?', 20)
if (0 <= Number(age) <= 10) {
        message = 'Child'
    } else if (11< Number(age)< 18) {
        message = 'Teenager'
    } else if (19< Number(age)< 30) {
        message = 'Young Person'
    } else {
        message = 'Adult'
    }

// 3
function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    let expires = "expires=" +d.toUTCString();
    document.cookie = cname + "=" + cvalue +";" + expires + ";path=/";
}

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i < ca.length; i++){
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

let username = prompt('Username: ')
setCookie('username', username)
alert(getCookie(username))

//4
