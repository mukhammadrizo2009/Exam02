### ✅ 7. **Mahsulotlar savatchasi**

#**🧠 Vazifa**: Har bir mahsulot uchun narx va miqdor berilgan. Umumiy narxni hisoblang.

sum = 0
cart = {
    'non': {'price': 3000, 'quantity': 2},
    'sut': {'price': 8000, 'quantity': 1},
    'olma': {'price': 5000, 'quantity': 5}
}
for i in cart.keys():
    a = cart[i]['price'] * cart[i]['quantity']
    sum += a

print(sum)
