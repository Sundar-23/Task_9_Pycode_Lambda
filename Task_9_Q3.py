#Question-3
#Create a Fibonacci series from 1 to 50 elements

def fibonacci(n):
    # fibonacci series upto n elements
  a, b = 0, 1
  result = []
  for _ in range(n):
    result.append(a)
    a, b = b, a + b
  return result

print(fibonacci(50))