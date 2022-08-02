def greeting(func):
    def wraper(*args, **kwargs):
        print('Good Moring')
        return func(*args, **kwargs)

    return wraper


@greeting
def emp(name):
    print(name)


emp('ajit')

