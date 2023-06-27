lower_letter = []
digit_7 = 0
upper_letter = []
digit_in_string = []
for letter in 'abcABC90':
    if letter.isdigit():
            digit_7 +=1
            digit_in_string.append(True)
    elif letter.islower():
            digit_7 +=1
            lower_letter.append(True)
    elif letter.isupper():
            digit_7 +=1
            upper_letter.append(True)
    else:
         break
if lower_letter and digit_7 >= 7 and upper_letter and digit_in_string:
    print('YES')
else:
    print('NO')