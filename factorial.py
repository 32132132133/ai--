def factorial(n):
  if n == 0:
    return 1
  else:
    result = 1
    for i in range(1, n + 1):
      result *= i
    return result

n = int(input("n 값을 입력하세요: "))
print(f"{n}!은 {factorial(n)}입니다.")