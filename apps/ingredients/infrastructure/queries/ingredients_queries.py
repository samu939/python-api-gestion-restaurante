
GET_INGREDIENT_BY_ID = """
    SELECT ing.id, ing.name, ing_store.quantity, ing_store.fk_store as store_id
    FROM ingredient AS ing, ingredient_store AS ing_store
	WHERE ing.id = ing_store.fk_ingredient
	AND ing.id = :id;
"""
GET_ALL_INGREDIENTS = """
    SELECT ing.id, ing.name, ing_store.quantity, ing_store.fk_store as store_id
    FROM ingredient AS ing, ingredient_store AS ing_store
	WHERE ing.id = ing_store.fk_ingredient
"""

INSERT_INGREDIENT = """
    INSERT INTO ingredients (id, name, quantity, store_id)
    VALUES (:id, :name, :quantity, :store_id) ON CONFLICT (id) DO UPDATE SET name = :name, quantity = :quantity, store_id = :store_id;
"""

GET_STORE_INGREDIENTS = """
    SELECT id, name, quantity, store_id FROM ingredients WHERE store_id = :id
"""
