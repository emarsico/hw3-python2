import math

def digit_sum(n):
  if (n < 10):
    return n
  else:
    last = n - (math.floor(n/10)) * 10
    return (digit_sum(math.floor(n/10))) + last

def run():
  digit = int(input("Enter an int: "))
  print(digit_sum(digit))

if __name__ == "__main__":
  run();
