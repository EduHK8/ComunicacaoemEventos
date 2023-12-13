from confluent_kafka import Consumer
import json
import time

def enviar_email(msg):
    pedido_info = json.loads(msg.value())
    email_info_str = f"E-mail enviado para Cliente ID {pedido_info['cliente_id']} - Assunto: {pedido_info['mensagem']}"

    print(email_info_str)

conf = {
    'bootstrap.servers': 'kafka:9093',
    'group.id': 'enviar-email-group',
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
        time.sleep(5)
    else:
        enviar_email(msg)
