import pytest
# from budget.budget import *
from Income import NowyPrzychod
from Expense import NowyWydatek

def test_NowyWydatek():
    resp = NowyWydatek.add(2,"am","lidl")
    assert resp == "dodano 2"

def test_NowyPrzychod():
    resp = NowyPrzychod(1,"P",5000)
    assert resp.add() == "Styczen 5000"
