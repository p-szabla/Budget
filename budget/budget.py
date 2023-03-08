from Income import NowyPrzychod
from Expense import NowyWydatek



if __name__=="__main__":      
    resp = NowyPrzychod(1,"P",5000)
    print(resp.add())
    resp2 = NowyWydatek
    print(resp2.add(2,"am","lidl"))