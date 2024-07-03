GET_USER_BY_USERNAME = """
    SELECT us.id, us.name, us.username, us.password, us.role
    FROM "user" AS us
    WHERE us.username = :username;
"""

GET_USER_BY_ID = """
    SELECT us.id, us.name, us.username, us.password, us.role
    FROM "user" AS us
    WHERE us.id = :id;
"""

ADD_USER = """
    INSERT INTO "user" (id, username, password, name, role)
    VALUES (:id, :username, :password, :name, :role);
"""