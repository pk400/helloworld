class User:
    name = ''
    def __init__(self, name):
        self.name = name

    def greeting(self):
        sayhello('Hello ' + self.name + '!')

def sayhello(str):
  print(str)

sayhello('hello world!')

jj = User('Joel')
jj.greeting()