
import json
from websocket import WebSocket, create_connection
from mycroft.configuration import ConfigurationManager

config = ConfigurationManager.get().get("daphne").get("websocket")


class DaphneWebsocketClient():
    
    def __init__(self):
        self.port = config.get("port")
        self.host = config.get("host")
        self.route = config.get("route")
        self.url = "ws://" + host + ":" + str(port) + route + "/"
        ws = create_connection(self.url)
        
    def send_message(self,message):
        ws = create_connection(self.url)
        ws.send(message)
        ws.close()
        
        
        