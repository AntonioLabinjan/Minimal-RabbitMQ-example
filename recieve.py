import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='my_queue')

channel.basic_publish(exchange='',
                      routing_key='my_queue',
                      body='Hello RabbitMQ!')

print(" [x] Sent 'Hello RabbitMQ!'")
connection.close()
