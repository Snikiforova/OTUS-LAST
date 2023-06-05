def test_registration(registration_page):
    registration_page.open()
    registration_page.click_myaccount()
    registration_page.select_reg_page()
    registration_page.fill_registration_form()
