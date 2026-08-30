import os
import mysql.connector
from dotenv import load_dotenv


# Load variables from .env
load_dotenv()


## importing project's package
from app.Backend.customer.service import get_allcustomer
import app.Backend.product.productservice
## main function

def customerList():
    customers = get_allcustomer()

    print("Customer List")
    print("-" * 80)

    for customer in customers:
        print(
            f"ID: {customer['customer_id']}, "
            f"Name: {customer['customer_name']}, "
            f"Phone: {customer['phone']}, "
            f"Email: {customer['email']}"
        )

def productcatg_list():
    errormsg=""
    productcatlist, errormsg = app.Backend.product.productservice.get_List_ProductCategory()
    if errormsg =="" :
        for catg in productcatlist:
                print(
                    f"ID: {catg['category_name']}, "
                    f"Name: {catg['description']} "                
                )
    else:
        print(errormsg)

def product_listForcatg():
    errormsg=""
    productcatlist, errormsg = app.Backend.product.productservice.search_product_category("ELECT")
    if errormsg =="" :
        if len(productcatlist)==0 :
             print("No matching category found")
        for catg in productcatlist:
                print(
                    f"ID: {catg['category_name']}, "
                    f"Name: {catg['description']} "                
                )
    else:
        print(errormsg)
 
def main():
##   customerList()
##   productcatg_list()
    product_listForcatg()

## Main start from here

main()