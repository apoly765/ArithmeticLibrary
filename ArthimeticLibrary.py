def mathit(type,x,y):
  try:

    x_float = float(x);
    y_float = float(y);
    type = type.upper()

    if type == 'ADD':
      result = x_float + y_float   
    elif type == 'SUB':
       result = x_float - y_float   
    elif type == 'MULT':
       result = x_float * y_float 
    elif type == 'DIV': 
       result = x_float / y_float  
    
    return str(result)

    print("Result: ",result)
  except ValueError:
    print("Invalid input(s)")
    return
  