# Pattern Printing Demo (Covers: loops, conditionals, functions, recursion, list comprehension)

# -------------------------------
# 1. Pyramid Pattern
# -------------------------------
def pyramid(n):
    for i in range(1, n+1):
        print(" " * (n - i) + "* " * i)

# -------------------------------
# 2. Inverted Pyramid
# -------------------------------
def inverted_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * i)

# -------------------------------
# 3. Number Triangle
# -------------------------------
def number_triangle(n):
    for i in range(1, n+1):
        print(" ".join(str(j) for j in range(1, i+1)))

# -------------------------------
# 4. Pascal’s Triangle (Recursion)
# -------------------------------
def fact(n):  # recursive factorial
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)

def pascal(n):
    for i in range(n):
        row = [str(fact(i)//(fact(j)*fact(i-j))) for j in range(i+1)]
        print(" " * (n-i), " ".join(row))

# -------------------------------
# 5. Diamond Pattern
# -------------------------------
def diamond(n):
    for i in range(1, n+1):
        print(" " * (n - i) + "* " * i)
    for i in range(n-1, 0, -1):
        print(" " * (n - i) + "* " * i)

# -------------------------------
# 6. Recursive Right Triangle
# -------------------------------
def right_triangle(n, i=1):
    if i > n:
        return
    print("* " * i)
    right_triangle(n, i+1)

# -------------------------------
# Main Program
# -------------------------------
def main():
    n = int(input("Enter size of pattern: "))

    print("\n1. Pyramid Pattern:")
    pyramid(n)

    print("\n2. Inverted Pyramid:")
    inverted_pyramid(n)

    print("\n3. Number Triangle:")
    number_triangle(n)

    print("\n4. Pascal's Triangle:")
    pascal(n)

    print("\n5. Diamond Pattern:")
    diamond(n)

    print("\n6. Right Triangle (Recursion):")
    right_triangle(n)

if __name__ == "__main__":
    main()
