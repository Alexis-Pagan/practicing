#==============================================================================
# simple calculator using Python
# Made by: Alexis.I
# PLACE: Puerto Rico, Vega Alta
# Day: Jan 1, 2018
#==============================================================================
class Calculator():
    #attributes of class
    num1 = 0
    num2 = 0

    def userOptions(self):
        print('Select an option\n')
        print('1. Add numbers\n')
        print('2. Sub numbers\n')
        print('3. Mult numbers\n')
        print('4. Div numbers\n')
        print('5. Close calculatorX\n')
       
    def ifUserChoose(self):
        enter = int(input('Choose an option from menu: '))
        option = enter
        if(option == 1):
            self.add()
        elif(option == 2):
            self.sub()
        elif(option == 3):
            self.mult()
        elif(option == 4):
            self.div()
        elif(option == 5):
            print('Calculator turning... off')
        
    def add(self):
        self.num1 = int(input('Enter first number: \n'))
        self.num2 = int(input('Enter second number: \n')) 
        
        print('\nResult: ' + str(self.num1 + self.num2))
        return
        
    def sub(self):
        self.num1 = int(input('Enter first number: \n'))
        self.num2 = int(input('Enter second number: \n')) 
        
        print('\nResult: ' + str(self.num1 - self.num2))
        
    def mult(self):
        self.num1 = int(input('Enter first number: \n'))
        self.num2 = int(input('Enter second number: \n')) 
        print('\nResult: ' + str(self.num1 * self.num2))
    
    def div(self):
        self.num1 = int(input('Enter first number: \n'))
        self.num2 = int(input('Enter second number: \n')) 
        print('\nResult: ' + str(self.num1 / self.num2))
        
#==============================================================================
# create an object of class Calculator 
#==============================================================================
object = Calculator()
#==============================================================================
# -------------------
#==============================================================================

menu = object.userOptions()

object.ifUserChoose()