import websocket
import json
import logging

logging.basicConfig(filename="test_ethusdt.log", level=logging.DEBUG,format='%(asctime)s %(levelname)s:%(message)s',filemode='w')
logger=logging.getLogger() 
crypt = "ethusdt"
socket = f'wss://stream.binance.com:9443/ws/{crypt}@kline_1m'

closes = []
SMA = []

def on_message(ws, message):
    json_message = json.loads(message)
    candle = json_message['k']
    is_candle_is_closed = candle['x']
    close = candle['c']
    high = candle['h']
    low = candle['l']
    #volume = candle['v']

    #if is_candle_is_closed:    только для закрытой?
    closes.append(float(close)) 
    SMA = float(sum(closes)/len(closes)) #среднее по цене закрытия
    logger.info(crypt)
    logger.info('Close price')
    logger.info(close)
    logger.info('High price')
    logger.info(high)
    logger.info('Low price')
    logger.info(low)
    logger.info('SMA')
    logger.info(close)
    logger.info('#################################')

def on_close(ws):
   print("### closed ###")

ws = websocket.WebSocketApp(socket, on_message = on_message, on_close = on_close)
ws.run_forever()
