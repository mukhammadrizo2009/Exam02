### ✅ 6. **Baholar tizimi**

#**🧠 Vazifa**: Talabalar ro‘yxati `dict` tarzida berilgan. O‘rtacha bahoni hisoblang.
#o'rtacha balldan yuqori baho olgan talabalarni chiqarish kerak.

students = {'Ali': 5, 'Vali': 4, 'Hasan': 5, 'Husan': 3}
total = 0
for i in students:
    result = (students[i])
    total += result
    
average = total / len(students)
print(f"O'rtacha ball {average}!")

for i in students:
    result = (students[i])
    if result > average:
        print(f"O'rtachadan yuqori {i} - {result}")