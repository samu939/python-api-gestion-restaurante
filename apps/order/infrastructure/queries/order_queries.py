GET_ALL_ORDERS_BY_USERS = """
    SELECT
            o.id,
            o.final_price as price,
            json_agg(json_build_object('plate_id', od.fk_plate, 'quantity', od.quantity)) AS plates,
            o.order_date as date,
            o.fk_user as user_id
        FROM
            "order" as o, order_detail as od
        where 
            o.id = od.fk_order and o.fk_user = :user_id
        group by
            o.id
"""

GET_ORDER_BY_ID = """
    SELECT
            o.id,
            o.final_price as price,
            json_agg(json_build_object('plate_id', od.fk_plate, 'quantity', od.quantity)) AS plates,
            o.order_date as date,
            o.fk_user as user_id
        FROM
            "order" as o, order_detail as od
        where 
            o.id = od.fk_order and o.id = :id
        group by
            o.id
"""

INSERT_NEW_ORDER = """
    INSERT INTO "order" ( id , order_date, final_price, fk_user) values(:id, :date, :price, :user_id);
"""

INSERT_NEW_ORDER_DETAIL = """
    INSERT INTO order_detail(quantity, fk_order, fk_plate) values(:quantity, :order_id, :plate_id);
"""
