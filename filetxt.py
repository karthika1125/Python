                    #   File Handling

                     # txt file

# f=open("demofile.txt","x")   # create file - x

# f=open("demofile.txt","w")    # write a file -w
# f.write("My name is karthika")
# f.close()

# f=open("demofile.txt","r")     # read file - r
# print(f.read())

# f=open("demofile.txt","r")       # read by line using index
# print(f.read(8))

# f=open("demofile.txt","r")      # read line 
# print(f.readline())

# f=open("demofile.txt","a")                   # adding line, append - a
# f.writelines(["\n I am from Kottayam","\n My fav color black"])
# f.close()


                            # CSV files

# import csv
# # with open("text.csv","w",newline="") as f:
# #     writer=csv.writer(f)
# #     writer.writerow(["name", "age", "place"])
# #     writer.writerow(["karthu", "4",  "ktm"])
# #     writer.writerow(["sidx",   "5",   "ekm"])


# f=open("text.csv","r")
# reader=csv.reader(f)
# for i in reader:
#     print(i)


                    # Zipfile
import zipfile
# with zipfile.ZipFile("C:/Users/HP/OneDrive/Desktop/python1/text.zip","w")as f:
#     f.write("C:/Users/HP/OneDrive/Desktop/python1/file.1.txt")
#     f.write("C:/Users/HP/OneDrive/Desktop/python1/file2.txt")      

                                    # zipfile read

# with zipfile.ZipFile("C:/Users/HP/OneDrive/Desktop/python1/text.zip","r")as f:
#     f.extractall("extracted")                                    


with zipfile.ZipFile("C:/Users/HP/OneDrive/Desktop/python1/text.zip","r")as f:
    f.extractall("extracted")
    list1=f.namelist()
    print(list1)