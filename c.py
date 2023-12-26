#1. Function defination is one time process
def myFunction(**formalargument):
    
    for key, value in formalargument.items():
        print(f"{key}: {value}")
    pass

#2. Function calling/invoking is many time process
myFunction(name="Vishal", city='Neemuch', age='''14''' )