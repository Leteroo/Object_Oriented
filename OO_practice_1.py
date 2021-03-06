# 會員制度
class members:
    def __init__(self, cost, name):
        self.__name = name
        self.__cost = cost
    def getname(self):
        return self.__name
    def checkout(self):
        return self.__cost
    def printcheckout(self):
        print('Hello {0}! How do you do today!'.format(self.getname()))
        print('All things you buy are {0} dollars.'.format(self.__cost))
    
class silvermembers(members):
    def __checkout(self):
        return round(super().checkout() * 0.95)
    def printcheckout(self):
        print('Glad to see you %s! We have some discount for you!'%super().getname())
        print('All things you buy are %d dollars. See you next time!'%self.__checkout())

class goldenmembers(members):
    def __checkout(self):
        return round(super().checkout() * 0.85)
    def printcheckout(self):
        print('Welcome back %s! How can we help you today?'%super().getname())
        print('All things you buy are %d dollars. We are always ready to serve you!'%self.__checkout())

customer1 = members(30000, 'Ran')
customer2 = silvermembers(30000, 'Michelle')
customer3 = goldenmembers(30000, 'Isaac')

customer1.printcheckout()
print()
customer2.printcheckout()
print()
customer3.printcheckout()
