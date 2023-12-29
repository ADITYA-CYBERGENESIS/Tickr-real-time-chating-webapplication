password= document.getElementById('password');
confirmpassword= document.getElementById('confirmpassword');
btn = document.querySelector('.submit-btn');
regForm = document.getElementById('regform');
var s5,s6;
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
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
var s1, s2, s3, s4, s5, s6;
// Array of uppercase alphabet letters
const ucAlphabets = Array.from({ length: 26 }, (_, i) => String.fromCharCode('A'.charCodeAt(0) + i));

// Array of lowercase alphabet letters
const lcAlphabets = Array.from({ length: 26 }, (_, i) => String.fromCharCode('a'.charCodeAt(0) + i));

// Array of special characters
const specialCharacters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', ';', ':', ',', '.', '<', '>', '?', '/', '|', '\\'];
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
    if (s5 == true && s6 == true) {
        btnunblocker();
    }else{
        btnblocker();
    }
}, 50)
