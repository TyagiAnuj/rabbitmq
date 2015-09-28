
from datetime import datetime
__author__ = 'niko'
import pika ,time
import sys
#define connection parameters
my_credentials= pika.PlainCredentials(username='rmq_root',password='112233')
parameters=pika.ConnectionParameters(host='192.168.122.2',credentials=my_credentials)

#connecting to the rabbitMQ and getting channel
connection=pika.BlockingConnection(parameters=parameters)
channel=connection.channel()


#define calback functions to activate whenever new messages arrive
def callback(channel,method,properties,body):
    print("[x] Recieved:  {}".format(body))
    if body == 'EXIT':
        print "Exiting .. "
        sys.exit()
    print "{} Executing job , it will take approximately {} seconds to complete".format(datetime.now(),body.count('.'))
    time.sleep(body.count('.'))
    print "[x] {} finished executing the task".format(datetime.now())
    channel.basic_ack(delivery_tag=method.delivery_tag)

print ' [*] Waiting for messages. To exit press CTRL+C'
channel.basic_consume(consumer_callback=callback,queue='hello')
channel.start_consuming()


# 1.................................................
# 2.................................................
# 3................................................
# 4................................................
# 5................................................
# 6................................................
# 7................................................
# 8................................................
