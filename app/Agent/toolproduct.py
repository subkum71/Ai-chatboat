## Convert all our functions in tool
from langchain.tools import tool

from app.Backend.product.productservice import (
    get_List_ProductCategory,
    search_product_category,
    search_product_on_name,
    search_product_on_description,
    search_product_on_brand,
    get_product_List_For_Given_Category,
    is_stockavilableforproduct
)

@tool
def get_all_product_categories() -> list:
    """
    Get the list of all available product categories.

    Returns:
        A list of product categories with their descriptions.
    """
    productcatlist, error = get_List_ProductCategory()

    if error == "":
        return productcatlist

    return []


@tool
def search_product_categories(category: str) -> list:
    """
    Search for product categories matching the specified category.

    Args:
        category: Product category or keyword to search for.

    Returns:
        A list of matching product categories.
    """
    productcatlist, error = search_product_category(category)

    if error == "":
        return productcatlist

    return []

@tool
def search_product_on_name_Service(ProductName: str) -> list:
    """
    For customer , Get the list of all available products.

    Args:Product Name

    Returns:
        A list of product Name with their details.
    """
    productcatlist, error = search_product_on_name(ProductName)

    if error == "":
        return productcatlist

    return []

@tool
def search_product_on_description_Service(productdescription:str) -> list:
    """
    GetFor customer ,  the list of all available products.

    Args:Product Description

    Returns:
        A list of product Name with their details.
    """
    productcatlist, error = search_product_on_description(productdescription)

    if error == "":
        return productcatlist
    return []
@tool
def search_product_on_brand_Service(productname:str, brand:str) -> dict:
    """
    For customer , Get the list of products for given brand.

    Args:productname,brand

    Returns:
        A list of product Name with their details.
    """
    productcatlist, error = search_product_on_brand(productname,brand)

    if error:
        return {
            "success": False,
            "data": [],
            "message": f"Unable to search products. Server Error: {error}"
        }

    if not productcatlist:
        return {
            "success": True,
            "data": [],
            "message": "No product found under given category{productname} under brand {brand}"
        }

    return {
        "success": True,
        "data": productcatlist,
        "message": "Product found."
    }

@tool
def get_product_List_For_Given_Category_Service(productcatg:str) -> dict:
    """
    For customer , Get the list of products for given Product Category.

    Args:Product Category

    Returns:
        A list of product Name with their details.
    """
    productcatlist, error = get_product_List_For_Given_Category(productcatg)

    if error:
            return {
                "success": False,
                "data": [],
                "message": f"Unable to get list of products for given Product Category. Server Error: {error}"
            }
    if not productcatlist:
        return {
                "success": True,
                "data": [],
                "message": "No product found under given category{productcatg}"
            }
    
    return {
            "success": True,
            "data": productcatlist,
            "message": "Products found."
        }

@tool
def is_stockavilableforproduct_Service(productname:str) -> dict:
    """
    For customer , Get product details if stoack available. If Qty>0

    Args:Product Name

    Returns:
        A list of product Name with their details.
    """
    productcatlist, error = is_stockavilableforproduct(productname)

    if error:
        return {
                    "success": False,
                    "data": [],
                    "message": f"Unable to get product details. Server Error: {error}"
                }
    if not productcatlist:
        return {
                    "success": True,
                    "data": [],
                    "message": f"{productname} Out of stock "
                }
        
    return {
                "success": True,
                "data": productcatlist,
                "message": "Products found."
            }