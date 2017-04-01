
import json
import websocket
from pyee import EventEmitter

from mycroft.configuration import ConfigurationManager

config = ConfigurationManager.get().get("daphne").get("websocket")


class DaphneWebsocketClient():
    
    def __init__(self):
        self.port = config.get("port")
        self.host = config.get("host")
        self.route = config.get("route")
        self.url = "ws://" + self.host + ":" + str(self.port) + self.route + "/"
        self.emitter = EventEmitter()
        
        self.ws = websocket.WebSocketApp(self.url,
                                        on_open=self.on_open,
                                        on_close=self.on_close,
                                        on_error=self.on_error,
                                        on_message=self.on_message)
        
    
    def run_forever(self):
        self.ws.run_forever()
        
    def on_open(self, ws):
        ws.send("Connection made from Mycroft")
    def on_close(self, ws):
        pass
    def on_error(self, ws, error):
        pass
    def on_message(self, ws, message):
        self.emitter.emit('message', message)
        
    def on(self,event_name, func):
        self.emitter.on(event_name,func)
    
    
        
        