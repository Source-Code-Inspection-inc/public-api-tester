from helper import(
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

def main():
    
    get_status()

    products = get_all_products()

    selected_product_idx  = get_user_selected_product_idx(products)
    scan_id = products[selected_product_idx]["scans"][0]["id"]
    
    get_product_info(products[selected_product_idx]["id"])

    save_executive_report_by_scan_id(scan_id)
    save_executive_details_report_by_scan_id(scan_id)
    save_engineering_report_by_scan_id(scan_id)


if __name__ == "__main__":
    main()
