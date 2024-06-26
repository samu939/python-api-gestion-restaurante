GET_ALL_PLATES = """
    SELECT
            plate.id,
            plate.name,
            plate.description,
            plate.price,
            json_agg(json_build_object('ingredient_id', ingredient_plate.fk_ingredient, 'quantity', ingredient_plate.quantity)) AS ingredients
        FROM
            plate
        JOIN
            ingredient_plate ON plate.id = ingredient_plate.fk_plate
        GROUP BY
            plate.id
"""

GET_PLATE_BY_ID = """
    SELECT
            plate.id,
            plate.name,
            plate.description,
            plate.price,
            json_agg(json_build_object('ingredient_id', ingredient_plate.fk_ingredient, 'ingredient_name', ingredient.name, 'quantity', ingredient_plate.quantity)) AS ingredients
        FROM plate, ingredient_plate, ingredient
        WHERE ingredient_plate.fk_ingredient = ingredient.id
		AND ingredient_plate.fk_plate = plate.id
		AND plate.id = :id
        GROUP BY
            plate.id
"""

INSERT_NEW_PLATE = """
    INSERT INTO plate("id" ,"name", description, price) values(:id, :name, :description, :price);
"""
INSERT_NEW_PLATE_INGREDIENTS = """
    INSERT INTO ingredient_plate(quantity, fk_plate, fk_ingredient) values(:quantity, :plate_id, :ingredient_id);
"""