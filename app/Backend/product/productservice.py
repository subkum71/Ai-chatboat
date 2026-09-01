## All product and category related functions
## importing project's package
from app.Database.db import get_db_connection

#Purpose : Return Product category with its description
def get_List_ProductCategory():
     # database code to get Product category list
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        if connection is None:
            return None,"Error in get_List_ProductCategory,Database connection failed "
        cursor = connection.cursor(dictionary=True)

        query = """
            select category_name, description from ecommerce_chat.product_category
        """

        cursor.execute(query)
        productcatlist = cursor.fetchall()
        return productcatlist,""

    except Exception as error:
        errormsg = f"Error in get_List_ProductCategory, Error: {error}"
        return None, errormsg
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
    #Purpose : Return Product category with its description

#Purpose : Return Productlist for given category
def search_product_category(category):
     # database code to get matching Product category list
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        if connection is None:
            return None,"Error in get_List_Product,Database connection failed "
        cursor = connection.cursor(dictionary=True)
        query = """
            select category_name, description from ecommerce_chat.product_category
              WHERE UPPER(category_name) LIKE UPPER(%s)
        """ 
        cursor.execute(query,(category+'%',))
        productcatlist = cursor.fetchall()
        return productcatlist,""

    except Exception as error:
        errormsg = f"Error in search_product_category, Error: {error}"
        return None, errormsg
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()