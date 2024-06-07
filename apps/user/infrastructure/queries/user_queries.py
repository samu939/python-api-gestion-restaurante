GET_USER_BY_USERNAME = """
    SELECT us.id, us.name, us.username, us.password, us.role
    FROM users AS us
    WHERE username = :username;
"""