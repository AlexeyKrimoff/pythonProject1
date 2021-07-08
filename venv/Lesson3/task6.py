def int_func():
    latin_char = 'qwertyuioplkjhgfdsazxcvbnm'
    return word.title() if not set(word).difference(latin_char) else False


words = input('Enter string thrue the space  '). split()
for q in words:
    result = int_func(q)
    if result:
        print(int_func(q), ' ')
