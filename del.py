'''

#Genarator will give iterator
def Topten():
    i=1
    while i<=n:
        sq=i*i
        yield sq
        i+=1
n=int(input('enter no.'))
val=Topten()
for i in val:
    print(i)
    '''
#iterator
'''
class Topten:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
val=Topten()
print(next(val))
for i in val:
    print(i)
'''
def hi():
    i=1
    while i<=n:
        c=i*i
        print(c)
        i=i+1
n=int(input('e'))
hi()
