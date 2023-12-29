var fileInput = document.getElementById('message_file_selector');
function uploadFile() {
    var file = fileInput.files[0];

    var formData = new FormData();
    formData.append('file', file);

    var uploadUrl = 'http://127.0.0.1:8000/image/chatwithroot/2/adityasonkar/1';
    fetch(uploadUrl, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log('File uploaded successfully:', data);
    })
    .catch(error => {
        console.error('Error uploading file:', error);
    });
}
fileInput.addEventListener('change', function () {
    if (fileInput.files.length > 0) {
        let fileType = fileInput.files[0].type;
        let fileSizeBytes = fileInput.files[0].size;
        let fileSizeMB = fileSizeBytes / (1024 * 1024);
        let fileSource = URL.createObjectURL(fileInput.files[0]);
        if (fileType.startsWith('image/')) {
            console.log('Image uploaded:', fileInput.files[0].name, '| Size:', fileSizeMB.toFixed(2) + ' MB');
            let div = document.createElement('div');
            div.classList.add('fileshowerbg');
            div.classList.add('flex-center');
            div.innerHTML = `
                    <div class="fileshower">
                        <img src="${fileSource}" alt="uploads" class="fileimg">
                        <div class="filebtns flex-center"><a onclick="filecancel()" id="filecancel">CANCEL</a><a onclick="uploadFile()" id="filesend">SEiND</a></div>
                    </div>
                `;
                document.body.prepend(div);
        } else {
            let div = document.createElement('div');
            div.classList.add('fileshowerbg')
            div.classList.add('flex-center')
            div.innerHTML = `<div class="fileshowerbg flex-center">
                <div class="fileshower">
                    <div class="filecontainer flex-center"><svg xmlns="http://www.w3.org/2000/svg" width="45" height="45"
                            viewBox="0 0 24 24">
                            <path fill="#888888"
                                d="M12 18.212q1.367 0 2.3-1.002q.93-1.002.93-2.402V10.73q0-.214-.142-.357t-.357-.143q-.214 0-.357.143t-.143.357v4.077q0 .979-.643 1.691q-.642.713-1.588.713q-.94 0-1.586-.713q-.645-.712-.645-1.691V9.346q0-.398.246-.69q.247-.29.62-.29q.378 0 .622.29q.243.292.243.69v4.962q0 .213.143.356q.144.144.357.144t.357-.144q.143-.143.143-.356V9.346q0-.8-.533-1.39q-.532-.59-1.332-.59t-1.333.59q-.533.59-.533 1.39v5.462q0 1.4.935 2.402q.934 1.002 2.296 1.002M6.615 21q-.69 0-1.152-.462Q5 20.075 5 19.385V4.615q0-.69.463-1.152Q5.925 3 6.615 3h8.116L19 7.27v12.115q0 .69-.462 1.152q-.463.463-1.153.463zm0-1h10.77q.23 0 .423-.192q.192-.193.192-.423V7.769h-2.962q-.348 0-.577-.23q-.23-.23-.23-.577V4H6.615q-.23 0-.423.192Q6 4.385 6 4.615v14.77q0 .23.192.423q.193.192.423.192M6 4v3.77zv16z" />
                        </svg>
                        <div class="fileinfo flex-center">
                            <span class="filename">${fileInput.files[0].name}</span>
                            <span class="filesize flex-center">${fileSizeMB.toFixed(2)} MB</span>
                        </div>
                    </div>
                    <div class="filebtns flex-center"><a onclick="filecancel()"  id="filecancel">CANCEL</a><a id="filesend">SEND</a></div>
                </div>
            </div> `
            document.body.prepend(div);
            console.log('Other file uploaded:', fileInput.files[0].name, '| Size:', fileSizeMB.toFixed(2) + ' MB');
        }
    }
});
const filecancel = (()=>{
let fileshower = document.querySelector('.fileshowerbg')
fileshower.remove()
})
