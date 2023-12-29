password = document.getElementById('password');
confirmpassword = document.getElementById('confirmpassword');
regForm = document.getElementById('regform');
btn = document.querySelector('.submit-btn');

const Status = (boolean) => {

    return boolean
};

const appendErrorMessage = (message, color) => {
    const error = document.createElement('div');
    error.innerHTML = message;
    error.classList.add('message', `${color}`);
    regForm.append(error);
};

const clearErrorMessages = () => {
    regForm.innerHTML = '';
    errorAppended = 0;
};

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
var s1, s2, s3, s4, s5, s6;
// Array of uppercase alphabet letters
const ucAlphabets = Array.from({ length: 26 }, (_, i) => String.fromCharCode('A'.charCodeAt(0) + i));

// Array of lowercase alphabet letters
const lcAlphabets = Array.from({ length: 26 }, (_, i) => String.fromCharCode('a'.charCodeAt(0) + i));

// Array of special characters
const specialCharacters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', ';', ':', ',', '.', '<', '>', '?', '/', '|', '\\'];
const emailchk = ['@', '.'];
btn = document.querySelector('.submit-btn');
let username = document.querySelector('#username');
let firstname = document.querySelector('#firstname');
let lastname = document.querySelector('#lastname');
let email = document.querySelector('#email');
const btnblocker = () => {
    btn.type = 'button';
    if (!btn.classList.contains('blocked_btn')) {
        btn.classList.add('blocked_btn');
    }
    document.addEventListener('click', function (event) {
        if (event.target == btn || btn.contains(event.target)) {
            btn.classList.add('blocked_btn-animation');
            setTimeout(function () {
                btn.classList.remove('blocked_btn-animation');
            }, 300)
        }
    })
}
const btnunblocker = () => {
    btn.type = 'submit';
    if (btn.classList.contains('blocked_btn')) {
        btn.classList.remove('blocked_btn');
    }


}
const hasnumber = (str) => {
    return numbers.some(num => str.includes(num))
}
const hasuppercase = (str) => {
    return ucAlphabets.some(uc => str.includes(uc))
}
const haslowercase = (str) => {
    return lcAlphabets.some(lc => str.includes(lc))
}
const hasSpecialCharacter = (str) => {
    return specialCharacters.some(char => str.includes(char))
}
const isEmail = (str) => {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(str);
};


const usernameVerifier = (errorAppended) => {

        const usernameValue = username.value;
        let unameinputvalue = document.querySelector('#forusernamecheckinginput')
        if (hasSpecialCharacter(usernameValue) || usernameValue.length < 6 || usernameValue.length > 20) {
            if (errorAppended === 0 && usernameValue.length < 6) {
                appendErrorMessage('Username must be at least 6 characters long', 'red');
                errorAppended = 1;
                var s1 = Status(false);



            } else if (errorAppended === 0 && hasSpecialCharacter(usernameValue)) {
                appendErrorMessage('Username must not contain special characters', 'red');
                errorAppended = 1;
                var s1 = Status(false);



            } else if (errorAppended === 0 && usernameValue.length > 20) {
                appendErrorMessage('Username must not exceed 20 characters', 'red');
                errorAppended = 1;
                var s1 = Status(false);



            }
            else if (errorAppended === 0 && unameinputvalue.value == '2') {
                errorAppended = 1;
                var s1 = Status(false);



            }
        } else if (!hasSpecialCharacter(usernameValue) && usernameValue.length >= 6 && usernameValue.length <= 20 && unameinputvalue.value == '1') {
            clearErrorMessages();
            errorAppended = 0;
            var s1 = Status(true);

        }

        return s1
};


var errorAppended = 0;

username.addEventListener('input', function () {
    for(i=1;i<11;i++){
        setTimeout(() => {
    clearErrorMessages();
    errorAppended = 0;
    s1 = usernameVerifier(errorAppended);    },100);}
});
const firstnameVerifier = (errorAppended, name) => {

    const nameValue = name.value;
    if (nameValue.length < 3 || nameValue.length > 20 || hasSpecialCharacter(nameValue) || hasnumber(nameValue)) {
        if (errorAppended === 0 && nameValue.length < 3) {
            appendErrorMessage('Name must be at least 3 characters long', 'red');
            errorAppended = 1;
            var s2 = Status(false);



        } else if (errorAppended === 0 && nameValue.length > 20) {
            appendErrorMessage('Name must not exceed 20 characters', 'red');
            var s2 = Status(false);

            errorAppended = 1;
        }
        else if (errorAppended === 0 && hasSpecialCharacter(nameValue)) {
            appendErrorMessage('Name must not contain special characters', 'red');
            var s2 = Status(false);

            errorAppended = 1;
        }
        else if (errorAppended === 0 && hasNumber(nameValue)) {
            appendErrorMessage('Name must not contain Number', 'red');

            var s2 = Status(false);
            errorAppended = 1;
        }
    } else if (nameValue.length >= 3 && nameValue.length <= 20 || !hasSpecialCharacter(nameValue) || !hasnumber(nameValue)) {
        clearErrorMessages();
        errorAppended = 0;
        var s2 = Status(true);

    }

    return s2;

}
const lastnameVerifier = (errorAppended, name) => {
    const nameValue = name.value;
    if (nameValue.length < 3 || nameValue.length > 20 || hasSpecialCharacter(nameValue) || hasnumber(nameValue)) {
        if (errorAppended === 0 && nameValue.length < 3) {
            appendErrorMessage('Name must be at least 3 characters long', 'red');
            var s3 = Status(false);
            errorAppended = 1;


        } else if (errorAppended === 0 && nameValue.length > 20) {
            appendErrorMessage('Name must not exceed 20 characters', 'red');

            var s3 = Status(false);
            errorAppended = 1;
        }
        else if (errorAppended === 0 && hasSpecialCharacter(nameValue)) {
            appendErrorMessage('Name must not contain special characters', 'red');

            var s3 = Status(false);
            errorAppended = 1;
        }
        else if (errorAppended === 0 && hasNumber(nameValue)) {
            appendErrorMessage('Name must not contain Number', 'red');

            var s3 = Status(false);
            errorAppended = 1;
        }
    } else if (nameValue.length >= 3 && nameValue.length <= 20 || !hasSpecialCharacter(nameValue) || !hasnumber(nameValue)) {
        clearErrorMessages();
        errorAppended = 0;
        var s3 = Status(true);

    }

    return s3;

}

