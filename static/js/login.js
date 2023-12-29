const regForm = document.getElementById('regform');
const btn = document.querySelector('.submit-btn');
let usernameoremail = document.querySelector('#usernameoremail');
let password = document.getElementById('password');
var s1, s2;  // Declare s1 and s2 variables

const Status = (boolean) => {
    return boolean;
};

const appendErrorMessage = (message, color) => {
    const error = document.createElement('div');
    error.innerHTML = message;
    error.classList.add('message', `${color}`);
    regForm.appendChild(error);  // Use appendChild instead of append
};

const clearErrorMessages = () => {
    regForm.innerHTML = '';
    errorAppended = 0;  // It seems errorAppended is not declared anywhere
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
            }, 300);
        }
    });
};

const btnunblocker = () => {
    btn.type = 'submit';
    if (btn.classList.contains('blocked_btn')) {
        btn.classList.remove('blocked_btn');
    }
};

const usernameoremailVerifier = (usernameoremail) => {
    if (usernameoremail.value.length === 0) {
        appendErrorMessage(`Username or Email can't be blank`,'red');
        s1 = Status(false);
    } else {
        s1 = Status(true);
    }
};

const passwordVerifier = (password) => {
    if (password.value.length === 0) {
        appendErrorMessage(`Password can't be blank`,'red');
        s2 = Status(false);
    } else {
        s2 = Status(true);
    }
};

usernameoremail.addEventListener('input', function () {
    clearErrorMessages();
    usernameoremailVerifier(usernameoremail);
});

password.addEventListener('input', function () {
    clearErrorMessages();
    passwordVerifier(password);
});

setInterval(function () {
    if (s1 === true && s2 === true) {
        btnunblocker();
    } else {
        btnblocker();
    }
}, 50);
