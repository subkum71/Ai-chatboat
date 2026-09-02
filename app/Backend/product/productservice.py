## All product and category related functions
## importing project's package
from app.Database.db import get_db_connection

#1.Purpose : Return Product category with its description
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

#2.Purpose : Return Productlist for given category
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

            #Purpose : Return Productlist for given category
#3. Search on product Name 
def search_product_on_name(ProductName):
     # database code to get matching Product category list
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        if connection is None:
            return None,"Error in search_product,Database connection failed "
        cursor = connection.cursor(dictionary=True)
        query = """
            select product_name as ProductName, description as productdescription, brand, price, stock_quantity as Qty from ecommerce_chat.product_detail
            where UPPER(product_name) LIKE UPPER(%s)
        """ 
        cursor.execute(query,(ProductName+'%',))
        productcatlist = cursor.fetchall()
        return productcatlist,""

    except Exception as error:
        errormsg = f"Error in search_product, Error: {error}"
        return None, errormsg
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

    #4. Search on product Description
def search_product_on_description(productdescription):
     # database code to get matching Product category list
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        if connection is None:
            return None,"Error in search_product_on_description,Database connection failed "
        cursor = connection.cursor(dictionary=True)
        query = """
            select product_name as ProductName, description as productdescription, brand, price, stock_quantity as Qty from ecommerce_chat.product_detail
            where UPPER(description) LIKE UPPER(%s)
        """ 
        cursor.execute(query,(productdescription+'%',))
        productcatlist = cursor.fetchall()
        return productcatlist,""
    
    except Exception as error:
        errormsg = f"Error in search_product_on_description, Error: {error}"
        return None, errormsg
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

    #5 Search on Product Brand
def search_product_on_brand(productname,productbrand):
    # database code to get matching Product category list
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        if connection is None:
            return None,"Error in search_product_on_brand,Database connection failed "
        cursor = connection.cursor(dictionary=True)
        query = """
            select product_name as productname, description as productdescription, brand, price, stock_quantity as Qty
            from ecommerce_chat.product_detail
            where UPPER(product_name) LIKE UPPER(%s) and UPPER(brand) LIKE UPPER(%s)
        """ 
        cursor.execute(query,('%' +productname+'%', '%' +productbrand+'%',))
        productcatlist = cursor.fetchall()
        return productcatlist,""
    
    except Exception as error:
        errormsg = f"Error in search_product_on_brand, Error: {error}"
        return None, errormsg
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
     #6 Get Product List for Given Category
def get_product_List_Category(Productcategory):
             # database code to get matching Product category list
        connection = None
        cursor = None
        try:
            connection = get_db_connection()
            if connection is None:
                return None,"Error in get_product_List_Category,Database connection failed "
            cursor = connection.cursor(dictionary=True)
            query = """
                select product_name as ProductName,  brand, price, stock_quantity as Qty 
                from ecommerce_chat.product_detail as prod, ecommerce_chat.productproduct_category as Catg
                where prod.category_id = Catg.Category_id  and UPPER(Catg.category_name) LIKE UPPER(%s)
                """ 
            cursor.execute(query,(Productcategory+'%',))
            productcatlist = cursor.fetchall()
            return productcatlist,""
        
        except Exception as error:
                errormsg = f"Error in get_product_List_Category, Error: {error}"
                return None, errormsg
        finally:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()
    #7 Get Product List for Given Category
def is_stockavilableforproduct(productname):
    # database code to get matching Product category list
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        if connection is None:
            return None,"Error in is_stockavilableforproduct,Database connection failed "
        cursor = connection.cursor(dictionary=True)
        query = """
                select product_name as ProductName, description as productdescription, brand, price, stock_quantity as Qty from ecommerce_chat.product_detail
                where stock_quantity>0 and UPPER(product_name) LIKE UPPER(%s) 
                """ 
        cursor.execute(query,(productname+'%',productname+'%',))
        productcatlist = cursor.fetchall()
        return productcatlist,""
            
    except Exception as error:
            errormsg = f"Error in is_stockavilableforproduct, Error: {error}"
            return None, errormsg
    finally:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()