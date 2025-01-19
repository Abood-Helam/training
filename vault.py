class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons= galleons
        self.sickles= sickles
        self.kunts= knuts

    def __str__(self):
        return f"{self.galleons} Galleons,{self.sickles} Sickles, {self.kunts} Kunts"
    
    def __add__(self, other):
        galleons= self.galleons + other.galleons
        sickles= self.sickles + other.sickles
        kunts= self.kunts + other.kunts
        return Vault(galleons, sickles, kunts)

potter = Vault(100, 50, 25)
print(potter)

weasly= Vault(25, 50, 100)
print(weasly)

total = potter + weasly
print(total)