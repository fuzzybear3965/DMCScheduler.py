var ws = new WebSocket("ws://127.0.0.1:5678/")

function sendData(event) {
    ws.send(JSON.stringify(table.getData()));
};

ws.onmessage = function(event) {
    data = JSON.parse(event.data);
    insertSchedule(data);
}

msg = document.getElementById('send');
msg.addEventListener('click', sendData)
