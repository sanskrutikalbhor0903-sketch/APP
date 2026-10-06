#file create:
f=open("input.txt","w")
while True:
    e=input()
    f.write(e + "\n")
    ch=input("more:")
    if ch in "Nn":
        break
f.close()

#count:
f1=open("input.txt","r")
lines=f1.readlines()
print("no. of lines in the file:",len(lines)) 
f1.close()

#extracting 1st two lines writing that in the new file:
f2=open("output.txt","w") 
first_two=lines[:2] 
f2.writelines(first_two)
f2.close()
