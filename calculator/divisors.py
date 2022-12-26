"""Create a program that asks the user for a number and then prints out a list of all the divisors of that number."""
from time import sleep
from os import system

def main():
    system("cls")
    while True:
        num = int(input("\nEnter a number (0 to exit): "))
        if num != 0:
            divisors = Divisors(num)
            divisors.print_divisors()
        else:
            break
    print(f"Bye!")
    sleep(1)
    system("cls")


class Divisors:
    def __init__(self, num):
        self.num = num
        self.divisors = []
        self.divisors.append(self.num)
        for i in range(1, self.num):
            if self.num % i == 0:
                self.divisors.append(i)

    def print_divisors(self):
        self.divisors.sort()
        print("The divisors of", self.num, "are", self.divisors)


if __name__ == "__main__":
    main()
