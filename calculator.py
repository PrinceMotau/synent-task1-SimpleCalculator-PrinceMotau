import os

#Clear screen terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else clear)

while True:
    clear_screen()
    
    print('Simple Calculator CLI')
    print('Type "quit" to exit\n')

    #Get a valid 1st input
    first_input = input('Enter first number:')
    if first_input.lower() == 'quit':
        print('Calculator closed.')
        break
        
    try:    
        num1 = float(first_input)

        operator = input('Enter operator(+,-,*,/):')
        if operator.lower() == 'quit':
            print('Calculator closed.')
            break

        #get valid 2nd input
        second_input = input('Enter second number:')
        if second_input.lower() == 'quit':
            print('Calculator closed.')
            break

        num2 = float(second_input)

        #Calculations
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2            
        elif operator == '*':
            result = num1 * num2        
        elif operator == '/':
            if num2 == 0:
                print('Error, Cannot devide by 0.')
                input('R to reset:')
                continue
                result = num1 / num2
        else:
            print('Invalid number.\n')
            input('R to reset:')
            continue
            
        #Present reults
        print(f'\nResults:{result}')
        
    except ValueError:
        print('Invalid operator.\n')

    #Resert console.
    input('R to reset:')
    
    


        
    