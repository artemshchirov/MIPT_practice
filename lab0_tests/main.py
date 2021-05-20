import fib


def main():
    n = int(input("Input your Fibonacci number: "))
    f = fib.fib(n)
    print("Your Fibonacci number:", f)


if __name__ == "__main__":
    main()