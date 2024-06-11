
GET_INGREDIENT_BY_ID = """
    SELECT ing.id, ing.name
    FROM ingredients AS ing
    WHERE ing.id = :id;
"""