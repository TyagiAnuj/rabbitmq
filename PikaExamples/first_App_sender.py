import pika

#Define connection parameters
my_credentials=pika.PlainCredentials(username='rmq_root',password='112233')
server_parameters=pika.ConnectionParameters(host='192.168.122.2',credentials=my_credentials)
message_properties=pika.BasicProperties(delivery_mode=2)

#connecting to the channel
connection = pika.BlockingConnection(server_parameters)
channel = connection.channel()
channel.basic_qos(prefetch_count=1)

#Create queue to send messages to,
# (If we send a message to non-existing location,
#  RabbitMQ will just trash the message)
# Durable means that rabbitMQ will not lose our queue
channel.queue_declare(queue='hello',durable=True)

#the exchange defines how messages are routed to queues, default exchange lets the routing_parameter specify the queue

continue_to_send=True
message=''
while(continue_to_send and message!='EXIT'):
    message=raw_input("Enter message to send : ")
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=message,
                          properties=message_properties)
    print " [x] Sent {}".format(message)

#Before exiting the program we need to make sure the network buffers were flushed and our message was actually delivered to RabbitMQ
connection.close()
