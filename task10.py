### ✅ 10. **Tartiblash (`Input/numbers.txt`)**

#**🧠 Vazifa**: Fayldagi sonlarni tartiblang va `Output/output10.txt` fayliga yozing.

nums = []

with open("Input/numbers.txt" , "r+") as file:
    content = file.readlines()
    
    for i in content:
        number = int(i.strip())
        nums.append(number)
        
result = sorted(nums)
    
    
with open("Output/output10.txt", "w") as file02:
    
    for number in content:
        file02.write(f"{str(number)}")
