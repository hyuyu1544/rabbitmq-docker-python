import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='my_first_queue')
message='Hello World!'
channel.basic_publish(exchange='',
                      routing_key='my_first_queue',
                      body=message)
print("Sent the message: {}".format(message))
connection.close()