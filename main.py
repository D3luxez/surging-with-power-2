def isPowerOf8(n):
  """Checks if a given number is a power of 8.

  Args:
    n: The number to check.

  Returns:
    True if the number is a power of 8, False otherwise.
  """
  if n <= 0:
    return False
  while n % 8 == 0:
    n //= 8
  return n == 1

# Get the number from the user
number = int(input("Enter a number: "))

# Check if the number is a power of 8
if isPowerOf8(number):
  print(f"{number} is a power of 8.")
else:
  print(f"{number} is not a power of 8.")