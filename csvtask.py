import csv
with open("data.csv","w",newline="")as f:
    writer=csv.writer(f)
    writer.writerow(["Name"     , "Age" , "Grade"])
    writer.writerow(["karthika" , "23"  ,    "A"])
    writer.writerow(["Anu"      , "20"  ,    "A+"])
    writer.writerow(["kavya"    , "21"  ,    "B+"])
    f=open("data.csv","r")
    reader=csv.reader(f)
    for i in reader:
        print(i)