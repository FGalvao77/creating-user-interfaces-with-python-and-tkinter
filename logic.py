def validate_login(user, password) -> object:
    '''
    Docstring for validate_login
    
    :param user: Description
    :param password: Description
    '''
    if user == 'admin' and password == '1234':
        print(f'Login successful for: {user}')
        return True
    return False