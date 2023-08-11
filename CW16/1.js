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
