#STRINGS AND STRING SLICING
b="!!Hello I am Ashu!\n Kumar2808!!!"

print(b[0])
print(b[-1])
for i in b: #to print char by char
    print(i)
print(len(b)) #len()-gives the length of the string
for i in "Ashutosh":
    print(i)

print(b[:5])
print(b[0:-1])
print(b[2:])
print(b[-5:-1])
print(b[0::2]) #(start:end-1:step)
print(b[::-1]) #REVERSE
print(b.lower()) 
print(b.upper())
print(b.rstrip("!")) #removes only trailing
print(b.replace("Ashu","Ashutosh" ))
d="Hello I !am \nAshu2808"
print(d.split("!")) #Split it into different list

print(d.capitalize()) #Onlu capitalizes 1st char all other lowercase
print(d.center(24)) 
print(d.center(25,".")) #Add "." before and after the string
print(d.count("A"))
print(d.endswith("."))
print(d.endswith("u",13,17))
print(d.startswith("H"))
print(d.find("Ashu")) #finds index of first if not gives -1
print(d.index("")) #finds index of first if not gives error
print(d.isalnum()) #A-Z,0-9,a-z
print(d.isprintable()) #non printable \n
print(d.isalpha()) #A-Z,a-z
print(d.isspace()) #whitespaces
print(d.istitle()) #every word first capital
print(d.title()) #makes title
print(d.swapcase()) #lower to upper vice-versa
print(d.casefold()) #convert all to lower

age=20
b="Hello, Ashu {}"
print(b.format(age))

n=input("Enter the string:")
if (n>n[:3]):
    print(n[:2]+n[-2:])
else:
    print("Empty string")

mystr=input("Enter the string:")
count=0
for i in mystr:
    print(i)
    count=count+1
print("The length of string:",count)
print("The length of string:",len(mystr))
print(mystr.casefold()) #convert all to lowercase