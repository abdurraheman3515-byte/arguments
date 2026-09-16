def fabonacii(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        f=fabonacii(n-1)+fabonacii(n-2)
        return f

for i in range(10):
    
  print(fabonacii(i))    

