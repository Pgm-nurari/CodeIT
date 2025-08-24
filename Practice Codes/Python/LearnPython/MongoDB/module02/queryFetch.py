from module00.connection import checkConnectionSecond as m0c
from pymongo import collection
import pandas as pd

def queryOne(table : collection):
    query = {'email':'nurarisab6453@gmail.com'}
    for i in table.find(query):
        print(i)

def queryTwo(table: collection):
    print("List of names starting with \'S\' and letters greater than:")
    query = { 'name' : {'$gt':'S'}}  # to get the names starting with letter starting with 'S' and greater.
    for i in table.find(query):
        print(i)

def queryThree(table: collection):
    print("List of names starting with \'S\':")
    query = { 'name': { '$regex': r'^S', '$options': 'i' } }  # to get the names starting with letter starting with 'S'.
    # '$options' :'i' ==> implies take both 'S' and 's';
    for i in table.find(query):
        print(i)

def main():
    con = m0c()
    tab1 = con['mydatabase']['students']
    tab2 = con['mydatabase']['customers']

    # queryOne(table = tab1)
    queryThree(table = tab2)

if __name__=='__main__':
    main()

     