#from replit import clear
def add(a,b):
    return a + b
def substract(a,b):
    return a - b
def divi(a,b):
    return a / b 
def multi(a,b):
    return a * b
operations={"+":add,
            "-":substract,
            "/":divi,
            "*":multi}

def calcul():
    a=int(input("type the first number: "))
    for i in operations:
        print(i)
    continu=True
    while continu:
        operation=input("choose the operation in line above: ")
        b=int(input("type the next number: "))
        calculation_function=operations[operation]
        answer1=calculation_function(a,b)
        print(f"{a} {operation} {b} = {answer1}")
        choice=input("type yes to continue calculating or not for break: ")
        # if choice=="yes":
        #     clear()
        #     a=answer1
        # else:
        #     False
        #     clear()
        #     calcul()
calcul()














































# continu=True
# while continu:
#     f_number=float(input("what's the first number: "))
#     print("+\n-\n*\n/")
#     operation=input("type an operation: ")
#     L_number=float(input(" what's the next number: "))
#     result=0
#     if operation=="+":
#         result=f_number+L_number
#     elif operation=="-":
#         result=f_number-L_number
#     elif operation=="/":
#         result=f_number/L_number
#     elif operation=="*":
#         result=f_number*L_number
#     print(result)
#     choice=input("entrer 'yes' pour continuer a faire les calculs ou 'non' pour arreter: ")
#     if choice=="yes":
#         clear()
#         continue
#     elif choice=="non":
#         print("bye bye")
#         False
#     else:
#         print("plz andika ivyo twagusavye cnk wugare app yacu")
#         continue
