def even_odd_checker(num):
    if num % 2 == 0:
        return str(num) + " is even"
    else:
        return str(num) + " is odd"

def main():
    number_input = int(input("Enter a number: "))
    answer = even_odd_checker(number_input)
    print(answer)

if __name__ == "__main__":
    main()
