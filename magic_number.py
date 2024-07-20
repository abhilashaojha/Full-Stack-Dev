def user_input():
    magic_no=8
    user_value=int(input("Enter a number between 0 and 10: "))
    if user_value==magic_no:
        print("You won")
    else:
        user_input()
    return magic_no

user_input()



