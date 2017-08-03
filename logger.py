import logging.config
import tornado
from bitstampws import Client as Websocket

import lib.configs.logging
from lib.subscribers import SimpleLoggerSubscriber


logging.config.dictConfig(lib.configs.logging.d)


with Websocket() as client:
    with SimpleLoggerSubscriber(client):
        client.connect()
        try:
            tornado.ioloop.IOLoop.instance().start()
        except KeyboardInterrupt:
            client.close()

