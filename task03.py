### ✅ 3. **Tax Calculator**

#**🧠 Vazifa**: Maoshga qarab soliqni hisoblang va sof maoshni chiqaring.

def calculate_tax(salary):
    if salary > 5_000_000:
        tax = salary*0.2
    else:
        tax = salary*0.13

    return tax



def calculate_net_salary(salary):
    net_salary = salary - calculate_tax(salary)
    return net_salary

salary = 6_000_000
tax = calculate_tax(salary)
print(f"Soliq - {tax}")

print(f"Sof Maosh - {calculate_net_salary(salary)}")