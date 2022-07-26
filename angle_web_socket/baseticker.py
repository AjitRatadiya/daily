from web_socket import WebSoc
from threading import Thread


class BaseTicker:
    def __init__(self, stra):
        self.socket_instance = WebSoc.getinstance()
        Thread(target=self.socket_instance.run, args=(stra, )).start()

    def get_value(self, token):
        print("dic:", self.socket_instance.ticks)
        if token in self.socket_instance.ticks:
            print("ltp:",self.socket_instance.ticks[token].ltp)


if __name__ == '__main__':
    obj = BaseTicker("nse_cm|3045")
    while True:
        inpt = input("enter token:")
        obj.get_value(inpt)
        if inpt == 0:
            break
