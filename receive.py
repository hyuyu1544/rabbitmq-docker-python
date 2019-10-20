from connect_rabbitmq import ConnectRMQ

rmq = ConnectRMQ()

try:
    rmq.receive_message()
except:
    rmq.stop_connection()
