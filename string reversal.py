def  string_reverse(str):
    return str[::-1]
 

while True:
    str = input("Enter the string:")
    reverse_str = string_reverse(str)
    print(reverse_str)

    continue_choice = input("Want to reverse another string ? (yes to continue,no to exit):").strip().lower()
    if continue_choice != "yes":
        print("Exiting the string reverser ......... Goodbye!")
        break