### ✅ 1. **Calculator (Kalkulyator)**

#**🧠 Vazifa**: Foydalanuvchi ikkita son va amal kiritadi (`+`, `-`, `*`, `/`). Siz tegishli natijani hisoblab chiqaring.

def add(a , b):
    result = a + b
    return result

def subtract(a , b):
    result = a - b
    return

def multiply(a , b):
    result = a * b
    return result

def divide(a , b):
    result = a / b
    return result

a = int(input("Raqam kiriting!: "))
op = str(input("Amalni kiriting!: "))
b = int(input("Raqam kiriting!: "))

def main():

    if op == "+" :
        print(add(a , b))

    elif op == "-":
        print(subtract(a , b))
    
    elif op == "*":
        print(multiply(a , b))
    
    elif op == "/":
        if b == 0:
            print("Nolga bo'lib bo'lmaydi!")
        else:
            print(divide(a , b))
    
    else:
        print("Noto'g'ri amal kiritildi!")
        
main()