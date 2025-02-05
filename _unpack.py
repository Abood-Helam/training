#first, _ =input("what's your name? ").split(" ")
#print(f"hello, {first}")
def total(galleons, sickles, kunts):
    return(galleons*17+sickles) * 29 + kunts

coins = [100, 50, 25]
#print(total(coins[0], coins[1], coins[2]), "kunts")
#to unpack the list in print we use single *
print(total(*coins), "kunts")

coins = {"galleons":100, "sickles":50, "kunts":25}
#print(total(coins["galleons"], coins["sickles"], coins["kunts"]), "kunts")
#to unpack the dictionary we use tow *(**)
print(total(**coins), "kunts")

def f(*args, **kwargs):
    print("positional:", args)

f(100,50,25)

def f(*args, **kwargs):
    print("named:", kwargs)

f(galleons=100,sickles=50,kunts=25)