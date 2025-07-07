import json

with open("Input/students.json", "r") as file01:
    students = json.load(file01)
    
    names = []
    all_names = []
    
    for name in students:
            all_names.append(name["name"])
            
    for first_name in all_names:
        if len(first_name) > 5:
            names.append(first_name)
            
result = {"long_names":(names)}
            
with open("Output/output13.json", "w") as file02:
    json.dump(result, file02, indent=4)