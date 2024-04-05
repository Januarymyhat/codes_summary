two_type_string = input()
# KMP?
pin = 0
groups = 0
x_num = 0
y_num = 0

while pin < len(two_type_string):
    if two_type_string[pin] == 'X':  # string[5]就是第五个字符，包括括号
        x_num += 1
    else:
        y_num += 1

    if x_num == y_num:
        groups += 1
        x_num = 0
        y_num = 0

    pin += 1

print(groups)
