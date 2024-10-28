"""
     *
    ***
   *****
  *******
 *********
  *******
   *****
    ***
     *
"""

def print_diamond(n):
    
    # Upper segment
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

    # # Lower segment
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))



print_diamond(5)