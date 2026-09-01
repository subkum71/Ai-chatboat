## Convert all our functions in tool
from langchain.tools import tool

from app.Backend.product.productservice import (
    get_List_ProductCategory,
    search_product_category
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