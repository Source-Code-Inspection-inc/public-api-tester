import re, os, base64
from colorama import Fore, init

init(autoreset=True)

def set_env_for_scan():
    get_user_config("url")
    get_user_config("user name")
    get_user_config("password")
    get_user_config("license")

def get_user_selected_product_idx(products):
    print(products)
    val = input(f"\nPlease enter a number between 1 and {len(products)} to select the product: ").strip()
    if int(val) <= len(products):
        idx = int(val)
        print(f"products[idx] selected for scanning.")
        return idx
    else :
        print("Invalid Product Index")
        get_user_selected_product_idx(products)

def get_base64_encoded_val(data):
    return (base64.b64encode(data.encode("utf-8"))).decode("utf-8")

def get_user_config(key):
    val = input(f"Please enter the {key.title()} : ").strip()
    os.environ[key.upper()] = val

def print_info(data):
    print(Fore.WHITE + data )

def print_success(data):
    print(Fore.GREEN  + data )

def get_file_name_from_header(headers):
    # Extract the file_name from the Content-Disposition header using regex
    match = re.search(
        r"filename=(.*?)(?:;|$)", headers.get("content-disposition")
    )
    return f"{match.group(1)}"

