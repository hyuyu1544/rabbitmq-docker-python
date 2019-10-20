from connect_rabbitmq import ConnectRMQ

rmq = ConnectRMQ()

message = 'Hello World!'
rmq.send_message(message)
rmq.stop_connection()
