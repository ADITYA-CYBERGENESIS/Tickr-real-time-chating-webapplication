// document.addEventListener('DOMContentLoaded', function () {

const msgSubmit = document.querySelector('#send_message_submitbtn')
const msgForm = document.querySelector('#send_message_form')
const msgFormInp = document.querySelector('#send_message_form-inp')
const chatarea = document.querySelector('.message_viewing_area')

var id = document.querySelector('#receiverid');
id = id.value;
var receiverUsername = document.querySelector('#receiveruname');
receiverUsername = receiverUsername.value;
var senderUsername = document.querySelector('#senderuname');
senderUsername = senderUsername.value;
let rid = id
var ws = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + rid
    + '/'
);
function scrollToBottom() {
    chatarea.scrollTop = chatarea.scrollHeight;
}


window.onload = function () {
    scrollToBottom();
  };

ws.onopen = function (e) {
    console.log('connected');
    console.log(senderUsername + ' cennected ' + receiverUsername)
    msgForm.addEventListener('submit', (e) => {
        e.preventDefault()
        msg = msgFormInp.value
        if (msg != '') {
            let data = {
                'username': senderUsername,
                'receiver': receiverUsername,
                'message': msg,
            }
            data = JSON.stringify(data)
            ws.send(data)
            msgFormInp.value = '';
        }
    })
    
};
ws.onmessage = async function (e) {
    let receive_data = JSON.parse(e.data);
    console.log(receive_data)
    let message = receive_data.message
    let sender = receive_data.username
    let time = receive_data.time
    let firstName = receive_data.sfname
    let lastName = receive_data.slname
    console.log(message + ' sent by ' + sender)
    if (sender == receiverUsername) {
        let div = document.createElement('div');
        div.classList.add('message_container-other');
        div.classList.add('flex-center');
        div.innerHTML = `<div class="message-other">
                <div class="message_sender-other">
                    <svg xmlns="http://www.w3.org/2000/svg" width="8" height="8" viewBox="0 0 24 24">
                        <path fill=#0b09106b
                            d="m4.497 20.835l16.51-7.363c1.324-.59 1.324-2.354 0-2.944L4.497 3.164c-1.495-.667-3.047.814-2.306 2.202l3.152 5.904c.245.459.245 1 0 1.458l-3.152 5.904c-.74 1.388.81 2.87 2.306 2.202Z" />
                    </svg> ${firstName} ${lastName}
                </div>
                <div class="message_content-other flex-center">
        ${message}
                </div>
                <div class="message_time-other flex-center">
                    ${time}
                </div>
            </div>`
        chatarea.append(div);
        scrollToBottom()
    }
    else {
        let div = document.createElement('div');
        div.classList.add('message_container-self');
        div.classList.add('flex-center');
        div.innerHTML = `<div class="message-self">
            <div class="message_content-self flex-center">
        ${message}                    
            </div>
            <div class="message_time-self flex-center">
            ${time}
            <svg style="margin-left:2px" xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                    viewBox="0 0 16 16">
                    <path fill="none" stroke="#EAE6F3" stroke-linecap="round" stroke-linejoin="round"
                        stroke-width="1.5" d="m1.75 9.75l2.5 2.5m3.5-4l2.5-2.5m-4.5 4l2.5 2.5l6-6.5" />
                </svg>
            </div>
        </div>`
        chatarea.append(div);
        scrollToBottom()
    }
}
ws.onclose = function () {
    console.log('disconnected');
};

// });