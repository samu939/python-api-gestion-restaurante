GET_ALL_PLATES = """
    SELECT
    plate.id,
    plate.name,
    plate.description,
    plate.price,
    COALESCE(json_agg(
        json_build_object('ingredient_id', ingredient.id, 'ingredient_name', ingredient.name, 'quantity', ingredient_plate.quantity)
    ) FILTER (WHERE ingredient.id IS NOT NULL), '[]') AS ingredients
    FROM
        plate
    LEFT JOIN
        ingredient_plate ON ingredient_plate.fk_plate = plate.id
    LEFT JOIN
        ingredient ON ingredient_plate.fk_ingredient = ingredient.id
    GROUP BY
        plate.id
"""

GET_PLATE_BY_ID = """
    SELECT
    plate.id,
    plate.name,
    plate.description,
    plate.price,
    COALESCE(json_agg(
        json_build_object('ingredient_id', ingredient.id, 'ingredient_name', ingredient.name, 'quantity', ingredient_plate.quantity)
    ) FILTER (WHERE ingredient.id IS NOT NULL), '[]') AS ingredients
    FROM
        plate
    LEFT JOIN
        ingredient_plate ON ingredient_plate.fk_plate = plate.id
    LEFT JOIN
        ingredient ON ingredient_plate.fk_ingredient = ingredient.id
    WHERE
        plate.id = :id
    GROUP BY
        plate.id

"""

INSERT_NEW_PLATE = """
    INSERT INTO plate("id" ,"name", description, price) values(:id, :name, :description, :price);
"""
INSERT_NEW_PLATE_INGREDIENTS = """
    INSERT INTO ingredient_plate(quantity, fk_plate, fk_ingredient) values(:quantity, :plate_id, :ingredient_id);
"""

UPDATE_PLATE = """
    UPDATE plate
    SET price = :price
    WHERE id = :id
"""

DELETE_PLATE_INGREDIENTS = """
    DELETE FROM ingredient_plate
    WHERE fk_plate = :id;
"""