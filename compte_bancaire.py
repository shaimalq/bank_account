class compte:
    def __init__(self,balance=0) :
        self.balance =balance


    def getbalance(self):
        return self.balance
    def deposer(self ,amount ):
        self.balance += amount
    def retirer(self ,amount ):
        self.balance -= amount 
    def ajouter_interet(self,rate):
        self.balance = self.balance*(1+rate)

c1=compte()
c2 =compte(2000)
c1.deposer(100)
c2.retirer(1000)
c1.ajouter_interet(0.5)
print(c1.getbalance())   
print(c2.getbalance())   
