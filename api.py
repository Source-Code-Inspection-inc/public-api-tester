import os, json, requests
from helper import print_success, print_info, print_error, save_file, remove_trailing_slash

# Removed config from .env to create the exe for Windows machine using pyinstaller
VERSION = "/api/v1"


def make_request(endpoint, method="GET", data=None):
    headers = {
        "Authorization": "Bearer " + os.environ['TOKEN']
    }

    url = f"{remove_trailing_slash(os.environ['URL'])}{VERSION}{endpoint}"

    print_info(f"\nFetching  {url}")

    if method == "GET":
        response = requests.get(url, headers=headers)
    elif method == "POST":
        response = requests.post(url, headers=headers, json=data)
    elif method == "PUT":
        response = requests.put(url, headers=headers, json=data)
    else:
        raise ValueError("Invalid HTTP method")
    return response


def get_status():
    endpoint = "/Status"
    response = make_request(endpoint, method="GET")
    if response.status_code == 200:
        result = json.loads(response.text)
        if result["status"] == "OK":
            print_success(f"Success - GET {endpoint}")


def get_all_products():
    products = None
    endpoint = "/Products"
    response = make_request(endpoint, method="GET")
    if response.status_code == 200:
        products = json.loads(response.text)
        print_success(f"Success - GET {endpoint}")
        for idx, product in enumerate(products):
            print_success(f"{str(idx + 1)}. {product['title']}")
    else:
        print_error("Access Failed, Check credentials or contact the Adminstrator!")
        exit()
    return products


def get_product_info(product_id):
    endpoint = f"/Products/{product_id}"
    response = make_request(endpoint, method="GET")
    if response.status_code == 200:
        products = json.loads(response.text)
        print_success(f"Success - GET {endpoint}")
        print_success(f"Title:- {products['title']}")
        print_success(f"Lines Of Code:- {str(products['linesOfCode'])}")


def save_all_engineering_reports_by_scan_id(scan_id):
    save_response_to_file(f"/reports/Engineering/{str(scan_id)}")
    save_response_to_file(f"/reports/Executive/{str(scan_id)}")
    save_response_to_file(f"/reports/Executive/details/{str(scan_id)}")
    save_response_to_file(f"/reports/sbom/{str(scan_id)}")


def save_response_to_file(endpoint):
    response = make_request(endpoint, method="GET")
    if response.status_code == 200:
        print_success(f"Success - GET {endpoint}")
        save_file(response)
