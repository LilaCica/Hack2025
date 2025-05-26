with open('./input.txt', 'r') as f:
  input = f.read()

#print(input)

def fibonacci_div_by_3(n_str):
    try:
        n = int(n_str)
        if n < 0:
            return "N/A"
    except:
        return "N/A"

    a, b = 0, 1
    results = []

    while a <= n:
        if a % 3 == 0:
            results.append(str(a))
        a, b = b, a + b

    return ', '.join(results) if results else "N/A"
  
for line in input.strip().split('\n'):
    output = fibonacci_div_by_3(line.strip())
    print(output)
