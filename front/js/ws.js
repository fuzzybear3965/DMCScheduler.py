var ws = new WebSocket("ws://127.0.0.1:5678/")

function sendData(event) {
    var cnt = 0;
    return function(){
        cnt += 1;
        ws.send("hey " + cnt);
    }
};

ws.onmessage = function(event) {
    console.log(event.data);
}

msg = document.getElementById('send');

msg.addEventListener('click', sendData())
