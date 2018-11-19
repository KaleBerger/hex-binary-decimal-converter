#Conversion Functions#

def dtb():
    n=int(input("please enter the number you want to convert: "))
    x=n
    k=[]
    while (n>0):
        a=int(float(n%2))
        k.append(a)
        n=(n-a)/2
    k.append(0)
    string=""
    for j in k[::-1]:
        string=string+str(j)
    print('The binary conversion for %d is %s' %(x, string))
    
def btd():
    binary = input('Enter a binary number : ')
    decimal = int(binary, 2)
    print('The decimal number is : ', decimal)

def dth():
    def changeDigit(digit):
        decimal = [10 , 11 , 12 , 13 , 14 , 15 ]
        hexadecimal = ["A", "B", "C", "D", "E", "F"]
        for counter in range(7):
            if digit == decimal[counter - 1]:
                digit = hexadecimal[counter - 1]
        return digit
    
    result = int(input("Enter a whole number to be converted to hexadecimal: "))
    hexadecimal = ""
    while result != 0:
        remainder = changeDigit(result % 16)
        hexadecimal = str(remainder) + hexadecimal
        result = int(result / 16)
    print("The hex value is 0x", hexadecimal)
    
def htd():
    hexadecimal = input("Enter a hexidecimal number to convert to a decimal (No 0x !): ")
    print("The decimal value is", int(hexadecimal, 16))

def bth():
   binary = input("Enter number in Binary Format: ")
   temp = int(binary, 2)
   print(binary,"in Hexadecimal =",hex(temp)[2:],"\n")
   
def htb():
    hexadecimal = input("Enter your hex value (No 0x !): ")
    a = int(hexadecimal, 16)
    print("First we convert it to a decimal!, the decimal is", a)
    n=int(input("Now enter the decimal number above: "))
    x=n
    k=[]
    while (n>0):
        a=int(float(n%2))
        k.append(a)
        n=(n-a)/2
    k.append(0)
    string=""
    for j in k[::-1]:
        string=string+str(j)
    print('The binary conversion for %d is %s' %(x, string))
    
    
    
    
        