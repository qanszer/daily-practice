# This is for logic training.

# Problem 1 - 5%
num = int(input("Enter maximum number: "))

final_list = []

for i in range(1, num):
    if i % 3 == 0 or i % 5 == 0:
        final_list.append(i)
    else:
        continue
print(final_list)




