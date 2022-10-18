
def bisiesto(year):
    if (year % 400) == 0:
        print(year, "es un ano bisiesto") 
    elif (year % 4 == 0)  and (year % 100 != 0):
        print (year, 'es una ano bisiesto')
    else:
        print(year, ' no es un ano bisiesto')

bisiesto(2024)

    

    
    

