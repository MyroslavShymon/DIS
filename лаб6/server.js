const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 8080 });

// Масив для зберігання історії чату
const chatHistory = [];

wss.on('connection', function connection(ws) {
    console.log('New client connected');

    // Відправка історії чату при підключенні нового клієнта
    sendChatHistory(ws);
    ws.send('Зарплата була перерахована на карткові рахунки працівників.');
    ws.on('message', function incoming(message) {
        console.log('Received: %s', message);
        const data = JSON.parse(message);

        // Обробляємо запит на отримання історії чату
        if (data.action === 'getChatHistory') {
            sendChatHistory(ws);
        } else {
            // Додаємо повідомлення до історії чату
            chatHistory.push(data);

            // Пересилаємо повідомлення всім підключеним клієнтам
            wss.clients.forEach(function each(client) {
                if (client.readyState === WebSocket.OPEN) {
                    client.send(JSON.stringify(data));
                }
            });
        }
    });

    ws.on('close', function close() {
        console.log('Client disconnected');
    });
});

// Функція для відправлення історії чату
function sendChatHistory(ws) {
    ws.send(JSON.stringify(chatHistory));
}