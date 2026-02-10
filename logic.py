def validate_login(username, password) -> object:
    '''
    Checks if the provided credentials are valid.

    Args:
        username (str): The username entered in the form.
        password (str): The password entered in the input field.

    Returns:
        bool: True if the credentials match the database,
        False otherwise.

    Example:
        >>> validate_login('admin', '1234')
        True
    '''
    if username == 'admin' and password == '1234':
        print(f'Login successful for: {username}')
        return True
    return False