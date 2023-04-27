def triangle_of_symbols(symbol, height):
    for i in range(height):
        for j in range(height - i - 1):
            print(" ", end = "")
        
        for j in range(2 * i + 1):
            print(symbol, end = "")
        
        print()


def main():
    print("Print a solid triangle of symbols")
    height = int(input("Please enter the height of the triangle: "))
    symbol = input("Please enter the symbol of the triangle: ")
    triangle_of_symbols(symbol, height)

if __name__ == "__main__":
    main()