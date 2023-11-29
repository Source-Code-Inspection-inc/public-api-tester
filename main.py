from helper import (
    set_env_for_scanning,
    get_user_selected_product_idx,
)
from api import (
    get_status,
    get_all_products,
    get_product_info,
    save_all_engineering_reports_by_scan_id
)


def main():
    set_env_for_scanning()
    get_status()
    products = get_all_products()

    selected_product_idx = get_user_selected_product_idx(products)
    scan_id = products[selected_product_idx]["scans"][0]["id"]

    get_product_info(products[selected_product_idx]["id"])
    save_all_engineering_reports_by_scan_id(scan_id)


if __name__ == "__main__":
    main()
