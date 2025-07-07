### ✅ 12. **Ismlarni alfavit bo‘yicha tartiblash (`Input/students.json`)**

#**🧠 Vazifa**: `students.json` faylidagi barcha `name` maydonlarini alfavit bo‘yicha tartiblang va `Output/output12.json` fayliga yozing.


import json

with open("Input/students.json", "r") as file01:
    students = json.load(file01)
    
    names = []
    for name in students:
        names.append(name["name"])

    result = {"sorted_names": sorted(names)}

    
with open("Output/output12.json", "w") as file02:
    json.dump(result, file02, indent=4)
