#creating csv file:
import csv
f=open("input1.csv","w",newline="")
wo=csv.writer(f) 
wo.writerow(["Name","rollno","marks"]) 
while True:
    n=input()
    r=int(input()) 
    m=int(input()) 
    det=[n,r,m]
    wo.writerow(det) 
    ch=input("more:") 
    if ch in "Nn": 
        break 
f.close()

#csv to json:
import json
f1=open("input1.csv","r")
data=list(csv.reader(f1))
f2=open("output1.json","w")
json.dump(data,f2) 
f1.close()
f2.close()