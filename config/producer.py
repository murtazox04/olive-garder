from confluent_kafka import Producer

producer = Producer({
    'bootstrap.servers': 'localhost:9092'
})