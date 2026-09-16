'''
#possitional and keyword

def data(a,b,c,d):
    print(a)
    print(b)
    print(c)
    print(d)

data(50,60,c=70,d=80)    
'''

#============================================================================================================================
'''
#possitional and Arbitrary

def data(a,b,*c):
    print(a)
    print(b)
    print(c)


data(10,20,30,40,50,60,70,80)
'''
#=============================================================================================================================

'''
#possitional and keyword Arbitrary


def class_Average(a,schoolname,**Average):
    print(a)
    print(schoolname)
    print(Average)

class_Average(12,"MHS",first=85,second=96,therd=78,fourth=98,fifth=56)

'''

#==============================================================================================================================

'''
#possitional and default

def data(a,b,c=30):
    print(a)
    print(b)
    print(c)


data(10,20)

'''
#==============================================================================================================================
'''
#keyword and default

def data(a,b,c=100):
    print(a)
    print(b)
    print(c)

data(a=10,b=50)

'''

#==============================================================================================================================
'''
#keyword and keyword Arbitrary
def class_Average(a,b,**Average):
    print(a)
    print(b)
   
    print(Average)

class_Average(a=12,b=24,first=85,second=96,therd=78,fourth=98,fifth=56)

'''
