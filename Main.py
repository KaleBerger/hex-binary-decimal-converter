#######################################
#Kale Berger
#Conversion Program using OOP
#Start: November 13, 2018
#######################################
import Conversions as C


class conversions():
    def loop():
        convert = input ("Would you like to make a conversion? y/n: ")
        while convert == "y":
            conversion = input ("""You can choose from 6 conversions:
Decimal to Binary (type: DTB)
Binary to Decimal (type: BTD)
Decimal to Hexidecimal (type: DTH)
Hexidecimal to Decimal (type: HTD)
Binary to Hexidecimal (type: BTH)
Hexidecimal to Binary (type: HTB)

Which do you choose?

: """)
            if conversion == "DTB":
                C.dtb()
                convert = input ("Make another conversion? y/n: ")
            if conversion == "BTD":
                C.btd()
                convert = input ("Make another conversion? y/n: ")
            if conversion == "DTH":
                C.dth()
                convert = input ("Make another conversion? y/n: ")
            if conversion == "HTD":
                C.htd()
                convert = input ("Make another conversion? y/n: ")
            if conversion == "BTH":
                C.bth()
                convert = input ("Make another conversion? y/n: ")
            if conversion == "HTB":
                C.htb()
                convert = input ("Make another conversion? y/n: ")
                
            
                 
conversions.loop()
    
                
                
            


        
        
        
    