n = input()
print('Yes' if len(str(n)) == len(set(str(n))) else 'No')
