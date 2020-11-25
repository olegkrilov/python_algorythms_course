"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел
в диапазоне от 2 до 9. Примечание: 8 разных ответов.
"""

min_val = 2
max_val = 99
results = {j: 0 for j in range(min_val, (max_val // 10) + 1)}

for key in results.keys():
    for i in range(min_val, max_val + 1):
        if not i % key:
            results[key] += 1

print(results)
