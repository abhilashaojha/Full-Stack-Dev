def age_in_seconds():
    user_age=input('enter your age: ')
    res=int(user_age) * 365 * 24 * 60 * 60
    print("you have lived for {} seconds".format(res))

age_in_seconds()

