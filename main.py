def digit_sum(n):
  if (n < 10):
    return n
  else:
    last = n%10
    n = n//10
    return (digit_sum(n)) + last

def run():
  digit = int(input("Enter an int: "))
  print(f"sum of digits of {digit} is {digit_sum(digit)+digit_sum(0)}.")

if __name__ == "__main__":
  run();