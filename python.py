

original_list = [1, 2, 3, 4]
reversed_list = original_list[::-1]
print(reversed_list)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = 6
result = factorial(num)
print(result)

with open('fichier.txt', 'r') as file:
    content = file.read().replace('\n', ' ')
print(content)

word = "alternance"
alternating_case_word = ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(word))
print(alternating_case_word)

num_list = [10, 23, 45, 30, 15, 8, 50, 7]
divisible_by_5 = [num for num in num_list if num % 5 == 0]
print(divisible_by_5)

def replace_element(lst, target, replacement):
    for i in range(len(lst)):
        if isinstance(lst[i], list):
            replace_element(lst[i], target, replacement)
        elif lst[i] == target:
            lst[i] = replacement

list1 = [5, [10, 15, [20, 25, [30, 58], 40], 45], 50]
replace_element(list1, 58, 5800)
print(list1)

