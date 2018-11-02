from ..models import conn, cur
import re


class ProductsDetails():

    @staticmethod
    def create_product(product_name, product_category, buying_price, selling_price, description):

        data_type = (int, float)

        if not re.match("^[a-zA-Z0-9_]*$", product_name):
            return "Product Name Should be alphanumeric Characters and should not be empty"
        if not re.match("^[a-zA-Z0-9_]*$", product_category):
            return "Product Category Should be alphanumeric Characters and should not be empty"
        if not isinstance(buying_price, data_type):
            return "Product Buying price should be Numbers"
        if not isinstance(selling_price, data_type):
            return "Selling price should be Numbers"
        if not isinstance(description, str):
            return "Product Description Should be Strings"
        if len(product_name) == 0:
            return "The product Name field cant empty"
        if len(product_category) == 0:
            return "The category Name field cant empty"
        if len(description) == 0:
            return "The description field cant empty"
        if len(description) < 5:
            return "The description too short"

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

    @staticmethod
    def get_product_by_id(id):

        query = """ SELECT * FROM products WHERE id = %s """
        cur.execute(query, (id,))

        product = cur.fetchone()
        return product

    @staticmethod
    def delete_product(id):
        query = """ SELECT * FROM products """
        cur.execute(query)
        products = cur.fetchall()
        if products:
            for product in products:
                if product['id'] == id:
                    query = """ DELETE FROM products WHERE id = %s """
                    cur.execute(query, (id,))
                    conn.commit()
                    return True
                return "Product does not exist"
        return "There no Products in the database"

    

    @staticmethod
    def get_specific(category):
        query = """ SELECT * FROM products """
        cur.execute(query)
        products = cur.fetchall()

        if products:
            for product in products:
                if product['product_category'] == category:
                    products = len(product)
                    return products
            else:
                return "No Dells In The Store"

        return "There are no products in the database"


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

            query2 = """ DELETE FROM products WHERE id = %s """
            cur.execute(query2, (product['id'],))
            conn.commit()

            return True
        return "That product does not exist"

    @staticmethod
    def get_all_sales():
        query = """ SELECT * FROM sales """
        cur.execute(query)
        sales = cur.fetchall()
        return sales

    