var ws = new WebSocket("ws://127.0.0.1:5678/")

function sendData(event) {
    ws.send(table.getData());
};

ws.onmessage = function(event) {
    console.log(event.data);
}

msg = document.getElementById('send');
msg.addEventListener('click', sendData)
