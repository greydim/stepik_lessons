

def test_add_item_button_text(browser):
    # Data
    link = "http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207/"

    add_item_button_locator = "#add_to_basket_form button[type='submit']"

    list_of_button_text = ["Добавить в корзину", "Add to basket", "Añadir al carrito", "Ajouter au panier"]

    # Arrange
    browser.get(link)

    # Act
    add_item_button = browser.find_element_by_css_selector(add_item_button_locator)

    # Assert
    add_item_button_text = add_item_button.text
    assert add_item_button_text in list_of_button_text, \
        f'Неверный текст кнопки добавления товара, текст: "{add_item_button_text}"'
