def user_data(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(user_data(surname='Carter', name='Serge', year='1891', city='Chicago', email='hex@mail.ru',
              telephone='+6 666 777 000'))
