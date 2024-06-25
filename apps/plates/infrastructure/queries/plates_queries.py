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