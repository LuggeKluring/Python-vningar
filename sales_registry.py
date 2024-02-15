import csv
import matplotlib as plot
import numpy as np
from prettytable import PrettyTable

sales_dir = 'sales.csv'
salesmen_dir = 'salesmen.csv'

salesmen = []
sales = []

#with open(salesmen_dir, 'r') as salesmen_file:
#    reader = csv.reader(salesmen_file, delimiter=',')
#    for row in reader:
#        list_salesmen.append(row)
"""with open(sales_dir, 'r') as sales_file:
    reader = csv.reader(sales_file, delimiter=",")
    for row in reader:
        sales.append(row)"""
        
def main():
    print("Dunder Mifflin Paper Company -- Sales registry")
    print(" ")
    print("1. Register new sale")
    print("2. List sales by period")
    print("3. Register salesman")
    
    run_function = int(input("Ange funktionsnummer: "))
    
    if run_function == 1:
        sale = [2, int(input('Ange produktnummer: ')), int(input('Ange kvantitet: ')), float(input('Ange pris/enhet: ')), int(input('Ange säljar-ID: '))]
        register_sale(sale)
    elif run_function == 2:
        list_sales()
    elif run_function == 3:
        register_salesman()
        
        
def register_sale(sale):
    with open(sales_dir, 'a', newline='') as sales_file:
        writer = csv.writer(sales_file, delimiter=',')
        writer.writerow(sale)
    main()
    
def list_sales():
    sales_table = PrettyTable()
    with open(sales_dir, 'r+') as sales_file:
        csv_reader = csv.reader(sales_file, delimiter=',')
        for row in csv_reader:
            sales.append(row)
    sales_table.field_names = sales[0]
    sales.pop(0)
    for row in sales:
        sales_table.add_row(row)
    
    print(sales_table)
    main()
    
def register_salesman():
    
    
    main()
    
main()