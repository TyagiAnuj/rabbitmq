__author__ = 'niko'
import pika

#define connection parameters
my_credentials= pika.PlainCredentials(username='rmq_root',password='112233')
parameters=pika.ConnectionParameters(host='192.168.122.2',credentials=my_credentials)

#connecting to the rabbitMQ and getting channel
connection=pika.BlockingConnection(parameters=parameters)
channel=connection.channel()


#define calback functions to activate whenever new messages arrive
def callback(channel,method,properties,body):
    print("[x] Recieved:  {}".format(body))

print ' [*] Waiting for messages. To exit press CTRL+C'
channel.basic_consume(consumer_callback=callback,queue='hello',no_ack=True)
channel.start_consuming()
