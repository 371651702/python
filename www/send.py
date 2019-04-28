#coding = utf - 8


import pika
import json
import time
import copy
from datetime import datetime, timedelta
# from datasender.mongo import Mongo


class BondMarketDataSender(object):

    def Send(self, url, port, exchange, msg):
        connection = pika.BlockingConnection(pika.ConnectionParameters(url, port))
        channel = connection.channel()
        channel.exchange_declare(exchange=exchange, exchange_type='fanout', durable=True)

        channel.basic_publish(exchange=exchange,
                          routing_key='',
                          body=msg,
                          properties=pika.spec.BasicProperties(content_type="text/plain"))
        print('发送消息：', msg)
        connection.close()

    def Msg(self, file):
        file = open(file, 'r', encoding='utf-8')
        lines = file.readlines()
        results =[]
        for line in lines:
            now = datetime.now().strftime('%Y%m%d-%H:%M:%S.%f')
            now = now[:-3]
            result = line.strip('\n').replace("$NOW", now)
            results.append(result)
        return results


if __name__ == '__main__':
    exchange = "STC_MARKET_DATA_MESSAGE_IN"
    url="172.16.96.51"
    port=5672
    sender=BondMarketDataSender()
    messages = sender.Msg('testdata.txt')
    for i in range(0,len(messages),3):
        # print(i,message[i:i+3])
        message=messages[i:i+3]
        # print("mgs>>>",i,len(mgs),mgs)
        for mgs in message:
            print("mgs>>>",i,mgs)
            sender.Send(url, port, exchange, mgs)
        time.sleep(5)

    # for mgs in message:
    #     sender.Send(url, port, exchange, mgs)
        # time.sleep(15)

    # i=0
    # while i< int((len(message))/3):
    #     print(i, message[3 * i:3 * (i + 1)])
    #     i+=1













