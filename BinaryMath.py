from operator import*


#Add two binary numbers
#Longer implimentation example

def BinaryAdd(x, y):
    
    x = str(x)
    y = str(y)
    
    maxLength = max(len(x), len(y))
    
    x = x.zfill(maxLength)
    y = y.zfill(maxLength)
    
    result = ''
    carry = 0
    
    # Traverse the string
    for i in range(maxLength - 1, -1, -1):
        r = carry
        r += 1 if x[i] == '1' else 0
        r += 1 if y[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
     
        # Compute the carry.
        carry = 0 if r < 2 else 1
     
    if carry != 0:
        result = '1' + result
        
    return result.zfill(maxLength)

#Subtract two binary numbers
#Using built in functions     

def BinarySub(x, y):
    
    result = bin(sub(int(x,2),int(y,2)))
    
    return result

#Multiply two binary numbers
#Using built in functions   
     
def BinaryMult(x, y):
    
    result = bin(mul(int(x,2),int(y,2)))
    
    return result
 
#Divide two binary numbers
#Using built in function   

def BinaryDivide(x, y):
    
    result = bin(floordiv(int(x,2),int(y,2)))
    
    return result
    