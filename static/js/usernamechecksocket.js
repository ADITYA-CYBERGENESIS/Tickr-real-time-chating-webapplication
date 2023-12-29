username = document.querySelector('#username')
email = document.querySelector('#email')
let usernameChecking = document.querySelector('#forusernamechecking')
let usernameCheckinginp = document.querySelector('#forusernamecheckinginp')
let emailChecking = document.querySelector('#foremailchecking')
let emailCheckinginp = document.querySelector('#foremailcheckinginp')
var ws = new WebSocket("ws://localhost:8000/registration/ws");


ws.onopen = function () {
    username.addEventListener('input', function (event) {
        console.log('connected')
        usernamevalue = username.value
        usernameValue = usernamevalue.toLowerCase();
        if (!hasSpecialCharacter(usernameValue) && usernameValue.length >= 6 && usernameValue.length <= 20) {
            let data = {
                'is': 'username',
                'username': usernameValue
            }
            data = JSON.stringify(data)
            ws.send(data)
        }
    })
    email.addEventListener('input', function (event) {
        emailvalue = email.value
        emailValue = emailvalue.toLowerCase();
        if (isEmail(emailValue)) {
            let data = {
                'is': 'email',
                'email': emailValue
            }
            data = JSON.stringify(data)
            ws.send(data)
        }
    })
    
};
ws.onmessage = function (e) {
    const response = JSON.parse(e.data);
    console.log(response)
    if (response.availability == 1 && response.is == 'username') {
        usernameChecking.innerHTML = ""
        usernameChecking.innerHTML = `
         <span style="color: green;justify-content: flex-end;" class="flex-center">Username available<svg style="margin-left:5px" xmlns="http://www.w3.org/2000/svg" width="24" height="20" viewBox="0 0 12 12"><path fill=green d="M6 12A6 6 0 1 0 6 0a6 6 0 0 0 0 12Zm2.53-6.72L5.78 8.03a.75.75 0 0 1-1.06 0l-1-1a.75.75 0 0 1 1.06-1.06l.47.47l2.22-2.22a.75.75 0 0 1 1.06 1.06Z"/></svg></span> `

        usernameCheckinginp.innerHTML = `<input id="forusernamecheckinginput" type="number"value=${response.availability} hidden>`
    }
    else if (response.availability == 2 && response.is == 'username') {
        usernameChecking.innerHTML = ""
        usernameChecking.innerHTML = `<span style="color: red;
    justify-content: flex-end;" class="flex-center">Username taken. Try another<svg style="margin-left:5px" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><path fill=red fill-rule="evenodd" d="M5.312 10.762C8.23 5.587 9.689 3 12 3c2.31 0 3.77 2.587 6.688 7.762l.364.644c2.425 4.3 3.638 6.45 2.542 8.022S17.786 21 12.364 21h-.728c-5.422 0-8.134 0-9.23-1.572s.117-3.722 2.542-8.022l.364-.645ZM12 7.25a.75.75 0 0 1 .75.75v5a.75.75 0 0 1-1.5 0V8a.75.75 0 0 1 .75-.75ZM12 17a1 1 0 1 0 0-2a1 1 0 0 0 0 2Z" clip-rule="evenodd"/></svg></span>`
        usernameCheckinginp.innerHTML = `<input id="forusernamecheckinginput" type="number"value=${response.availability} hidden>`
    }
    else if (response.availability == 1 && response.is == 'email') {
        emailChecking.innerHTML = ""
        emailChecking.innerHTML = `<span style="color: green;
        justify-content: flex-end;" class="flex-center">Email available<svg style="margin-left:5px" xmlns="http://www.w3.org/2000/svg" width="24" height="20" viewBox="0 0 12 12"><path fill=green d="M6 12A6 6 0 1 0 6 0a6 6 0 0 0 0 12Zm2.53-6.72L5.78 8.03a.75.75 0 0 1-1.06 0l-1-1a.75.75 0 0 1 1.06-1.06l.47.47l2.22-2.22a.75.75 0 0 1 1.06 1.06Z"/></svg></span>`
        emailCheckinginp.innerHTML = `<input id="foremailcheckinginput" type="number"value=${response.availability} hidden> `

    }
    else if (response.availability == 2 && response.is == 'email') {
        emailChecking.innerHTML = ""
        emailChecking.innerHTML = `<span style="color: red;
    justify-content: flex-end;" class="flex-center">Email Already in Use. Try another<svg style="margin-left:5px" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><path fill=red fill-rule="evenodd" d="M5.312 10.762C8.23 5.587 9.689 3 12 3c2.31 0 3.77 2.587 6.688 7.762l.364.644c2.425 4.3 3.638 6.45 2.542 8.022S17.786 21 12.364 21h-.728c-5.422 0-8.134 0-9.23-1.572s.117-3.722 2.542-8.022l.364-.645ZM12 7.25a.75.75 0 0 1 .75.75v5a.75.75 0 0 1-1.5 0V8a.75.75 0 0 1 .75-.75ZM12 17a1 1 0 1 0 0-2a1 1 0 0 0 0 2Z" clip-rule="evenodd"/></svg></span>`
        emailCheckinginp.innerHTML = `<input id="foremailcheckinginput" type="number"value=${response.availability} hidden> `

    }
}
ws.onclose = function () {
    console.log('discennected')

    
};
ws.onerror = function () {
    console.log('error');
};
username.addEventListener('blur', () => {
    usernameChecking.innerHTML = ""
})

email.addEventListener('blur', () => {
    emailChecking.innerHTML = ""
})

