filename1="trace1.out"
filename2="trace7.out"
with open(filename1,mode="r") as f1:
    with open(filename2,mode="r") as f2:
        line1=f1.readlines()
        line2=f2.readlines()
        for i in range(len(line1)):
            a1=line1[i].split(None,maxsplit=2)[-1]
            a2=line2[i].split(None,maxsplit=2)[-1]
            
            with open("n1.txt",mode="a") as ff1:
                ff1.write(a1)
            with open("n2.txt",mode="a") as ff1:
                ff1.write(a2)

