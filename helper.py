import re, os
from colorama import Fore, Style, init

init(autoreset=True)

def set_env_for_scanning():
    get_user_config("URL", "API URL (without '/api')")
    get_user_config("TOKEN", "Token")

def remove_trailing_slash(url):
    return url.rstrip('/')

def get_user_config(key, title):
    os.environ[key] = input(f"\n{Fore.CYAN} {title}: {Style.RESET_ALL}").strip()

def get_user_selected_product_idx(products):

    if products is not None and len(products) > 0:
        val = input(f"\nSelect product (1..{len(products)}): ").strip()

        if int(val) <= len(products):
            idx = int(val) - 1
            print_success(f"{products[idx]['title']} selected for scanning.")
            return idx
        else :
            print("Invalid product index")
            get_user_selected_product_idx(products)
    else:
        print("No products found!")
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
    # remove the " \ characters from the file name some file are wrapped in quotes we dont need them here
    file_name = re.sub(r'[\\"]', '', match.group(1))

    # Save the file to disk
    with open(file_name, "wb") as file:
        file.write(response.content)

    print_success(f"File saved as {file_name}")


