def test_check_women_sales_url(sales):
    sales.open_page()
    sales.open_women_items('https://magento.softwaretestingboard.com/promotions/women-sale.html')


def test_check_title_jackets(sales):
    sales.open_page()
    sales.open_jackets()


def test_add_to_compare_and_delete_clothes(sales):
    sales.open_page()
    sales.add_to_compare_and_delete()
