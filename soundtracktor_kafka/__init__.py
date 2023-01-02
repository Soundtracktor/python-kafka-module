from kafka import KafkaConsumer, KafkaProducer
import os
import json

# Set up the Kafka consumer
# value_deserializer=lambda x: _safe_utf8_decode(x),
# move into python-kafka-module
def create_consumer(*, topic, group_id):
    return KafkaConsumer(
        topic,  # topic to consume from
        group_id=group_id,  # consumer group to join
        bootstrap_servers=[os.environ.get('KAFKA_BROKER_0')],  # list of Kafka brokers
        auto_offset_reset='earliest',  # start consuming from the earliest message
        enable_auto_commit=True,  # disable auto-commit of offsets
        value_deserializer=lambda x: json.loads(x.decode('utf-8')), # decode the message value as UTF-8
        api_version=None,
        max_poll_records=200,
        session_timeout_ms=60000,
    )

# Set up the Kafka producer
def create_producer():
    return KafkaProducer(
        bootstrap_servers=[os.environ.get('KAFKA_BROKER_0')],  # list of Kafka brokers
        value_serializer=lambda x: json.dumps(x).encode('utf-8'), # encode the message value as UTF-8
        key_serializer=lambda x: x.encode('utf-8'),  # encode the message key as UTF-8
    )
