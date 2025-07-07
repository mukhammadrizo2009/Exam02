import json

with open("Input/students.json", "r") as file01:
    students = json.load(file01)
    
names = [name["name"] for name in students]

result = list(filter(lambda x: x[0].upper() == "A", names))

result = {"a_names": result}
    
print(result)