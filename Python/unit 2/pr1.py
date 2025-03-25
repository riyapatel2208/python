def get_divisors(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return divisors

def is_perfect(num):
    divisors = get_divisors(num)
    return sum(divisors) == num, divisors

user_input = input("Enter a single number or a range (start,end): ")

if ',' in user_input:
    start, end = map(int, user_input.split(','))
    
    for num in range(start, end + 1):
        perfect, divisors = is_perfect(num)
        if perfect:
            print(f"{num} is a perfect number. Divisors: {divisors}")
else:
    num = int(user_input)
    perfect, divisors = is_perfect(num)
    if perfect:
        print(f"{num} is a perfect number. Divisors: {divisors}")
