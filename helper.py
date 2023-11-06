import re, os, base64
from colorama import Fore, Style, init

init(autoreset=True)
    
def get_user_selected_product_idx(products):

    if(products != None and len(products) > 0):
        val = input(f"\nPlease enter a number between 1 and {len(products)} to select the product: ").strip()
        
        if int(val) <= len(products):
            idx = int(val) - 1 
            print_success(f"{products[idx]['title']} selected for scanning.")
            return idx
        else :
            print("Invalid Product Index")
            get_user_selected_product_idx(products)
    else:
        print("No Products for the user!")
        exit()

def print_info(data):
    print(Fore.WHITE + data )

def print_success(data):
    print(Fore.GREEN  + data )

def print_error(data):
    print(Fore.RED + data )

def save_file(response):
    # Extract the file_name from the Content-Disposition header using regex
    match = re.search(
        r"filename=(.*?)(?:;|$)", response.headers.get("content-disposition")
    )
    # Save the file to disk
    file_name = match.group(1)
    with open(file_name, "wb") as file:
        file.write(response.content)
    
    print_success(f"File saved as {file_name}")


