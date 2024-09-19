def test_select_new_in_filter(shop_luma):
    shop_luma.open_page()
    shop_luma.select_new_in_filter()
    shop_luma.check_total_number_in_filter()


def test_add_clothes_to_compare(shop_luma):
    shop_luma.open_page()
    shop_luma.add_item()
    shop_luma.compare_item()


def test_add_to_wishlist_without_registration(shop_luma):
    shop_luma.open_page()
    shop_luma.add_item_to_wishlist()
    shop_luma.check_wish_list_message_is('You must login or register to add items to your wishlist.')
