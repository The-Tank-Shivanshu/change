def change():
    fileName=input("enter your file name")
    file11=open(file1.txt,"r")
    file22=open(file2.txt,"r")
    file1=open(file1.txt,"w")
    with open(file1,'w') as a:
        a.write(file11)
change()