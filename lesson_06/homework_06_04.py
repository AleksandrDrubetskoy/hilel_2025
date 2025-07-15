from collections import Counter

def sum_doubles (list_with_doubles_val):
    total_sum = 0
    list_unique_values = []
    for i in list_with_doubles_val:
        if i not in list_unique_values:
            amount_i = list_with_doubles_val.count(i)
            if amount_i > 1:
                total_sum += i * amount_i
            list_unique_values.append(i)
    return total_sum

def sum_doubles_2 (list_with_doubles_val):
    list_counter_uniq_val = Counter(list_with_doubles_val)
    total_sum = 0
    for i, j in list_counter_uniq_val.items():
        if j > 1:
            total_sum += int(i*j)
    return total_sum

def sum_doubles_only (list_with_doubles_val):
    list_counter_uniq_val = Counter(list_with_doubles_val)
    total_sum = 0
    for i, j in list_counter_uniq_val.items():
        if j % 2 == 0: # only for even doubles, like (a & a) or (a, a, a, a), etc. Doubles (a, a, a) is uneven.
            total_sum += int(i*j)
    return total_sum

my_list = [0, 1, 2, 2, 1, 10, 5, 6, 2, 4, 5, 10]

print(sum_doubles(my_list))
print(sum_doubles_2(my_list))
print(sum_doubles_only(my_list))
