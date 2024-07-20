def age_program():
    second_or_years=input('Give me seconds (s) or years (y): ')
    if second_or_years=='s':
        #convert seconds to years
        user_value=input('Enter the number of seconds you have lived for: ')
        res=int(user_value)/(365*24*60*60)
        print('You have {} years old'.format(int(res)))
    elif second_or_years=='y':
        user_value=input('Enter the number of years: ')
        res=int(user_value)*365*24*60*60
        print('You have lived for {} seconds.'.format(int(res)))
    else:
        return 'wrong input'
    return 999

age_program()