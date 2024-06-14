
INSERT_STORE = """
    INSERT INTO store (id, name)
    VALUES (:id, :name) ON CONFLICT (id) DO UPDATE SET name = :name;
"""

GET_STORE_BY_ID = """
    SELECT id, name FROM store WHERE id = :id
"""

GET_STORE_INGREDIENTS = """
    SELECT id FROM ingredients WHERE store_id = :id
"""