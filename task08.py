### ✅ 8. **Yig‘indi (`Input/numbers.txt`)**

#**🧠 Vazifa**: `Input/numbers.txt` faylida berilgan sonlar yig‘indisini hisoblang va `Output/output08.txt` fayliga yozing.


with open("Input/numbers.txt", "r+") as file:
    result = file.read()
    
    result01 = [int(num) for num in result.split()]
    
    total = sum(result01)
    
with open("Output/output08.txt","w") as file02:
    file02.write(f"Natija: {str(total)}")