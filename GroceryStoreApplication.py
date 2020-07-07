#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  4 11:49:16 2020

@author: manideepbangaru
"""

import pandas as pd
import time
import pathlib

def Ratnadeep_open():
    OwnPwd = '1234'
    switch1 = 1
    while switch1 == 1:
        choice_1 = input('Do you want to use the app ? (y/n) : ')
        if choice_1.lower() == 'y':
#            continue
            dirToCheck = pathlib.Path('/Users/manideepbangaru/Documents/RealPythonLearn/RatnadeepDatabase/')
            if len(list(pathlib.Path.iterdir(dirToCheck))) > 1:
                Files = list(pathlib.Path.iterdir(dirToCheck))
                Times = [int(i.stem.split('_')[1]) for i in Files if i.stem!='.DS_Store']
                FileDownload = pd.read_csv(str(dirToCheck) + '/stock_%s.csv'%(max(Times)))
                
                Prods  = list(FileDownload['Products'])
                Qtys   = list(FileDownload['Quantity'])
                Prices = list(FileDownload['Price'])
                stock = {}
                for i,j,k in zip(Prods,Qtys,Prices):
                    stock[i] = {}
                    stock[i]['Quantity'] = j
                    stock[i]['Price'] = k
            else:
                stock = {}
                    
            print("---------------------------------------------------")
            print('Please select type of user')
            print('1. Owner')
            print('2. Customer')
            choice_2 = input('Enter your choice : ')
            if choice_2 == '1':
                PwdIp = input('Enter the password : ')
                if PwdIp == OwnPwd :
                    if len(list(pathlib.Path.iterdir(dirToCheck))) > 1:
                            print(FileDownload)
                    else:
                        print('Empty Stock !!!')
                    while True:
                        choice_2_1 = input('Do you want to add stock ? (y/n) : ')
                        if choice_2_1.lower() == 'y':
                            prod  = input('Enter the Product  : ')
                            qty   = input('Enter the quantity : ')
                            price = input('Enter the Price : ')
                            if prod in stock:
                                stock[prod]['Quantity'] = stock[prod]['Quantity'] + int(qty)
                                stock[prod]['Price'] = stock[prod]['Price'] + float(price)
                                ProdIndex = 0
                                for key in stock:
                                    ProdIndex += 1
                                    print('%s. %s , qty : %s, price : %s'%(ProdIndex,key,stock[key]['Quantity'],stock[key]['Price']))
                            else:
                                stock[prod] = {}
                                stock[prod]['Quantity'] = int(qty)
                                stock[prod]['Price'] = float(price)
                                print('\nFollowing are the Stock details, Enter again if anything looks wrong')
                                print('--------------------------------------------------------------------')
                                ProdIndex = 0
                                for key in stock:
                                    ProdIndex += 1
                                    print('%s. %s , qty : %s, price : %s'%(ProdIndex,key,stock[key]['Quantity'],stock[key]['Price']))
                        else:
                            Prods = list(stock.keys())
                            Qtys = [stock[i]['Quantity'] for i in Prods]
                            Prices = [stock[i]['Price'] for i in Prods]
                            timestr = time.strftime("%Y%m%d%H%M%S")
                            FileToUpload = pd.DataFrame({'Products':Prods,'Quantity':Qtys,'Price':Prices})
                            FileToUpload.to_csv('/Users/manideepbangaru/Documents/RealPythonLearn/RatnadeepDatabase/stock_%s.csv'%timestr,index=False)
                            break
            elif choice_2 == '2':
                print('\n---- Note : Enter 0 once you are done building your cart ----')
                print('\nChoose your items from below :')
                ProdIndex = 0
                for key in stock:
                    ProdIndex += 1
                    print('%s. %s , qty : %s, price : %s'%(ProdIndex,key,stock[key]['Quantity'],stock[key]['Price']))
                select = {}
                while True:
                    try:
                        chProd = int(input('Choose the Product using serial number: '))
                        if chProd > 0 and chProd <= len(stock):
                            switch = 1
                            while switch == 1:
                                try:
                                    chQty = int(input('Enter the Quantity : '))
                                    if chQty > 0 and chQty <= stock[list(stock.keys())[chProd-1]]['Quantity']:
                                        select[list(stock.keys())[chProd-1]] = {}
                                        select[list(stock.keys())[chProd-1]]['Qty'] = chQty
                                        select[list(stock.keys())[chProd-1]]['Price'] = stock[list(stock.keys())[chProd-1]]['Price'] * chQty
                                        print('You added Product:%s , Quantity:%s, Price :%s\n'%((list(stock.keys())[chProd-1]),chQty,(stock[list(stock.keys())[chProd-1]]['Price'] * chQty)))
                                        stock[list(stock.keys())[chProd-1]]['Quantity'] = stock[list(stock.keys())[chProd-1]]['Quantity'] - chQty
                                        print('Below is the Available stock\n')
                                        ProdIndex = 0
                                        for key in stock:
                                            ProdIndex += 1
                                            print('%s. %s , qty : %s, price : %s'%(ProdIndex,key,stock[key]['Quantity'],stock[key]['Price']))
                                        switch = 0
                                    else:
                                        print("Enter the quantity available in stock")
                                except:
                                    print("Enter valid Quantity")
                                        
                        elif chProd == 0:
                            print('\nBelow are the items you purchased')
                            SelIndex = 0
                            BillAmt = 0
                            for key in select:
                                SelIndex += 1
                                print('%s. %s , qty : %s, price : %s'%(SelIndex,key,select[key]['Qty'],select[key]['Price']))
                                BillAmt += select[key]['Price']
                            pay = input('Please pay Bill Amount Rs %s : '%BillAmt)
                            print('Thank you for shopping with us !!!')
                            break
                        else:
                            print("Enter the correct line number of your product")
                    except:
                        print("Enter valid serial number")
        else:
            try:
                Prods = list(stock.keys())
                Qtys = [stock[i]['Quantity'] for i in Prods]
                Prices = [stock[i]['Price'] for i in Prods]
                timestr = time.strftime("%Y%m%d%H%M%S")
                FileToUpload = pd.DataFrame({'Products':Prods,'Quantity':Qtys,'Price':Prices})
                FileToUpload.to_csv('/Users/manideepbangaru/Documents/RealPythonLearn/RatnadeepDatabase/stock_%s.csv'%timestr,index=False)
                switch1 = 0
            except:
                switch1 = 0
        

Ratnadeep_open()