
try:
    num = int('abc')

except (ValueError, TypeError) as e:
    print(e)

