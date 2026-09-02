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
def search_product_on_name():
    errormsg=""
    print("search_product_on_name")
    productcatlist, errormsg = app.Backend.product.productservice.search_product_on_name("TV")
    if errormsg =="" :
        if len(productcatlist)==0 :
             print("No matching Product found")
        for catg in productcatlist:
                print(
                    f"Name: {catg['productName']}, "
                    f"Description: {catg['productdescription']} "                
                )
    else:
        print(errormsg)

def search_product_on_barnd():
    errormsg=""
    print("search_product_on_barnd")
    productcatlist, errormsg = app.Backend.product.productservice.search_product_on_brand("TV","samsung")
    if errormsg =="" :
        if len(productcatlist)==0 :
             print("No matching Product found")
        for catg in productcatlist:
                print(
                    f"Name: {catg['productname']}, "
                    f"Description: {catg['productdescription']} "                
                )
    else:
        print(errormsg)

def main():
##  customerList()
##   productcatg_list()
##   product_listForcatg()
    print("Test1")
    search_product_on_barnd()

## Main start from here
main()