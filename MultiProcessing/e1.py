from multiprocessing import Process


def myfunction():
    print('hi!! I am Python')

if __name__ == '__main__':

    p = Process(target=myfunction)
    p.start()

    p.join()
