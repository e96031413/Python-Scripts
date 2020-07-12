class Bank(object):
    def __init__(self):
        self.balance = 1000  #預設存款1000

    def deposit_money(self, amount):    # CREATE
        return self.balance + amount

    def get_balance(self):            # READ
        return self.balance

    def withdraw_money(self, amount):    # CREATE
        return self.balance - amount
bank = Bank()
mode = int(input("檢查餘額輸入0, 存款輸入1, 提款輸入2, 離開輸入3:"))

if mode ==0 or 1 or 2 or 3:
    if mode == 0:
        print("目前存款餘額:", bank.get_balance())
    if mode == 1:
        deposit_amount = int(input("請輸入存入的金額:"))
        print("存入後的存款:", bank.deposit_money(deposit_amount))
    if mode == 2:
        withdraw_amount = int(input("請輸入欲提款的金額:"))
        print("提款後的餘額:", bank.withdraw_money(withdraw_amount))
    if mode == 3:
        print("謝謝惠顧")

if mode >3:
    print("執行錯誤，請輸入正確數字")
if mode <0:
    print("執行錯誤，請輸入正確數字")