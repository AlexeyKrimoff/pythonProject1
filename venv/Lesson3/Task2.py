
def pers_data():
    #dict = (name,surname, year, city, email, tel)
    user_name = input('Enter name - ')
    user_surn = input('Enter surname - ')
    user_year = input('Enter year of birth - ')
    user_city = input('Enter name of city - ')
    user_email = input('Enter your e-mail - ')
    user_tel = input('Enter your telephone number - ')
    str = (user_name, user_surn, user_year, user_city, user_email, user_tel)
    return str
print(f'User data is - ',pers_data())