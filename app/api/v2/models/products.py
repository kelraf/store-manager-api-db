from app.api.v2.models import conn, cur

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
        return products
