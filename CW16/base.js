// 1
// Write a program that takes an input from the user and displays its type as alert.
let data = document.getElementById("inputValue").value;

if (!isNaN(data) && value.trim() !== "") {
    alert("number");
} else {
    alert("string");
}

// 2
/* Write a program that gets the user's age. If the received age was between 0
and 10, the word child, if the age was between 11 and 18, it was a teenager, if
the age was between 19 and 30, it was a young person, and if the age was
more than 30, an adult should be printed on the console. */
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

console.log(message)

// 3
/*Write a program that receives the username from the user, stores it in a cookie,
and then retrieves the username from the cookie and greets her. */
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
/* Write a program that displays the text in a DOM element when the user clicks
on a button */
// uploaded as 4.html

//5
/*  Write a program that allows the user to enter the site by entering a username
and password. If the user ticks the remember me option, his username will be
saved using a cookie so that it will be automatically entered in future visits to
the site */
// uploaded as 5.html 

// 6
/* Store your first name, last name, age, country, city in your browser
localStorage. */
let firstName = prompt("First Name: ")
let lastName = prompt("Last Name: ")
let age = prompt("Age: ")
let country = prompt("Country: ")
let city  = prompt("City: ")

let profile = {
    "firstName": firstName,
    "lastName": lastName,
    "age": age,
    "country": country,
    "city": city
}

let strProfile = JSON.stringify(profile)
localStorage.setItem('profile', strProfile)
alert(localStorage.getItem('profile'))

// 7
/* Create a student object. The student object will have first name, last name,
age, skills, country, enrolled keys and values for the keys. Store the student
object in your browser localStorage. */


