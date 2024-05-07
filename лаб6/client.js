const WebSocket = require('ws');

const ws = new WebSocket('ws://localhost:8080');

ws.on('open', function open() {
    console.log('Connected to server');

    // Відправляємо перше привітання
    ws.send('Hello from client!');
});

ws.on('message', function incoming(data) {
    console.log('Received: %s', data);
});

// Відправляємо повідомлення кожні 3 секунди
setInterval(() => {
    ws.send('Ping from client');
}, 3000);