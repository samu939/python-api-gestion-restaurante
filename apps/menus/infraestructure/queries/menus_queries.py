GET_ALL_MENUS = """
    SELECT menu.id, menu.name, json_agg(json_build_object('plate_id', menu_plate.fk_plate)) as plates
    FROM menu, menu_plate
    WHERE menu.id = menu_plate.fk_menu
    GROUP BY menu.id
"""

GET_MENU_BY_ID = """
    SELECT menu.id, menu.name, json_agg(json_build_object('plate_id', menu_plate.fk_plate)) as plates
    FROM menu, menu_plate
    WHERE menu.id = menu_plate.fk_menu
    AND menu.id = :id
    GROUP BY menu.id
"""

INSERT_MENU = """
    INSERT INTO menu(id, name) values(:id, :name)
"""

INSERT_PLATE_MENU = """
    INSERT INTO menu_plate(fk_plate, fk_menu) values(:plate_id , :menu_id)
"""