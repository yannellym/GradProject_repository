def main():
    
      name = "Paulo"

      number = 21.2

      c1 = Client("Fernandes", 64)

      x = number
      print(x)
      
class Client:
    
    def __init__(self, name, number):
        self.name = name
        self.number = int(number)

    def getName(self):
        return self.name

    def getNumber(self):
        return self.number
main()