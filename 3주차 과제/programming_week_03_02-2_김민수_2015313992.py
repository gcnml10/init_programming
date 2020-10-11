
### write inch2centi(), centi2inch(), choose_scale(), continues()
### make sure changeScale() iterate until user wants to stop


def get_number(message1):
    ### do not edit here ###
    num = input(message1)
    while not num.isdigit():
        num = input(message1)
    return int(num) 


def centi2inch():
    # get value(centimeter), change it into inch, and print it
    
    print('-centimeter to inch')
    
    ### your code here ###
    centi = get_number('input number(centimeter)');
    inch = float(centi/2.54);
    inch = round(inch,2);
    print(str(centi)+'cm -> '+str(inch)+'inch')



def inch2centi():
    # get value(inch), change it into centimeter, and print it 

    print('-inch to centimeter')
    
    ### your code here ###
    inch = get_number('input number(inch)');
    centi = float(inch * 2.54);
    centi = round(centi, 2);
    print(str(inch)+'inch -> '+str(centi)+'centi')


def choose_scale(): 
    # get 1 or 2 as input (centi to inch or inch to centi)

    print('# centimeter to inch = 1')
    print('# inch to centimeter = 2')
    
    ### your code here ###
    which = input("choose 1 or 2 :")
    while not (which == '1' or which == '2'):
        which = input("choose 1 or 2 :")
    return which



def continues():
    # ask to continue or not
    
    ### your code here ###
    yon = input('Wanna continue? (y/n)')
    while not (yon == 'y' or yon =='n' or yon =='Y' or yon =='N'):
        yon = input('Wanna continue? (y/n)')
    return yon


def changeScale():
    ### do not edit here ###
    sc = choose_scale()
    if sc == '1':
        centi2inch()
    elif sc == '2': 
        inch2centi()


# make sure changeScale() iterate until user wants to stop
def main():
    On = True
    while On:
        changeScale()
        ### your code here ###
        yon = continues()
        if (yon == 'y' or yon == 'Y'):
            On = True
        else:
            break
main()