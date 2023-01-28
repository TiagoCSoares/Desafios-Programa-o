def knapsack(cont1, cont2, base_string, sub_string):
    if cont2 >= len(sub_string):
        return 1
    if cont1 >= len(base_string):
        return 0
    if base_string[cont1] == sub_string[cont2]:
        return knapsack(cont1 + 1, cont2 + 1, base_string, sub_string) + knapsack(cont1 + 1, cont2, base_string, sub_string)
    return knapsack(cont1 + 1, cont2, base_string, sub_string)


n = input()
n = int(n)
while(n > 0):
    base_string = input()
    sub_string = input()
    print(knapsack(0, 0, base_string, sub_string))
    n -= 1