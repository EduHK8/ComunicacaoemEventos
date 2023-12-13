from confluent_kafka import Producer
import json

def pagar():
    pedido_info = {"mensagem": "Novo pedido recebido", "valor_total": 150.00, "cliente_id": 123}

    print("Início do processamento do pagamento")

    producer.produce("ecommerce-events", value=json.dumps(pedido_info))
    producer.flush()

    print("Mensagem de pagamento produzida com sucesso no tópico 'ecommerce-events'")

    print("Término do processamento do pagamento")

conf = {
    'bootstrap.servers': 'kafka:9093',
    'client.id': 'pagar-producer'
}

producer = Producer(conf)
pagar()
