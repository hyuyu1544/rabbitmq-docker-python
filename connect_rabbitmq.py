import pika


class ConnectRMQ:
    def __init__(self, Host='localhost', Queue='my_first_queue'):
        self.queue = Queue
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=Host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=Queue)

    def send_message(self, message):
        self.channel.basic_publish(exchange='',
                                   routing_key=self.queue,
                                   body=message)
        print("Sent the message: {}".format(message))

    def on_message(self, channel, method_frame, header_frame, body):
        print(method_frame.delivery_tag)
        print('Receive the message: {}'.format(body))
        print()

    def receive_message(self):
        self.channel.basic_consume(self.queue, self.on_message, auto_ack=True)
        self.channel.start_consuming()

    def stop_connection(self):
        self.connection.close()
