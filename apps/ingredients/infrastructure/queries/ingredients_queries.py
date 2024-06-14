
GET_INGREDIENT_BY_ID = """
    SELECT ing.id, ing.name, ing.quantity, ing.store_id
    FROM ingredients AS ing
    WHERE ing.id = :id;
"""
GET_ALL_INGREDIENTS = """
    SELECT ing.id, ing.name, ing.quantity, ing.store_id
    FROM ingredients AS ing;
"""

INSERT_INGREDIENT = """
    INSERT INTO ingredients (id, name, quantity, store_id)
    VALUES (:id, :name, :quantity) ON CONFLICT (id) DO UPDATE SET name = :name, quantity = :quantity, store_id = :store_id;
"""

GET_STORE_INGREDIENTS = """
    SELECT id, name, quantity, store_id FROM ingredients WHERE store_id = :id
"""
