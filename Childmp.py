# Inheritance
from oops import Calculator


class ChildImp(Calculator):
    num2=200

    def __init__(self):
        Calculator.__init__(self,20,30)
    def getCompleteData(self):
        return self.num2+self.num+self.Summation()

obj=ChildImp()
print(obj.getCompleteData())
