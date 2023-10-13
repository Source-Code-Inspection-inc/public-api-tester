from helper import(
    set_env_for_scan,
    get_user_selected_product_idx,
)
from api import (    
    get_status,
    get_all_products,
    get_product_info,
    save_executive_report_by_scan_id,
    save_executive_details_report_by_scan_id,
    save_engineering_report_by_scan_id
)

# All the three endpoints are tested here
def main():

    set_env_for_scan()
    
    get_status()

    products = get_all_products()
    print(products)
    selected_product_idx  = get_user_selected_product_idx(products)
    scan_id = products[selected_product_idx]["scans"][0]["id"]
    
    get_product_info(products[selected_product_idx]['id'])

    save_executive_report_by_scan_id(scan_id)
    save_executive_details_report_by_scan_id(scan_id)
    save_engineering_report_by_scan_id(scan_id)


if __name__ == "__main__":
    main()
