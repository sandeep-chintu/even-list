nums=[11,22,33,44,55,66,77,88]
even_list=[]
odd_list=[]
for i in nums:
    if i % 2== 0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(f"Even List: {even_list}\nOdd List: {odd_list}")

