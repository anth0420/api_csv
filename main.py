import csv

with open ("prueba.csv") as f:
    reader = csv.reader(f)
    for row in reader: 
        print("Ap paterno: {0}, Ap materno: {1}, Nombre: {2}, Ciudad: {3}".format(row[0], row[1],row[2], row[3]))