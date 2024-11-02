f = open("checker.py", "w")

desc = input("Enter description: ")
n = int(input("Enter number of questions: "))
print()

f.write(f"""def no():
    print('Wrong answer!', flush=True)
    exit()

print('{desc}\\n', flush=True)

print('Answer the following question:', flush=True)

""")

for i in range(n):
    q = input(f"Enter question {i+1}: ")
    a = input(f"Enter answer {i+1}: ")
    print()
    f.write(f"""print('\\n{i+1}. {q}', flush=True)
print('>> ', end='')
if input() != '{a}':
    no()

""")

flag = input("Enter flag: ")
f.write(f"print('\\nGreat job! Here is your flag: {flag}', flush=True)")

print('\nchecker.py has been created')

f.close()