import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='my_first_queue')


def on_message(channel, method_frame, header_frame, body):
    print(method_frame.delivery_tag)
    print('Receive the message: {}'.format(body))
    print()
    # channel.basic_ack(delivery_tag=method_frame.delivery_tag)


channel.basic_consume('my_first_queue', on_message, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()