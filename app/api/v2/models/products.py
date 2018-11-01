from ..models import conn, cur


class ProductsDetails():

    @staticmethod
    def create_product(product_name, product_category, buying_price, selling_price, description):
        query = """ INSERT INTO products(product_name, product_category, buying_price, selling_price, description) 
                    VALUES(%s, %s, %s, %s, %s)
                """
        cur.execute(query, (product_name, product_category, buying_price, selling_price, description))
        conn.commit()
        return True

    @staticmethod
    def get_all_products():

        query = """ SELECT * FROM products """
        cur.execute(query)
        products = cur.fetchall()
        print(products)
        return products

    @staticmethod
    def get_product_by_id(id):

        query = """ SELECT * FROM products WHERE id = %s """
        cur.execute(query, (id,))

        product = cur.fetchone()
        return product


class SalesDetails():

    @staticmethod
    def create_sales(id):
        sale_info = {}

        query = """ SELECT * FROM products WHERE id = %s """
        cur.execute(query, (id,))

        product = cur.fetchone()

        if product:
            sale_info['product_name'] = product['product_name']
            sale_info['product_category'] = product['product_category']
            sale_info['product_id'] = product['id']
            sale_info['selling_price'] = product['selling_price']
            sale_info['description'] = product['description']

            query = """ INSERT INTO sales(product_name, product_category, product_id, selling_price, description)
            VALUES(%s, %s, %s, %s, %s)"""
            cur.execute(query, (sale_info['product_name'], sale_info['product_category'], sale_info['product_id'],
            sale_info['selling_price'], sale_info['description']))
            conn.commit()
            return True
        return "That product does not exist"

    @staticmethod
    def get_all_sales():
        query = """ SELECT * FROM sales """
        cur.execute(query)
        sales = cur.fetchall()
        return sales