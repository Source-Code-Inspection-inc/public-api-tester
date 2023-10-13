import os, json, requests
from dotenv import load_dotenv
from helper import print_success, print_info, save_file, get_base64_encoded_val

# Read environment variables from .env file
load_dotenv()

# using these for testing https://staging-internal.codewetrust-api.com test_user:token_123 6AB862-93BD86-C2DE65-AACC76-14D6D8-V3

def make_request(endpoint, method="GET", data=None):

    b64_auth_token = get_base64_encoded_val(f"{os.environ['USER NAME']}:{os.environ['PASSWORD']}")
    b64_license_key = get_base64_encoded_val(os.environ['LICENSE']) 
    
    headers = {
        "Authorization": f"Basic {b64_auth_token}",
        "CwtLicenseKey": f"{b64_license_key}",
    }

    url = f"{os.environ['URL']}{os.environ['VERSION']}{endpoint}"

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
    return products

def get_product_info(product_id):
    endpoint = f"/Products/{product_id}"
    response = make_request(endpoint, method="GET")
    if response.status_code == 200:
        products = json.loads(response.text)
        print_success(f"Success - GET {endpoint}")
        print_success(f"Title:- {products['title']}")
        print_success(f"Lines Of Code:- {str(products['linesOfCode'])}")

def save_engineering_report_by_scan_id(scan_id):
    endpoint = f"/reports/Engineering/{str(scan_id)}"
    response = make_request(endpoint, method="GET")
    if response.status_code == 200:
        print_success(f"Success - GET {endpoint}")
        save_file(response)

def save_executive_report_by_scan_id(scan_id):
    endpoint = f"/reports/Executive/{str(scan_id)}"
    response = make_request(endpoint, method="GET")
    if response.status_code == 200:
        print_success(f"Success - GET {endpoint}")        
        save_file(response)

def save_executive_details_report_by_scan_id(scan_id):
    endpoint = f"/reports/Executive/details/{str(scan_id)}"
    response = make_request(endpoint, method="GET")
    if response.status_code == 200:
        print_success(f"Success - GET {endpoint}")
        save_file(response)
