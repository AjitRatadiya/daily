class a:
    name = 'ajit'

    def dis(self):
        print("mother")


class b(a):

    def dis(self):
        super().dis()
        print("child", self.name)


obj=b()
obj.dis()