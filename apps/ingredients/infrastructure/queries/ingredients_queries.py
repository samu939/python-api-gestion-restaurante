
GET_INGREDIENT_BY_ID = """
    SELECT ing.id, ing.name, ing.quantity
    FROM ingredients AS ing
    WHERE ing.id = :id;
"""

INSERT_INGREDIENT = """
    INSERT INTO ingredients (id, name, quantity)
    VALUES (:id, :name, :quantity) ON CONFLICT (id) DO UPDATE SET name = :name, quantity = :quantity;
"""