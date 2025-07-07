# ✅ 9. **Eng katta son (`Input/numbers.txt`)**

#**🧠 Vazifa**: Fayldagi eng katta sonni toping va `Output/output09.txt` fayliga yozing.

with open("input/numbers.txt","r+") as file:
    content = file.readlines()
    
    result_max = max(content , key=int)
    
with open("Output/output09.txt","w") as file02:
    file02.write(f"Eng katta son - {str(result_max)}")