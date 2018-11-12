var ws = new WebSocket("ws://127.0.0.1:5678/")

function sendData(event) {
    ws.send(JSON.stringify(table.getData()));
};

ws.onmessage = function(event) {
    data = JSON.parse(event.data);
    error_msg = data.errors.join('\n');

    if (error_msg) {
        alert(error_msg)
    }

    if (data.message === 'schedule') {
        insertSchedule(data.schedule);
    }
}

msg = document.getElementById('send');
msg.addEventListener('click', sendData)
