def generate_star_pattern(rows):
    for i in range(1, rows + 1):
        print("*" * i)

def main():
    print("Welcome to the Star Program!")
    rows = int(input("Enter the number of rows: "))
    generate_star_pattern(rows)

if __name__ == "__main__":
    main()