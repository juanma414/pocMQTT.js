// Conectar al broker MQTT
const client = mqtt.connect('wss://test.mosquitto.org:8081');

// Suscribirse al tópico inicial
client.on('connect', () => {
    console.log('Conectado al broker MQTT');
    client.subscribe('test/topic', (err) => {
        if (!err) {
            console.log('Suscrito al tópico test/topic');
        }
    });
});

// Manejar mensajes recibidos
client.on('message', (topic, message) => {
    const msgList = document.getElementById('messages');
    const newMsg = document.createElement('li');
    newMsg.textContent = `Tópico: ${topic} - Mensaje: ${message.toString()}`;
    msgList.appendChild(newMsg);
});

// Enviar un mensaje al tópico especificado
function sendMessage() {
    const topic = document.getElementById('topic').value;
    const message = document.getElementById('message').value;
    client.publish(topic, message);
}

// Suscribirse a un nuevo tópico
function subscribeToNewTopic() {
    const newTopic = document.getElementById('newTopic').value;
    client.subscribe(newTopic, (err) => {
        if (!err) {
            console.log(`Suscrito al nuevo tópico ${newTopic}`);
        }
    });
}

// Desuscribirse de un tópico
function unsubscribeFromTopic() {
    const unsubscribeTopic = document.getElementById('unsubscribeTopic').value;
    client.unsubscribe(unsubscribeTopic, (err) => {
        if (!err) {
            console.log(`Desuscrito del tópico ${unsubscribeTopic}`);
        }
    });
}