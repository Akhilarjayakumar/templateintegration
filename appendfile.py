f=open("name.txt","a")
n=int(input("enter the count "))
for x in range(n):
	name=input("enter a text ")
	name=name+"\n"
	f.write(name)
f.close()