#Possitional Arguments
'''
def calculat_result(name,roll,marks):
    print(name)
    print(roll)
    print(marks)

calculat_result("Ali","45",[80,65,98,45,68,78])    
'''
#keyword Argument
'''
def calculat_result(name,roll,marks):
    print(name)
    print(roll)
    print(marks)

calculat_result(roll="45",marks=[80,65,98,45,68,78],name="Ali")  
'''


#Arbitrary Argument
'''
def class_Average(std,*marks):
    print(std)
    print(sum(marks)/len(marks))

class_Average(11,85,96,78,98,56)

'''
#keyword Arbitrary Argument
'''
def display_landmarks(country,**p):
	print(country)
	print(p)


display_landmarks("India",longitude=74.52,latitude=36.52,city="Pune",Sea_Level=745.0)
'''


'''
# keyword Arbitrary Argument

def class_Average(schoolname,**Average):
    print(schoolname)
    print(Average)

class_Average("MHS",first=85,second=96,therd=78,fourth=98,fifth=56)
'''
'''
#default argument
def data(a,b,c=150):
    print(a)
    print(b)
    print(c)

data(50,100)
'''


