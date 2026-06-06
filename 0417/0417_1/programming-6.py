def has_common(a, b):
    for i in a:
        if i in b:
            return True
    return False

list_a = [1, 2, 3, 4, 5, 6]
list_b = [6, 7, 8, 9, 10]

print(has_common(list_a, list_b))

# p302 6번 문제