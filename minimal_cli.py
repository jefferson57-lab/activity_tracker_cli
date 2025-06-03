
def main():
    print("Hello from CLI!")
    while True:
        print("\nOptions:")
        print("1. Test")
        print("2. Exit")
        choice = input("Choose: ")
        
        if choice == '1':
            print("Working!")
        elif choice == '2':
            break

if __name__ == "__main__":
    main()