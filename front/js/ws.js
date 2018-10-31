var ws = new WebSocket("ws://127.0.0.1:5678/")

function sendData(event) {
    ws.send(JSON.stringify(table.getData()));
};

ws.onmessage = function(event) {
    data = JSON.parse(event.data);
    for (error of data.errors) {
        alert(error);
    }
    if (data.message === 'schedule') {
        insertSchedule(data.schedule);
    }
}

msg = document.getElementById('send');
msg.addEventListener('click', sendData)
