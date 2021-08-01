from connection import get_sql_connection


def get_all_products(cnx):
    cursor = cnx.cursor()
    query = """select product.product_id, product.name, product.unit_id,units.unit_name, 
        product.price_per_unit from product
        inner join units on product.unit_id = units.unit_id;"""
    cursor.execute(query)
    response = []
    for (product_id, name, unit_id, unit_name, price_per_unit) in cursor:
        response.append({
            'product_id': product_id,
             'name': name, 
             'unit_id':unit_id,
             'unit_name':unit_name,
             'price_per_unit':price_per_unit
        })
    return response

def insert_product(cnx, data):
    cursor = cnx.cursor()
    query = """insert into product (name, unit_id, price_per_unit) 
            values (%s, %s, %s)"""
    product = (data['name'], data['unit_id'], data['price_per_unit'])
    cursor.execute(query, product)
    cnx.commit()
    return cursor.lastrowid


def delete_product(cnx, product_id):
    cursor = cnx.cursor()
    query = ("delete from product where product_id=" + str(product_id))
    cursor.execute(query)
    cnx.commit()
    return cursor.lastrowid

if __name__ == '__main__':
    cnx = get_sql_connection()
    rep = get_all_products(cnx)
    print(rep)
    print("===============================")
    print(insert_product(cnx, {'name':'pista', 'unit_id':1, 'price_per_unit':435}))
    print("===============================")
    rep = get_all_products(cnx)
    print(rep)
    print("===============================")
    print(delete_product(cnx, 2))
    print("===============================")
