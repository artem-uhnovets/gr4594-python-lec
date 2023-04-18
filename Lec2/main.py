# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# list = [5, 1, 2, 1, -1, 3, 4, 4]
# count = 0
# for i in range(1, len(list)):
#     if list[i] == list[i - 1]:
#         print(i)
#         break
#     count += 1
# print(count)

# my_list = [3, 8, 1, 6, 0, 8, 4]
# list = []
# print(list)
# list = my_list.copy()
# print(list)
# odd = [1, 3, 5]
# odd.extend(list)
# odd.sort()
# print(odd)

# list = []
# number = None
# while (number: = int(input("Введите число: "))) != 0:
#     list.append(number)
# print(max(list))
list = [c + d for c in 'list' if c != 'i' for d in 'spam' if d != 'a']
print(list)
