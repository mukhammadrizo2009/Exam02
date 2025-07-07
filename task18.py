# 18. Sonlarni kvadratga oshirish (map + list[dict])

numbers = [
    {'value': 2}, 
    {'value': 3}, 
    {'value': 4}
]

result = list(map(lambda x:{'value': x["value"]**2}, numbers))

print(result)

