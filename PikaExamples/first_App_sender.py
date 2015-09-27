import pika

#Define connection parameters
my_credentials=pika.PlainCredentials(username='rmq_root',password='112233')
server_parameters=pika.ConnectionParameters(host='192.168.122.2',credentials=my_credentials)

#connecting to the channel
connection = pika.BlockingConnection(server_parameters)
channel = connection.channel()

#Create queue to send messages to,(If we send a message to non-existing location, RabbitMQ will just trash the message.)
channel.queue_declare(queue='hello')

#the exchange defines how messages are routed to queues, default exchange lets the routing_parameter specify the queue

continue_to_send=True
message=''
while(continue_to_send and message!='EXIT'):
    message=raw_input("Enter message to send : ")
    channel.basic_publish(exchange='',routing_key='hello',body=message)
    print " [x] Sent {}".format(message)

#Before exiting the program we need to make sure the network buffers were flushed and our message was actually delivered to RabbitMQ
connection.close()
