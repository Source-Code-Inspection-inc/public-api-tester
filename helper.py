import re, os, base64
from colorama import Fore, Style, init

init(autoreset=True)

def set_env_for_scan():
    get_user_config("url")
    get_user_config("user name")
    get_user_config("password")
    get_user_config("license")

def get_user_config(key):
    os.environ[key.upper()] = input(f"\n{Fore.CYAN} Please enter the {key.title()} : {Style.RESET_ALL}").strip()
    
def get_user_selected_product_idx(products):
    val = input(f"\nPlease enter a number between 1 and {len(products)} to select the product: ").strip()
    
    if int(val) <= len(products):
        idx = int(val) - 1 
        print_success(f"{products[idx]['title']} selected for scanning.")
        return idx
    else :
        print("Invalid Product Index")
        get_user_selected_product_idx(products)

def get_base64_encoded_val(data):
    return (base64.b64encode(data.encode("utf-8"))).decode("utf-8")

def print_info(data):
    print(Fore.WHITE + data )

def print_success(data):
    print(Fore.GREEN  + data )

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


