# 房貸月繳金額計算
import sys

class homeloan:
    def __init__(self, name, years, amount, rate):
        self.__name = name
        self.__years = years
        self.__amount = amount
        self.__rate = rate
    def getname(self):
        return self.__name
    def get_month_payment(self):
        return round((self.__amount * (1 + self.__rate)) / (self.__years * 12))

while True:
    print("輸入Q離開或隨意鍵繼續")
    key = input()
    key.lower()
    if key == 'q':
        sys.exit()
    while True:
        name = input("姓名:")
        while True:
            try:
                amount = eval(input("貸款總金額(單位:萬):"))
                amount *= 10000
            except NameError:
                print("輸入金額格式錯誤，請重新輸入")
            except SyntaxError:
                print("輸入金額格式錯誤，請重新輸入")
            else:
                break
        while True:
            years = eval(input("貸款年限(3,5,20):"))
            if years != 3 and years != 5 and years != 20:
                print("貸款年限格式錯誤，請重新輸入")
                continue
            elif years == 3:
                rate = 0.0603
                break
            elif years == 5:
                rate = 0.0620
                break
            elif years == 20:
                rate = 0.0650
                break
        client = homeloan(name, years, amount, rate)
        print("{0}的每月還款金額為{1:,}元\n".format(client.getname(), client.get_month_payment()))
        break
