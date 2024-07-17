def get_uoms(connection):
    cursor = connection.cursor()
    query = ("select * from unit_of_measure")
    cursor.execute(query)
    response = []
    for (unit_id, unit_name) in cursor:
        response.append({
            'uom_id': unit_id,
            'uom_name': unit_name
        })
    return response


if __name__ == '__main__':
    from sql_connection import get_sql_connection

    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(get_uoms(connection))