firstname.addEventListener('input', function () {
    clearErrorMessages();
    errorAppended = 0;
    s2 = firstnameVerifier(errorAppended, firstname);
})
lastname.addEventListener('input', function () {
    clearErrorMessages();
    errorAppended = 0;
    s3 = lastnameVerifier(errorAppended, lastname);
})
emailVerifier = (errorAppended, email) => {
    const emailValue = email.value;
    let emailinputvalue = document.querySelector('#foremailcheckinginput')
    let emailValued = emailinputvalue.value
    if (!isEmail(emailValue) || emailValued == '2') {
        if (errorAppended === 0) {
            appendErrorMessage('Please enter a valid email address', 'red');
            var s4 = Status(false);

            errorAppended = 1;
        }
        else if (errorAppended === 0 && emailValued == '2') {
            var s4 = Status(false);
            errorAppended = 1;
        }
    } else if (isEmail(emailValue) && emailValued == '1') {
        clearErrorMessages();
        errorAppended = 0;
        var s4 = Status(true);


    }

    return s4;
}
email.addEventListener('input', function () {
    for(i=1;i<11;i++){
    setTimeout(() => {
    clearErrorMessages();
    errorAppended = 0;
    s4 = emailVerifier(errorAppended, email);    },100);
}

})
passwordVerifier = (errorAppended, password) => {
    const passwordvalue = password.value;
    if (passwordvalue.length < 6 || passwordvalue.length > 20 || !hasSpecialCharacter(passwordvalue) || !hasnumber(passwordvalue) || !haslowercase(passwordvalue) || !hasuppercase(passwordvalue)) {
        if (errorAppended === 0 && passwordvalue.length < 6) {
            appendErrorMessage('Password must be at least 6 characters long', 'red');
            errorAppended = 1;
            var s5 = Status(false);



        } else if (errorAppended === 0 && passwordvalue.length > 20) {
            appendErrorMessage('Password must not exceed 20 characters', 'red');
            errorAppended = 1;
            var s5 = Status(false);


        }
        else if (errorAppended === 0 && !hasSpecialCharacter(passwordvalue)) {
            appendErrorMessage('Password must contain a special character', 'red');
            var s5 = Status(false);
            errorAppended = 1;


        }
        else if (errorAppended === 0 && !hasnumber(passwordvalue)) {
            appendErrorMessage('Password must contain a number', 'red');
            errorAppended = 1;
            var s5 = Status(false);


        }
        else if (errorAppended === 0 && !haslowercase(passwordvalue)) {
            appendErrorMessage('Password must contain a lowercase letter', 'red');
            var s5 = Status(false);
            errorAppended = 1;

        }
        else if (errorAppended === 0 && !hasuppercase(passwordvalue)) {
            appendErrorMessage('Password must contain an uppercase letter', 'red');
            var s5 = Status(false);
            errorAppended = 1;


        }
    } else if (passwordvalue.length >= 6 && passwordvalue.length <= 20) {
        clearErrorMessages();
        errorAppended = 0;
        var s5 = Status(true);

    }
    return s5;
}
password.addEventListener('focus', function () {
    if (password.value.length == 0) {
        clearErrorMessages();
        appendErrorMessage('Password must contain at least 1 uppercase letter, 1 lowercase letter, 1 number and 1 special character', 'blue');
    }
})
password.addEventListener('input', function () {
    clearErrorMessages();
    errorAppended = 0;
    s5 = passwordVerifier(errorAppended, password);
})
confirmpasswordVerifier = (errorAppended, confirmpassword) => {
    const confirmpasswordvalue = confirmpassword.value;
    if (confirmpasswordvalue !== password.value) {
        if (errorAppended === 0) {
            appendErrorMessage('Password and Confirm Password must be same', 'red');
            var s6 = Status(false);
            errorAppended = 1;


        }
    } else if (confirmpasswordvalue === password.value) {
        clearErrorMessages();
        errorAppended = 0;
        var s6 = Status(true);

    }
    return s6;
}
confirmpassword.addEventListener('input', function () {
    clearErrorMessages();
    errorAppended = 0;
    s6 = confirmpasswordVerifier(errorAppended, confirmpassword);
})

setInterval(function () {
    if (s1 == true && s2 == true && s3 == true && s4 == true && s5 == true && s6 == true) {
        btnunblocker();
    } else {
        btnblocker();
    }
}, 50)
