from confluent_kafka import Consumer
import json

def notificar(msg):
    pedido_info = json.loads(msg.value())
    notificacao_info_str = f"Notificação para Cliente ID {pedido_info['cliente_id']} - Mensagem: {pedido_info['mensagem']}"

    print(notificacao_info_str)

conf = {
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'notificar-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
consumer.subscribe(['ecommerce-events'])

while True:
    msg = consumer.poll(1.0)  
    if msg is None:
        continue
    if msg.error():
        print(f"Erro ao receber mensagem: {msg.error()}")
    else:
        notificar(msg)
