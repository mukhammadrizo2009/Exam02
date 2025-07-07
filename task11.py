### ✅ 11. **Ismlar soni (`Input/students.json`)**

#**🧠 Vazifa**: `students.json` faylidagi o‘quvchilar sonini hisoblang va natijani `Output/output11.json` fayliga yozing.

import json

with open('Input/students.json', 'r') as file:
    students = json.load(file)

count = len(students)


with open('Output/output12.json', 'w', ) as file02:
    json.dump({"count": count}, file02 , indent=4)

    