from datetime import date
import csv

dt=date.today()
dt=dt.strftime("%d/%m/%y")


filename="test.csv"
exp=[]
stopped=False

with open(filename,'a',newline="") as file:
    csvwriter=csv.writer(file)
    while not stopped:
        xp=int(input("enter the expenses(enter 0 to exit):"))
        if(xp==0):
            stopped=True
        else:
            csvwriter.writerow([dt,xp])
            exp.append(xp)
file.close()

print("Your expense are", exp)

