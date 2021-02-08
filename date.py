import datetime
class Test:
   def __init__(self):
    now = datetime.datetime.now()
    self.date = now.strftime("%Y-%m-%d")
    self.time = now.strftime("%H:%M:%S")
def fun():
    return Test()

t = fun()
print (t.date)
print (t.time)

