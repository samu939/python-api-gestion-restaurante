
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
    INSERT INTO ingredient (id, name)
    VALUES (:id, :name);
"""

GET_STORE_INGREDIENTS = """
    SELECT id, name, quantity, store_id FROM ingredients WHERE store_id = :id
"""

INSERT_INGREDIENT_INTO_STORE = """
    INSERT INTO ingredient_store(fk_ingredient, fk_store, quantity) values(:ingredient_id, :store_id, :quantity)
"""

SEARCH_BY_NAME = """
    SELECT * FROM ingredient
    WHERE LOWER(name) = LOWER(:name)
"""