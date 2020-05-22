class even:
    def _init_(self,a):
        self.a=a
    def num(self):
        no=int(input("enter the number"))
        if no%2==0:
            print("even")
        else:
            print("odd")
obj=even()
obj.num()
