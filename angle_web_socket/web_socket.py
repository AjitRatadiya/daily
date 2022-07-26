from smartapi import SmartWebSocket
from tickdata import TickData


class WebSoc:
    __instance = None

    @staticmethod
    def getinstance():
        if WebSoc.__instance is None:
            WebSoc()
        return WebSoc.__instance

    def __init__(self):
        self.token = None
        if WebSoc.__instance is None:
            WebSoc.__instance = self
            self.ticker = SmartWebSocket('095039062', 'PICIA1012')
            self.task = "mw"
            self.ticks = {}

        else:
            raise Exception("We can not creat another class")

    def run(self, token):
        self.token = token
        self.ticker._on_open = self.on_open
        self.ticker._on_message = self.on_message
        self.ticker._on_error = self.on_error
        self.ticker._on_close = self.on_close
        self.ticker.connect()

    def on_message(self, ws, message):
        for bTick in message:
            if "ltp" in bTick:
                if bTick['tk'] not in self.ticks:
                    tck_obj = TickData()
                    tck_obj.ltp = bTick['ltp']
                    tck_obj.token = bTick['tk']
                    self.ticks[bTick['tk']] = tck_obj
                else:
                    self.ticks[bTick['tk']].ltp = bTick['ltp']

    def on_open(self, ws):
        print("on open")
        self.ticker.subscribe(self.task, self.token)

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print("on close")
