from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from sms_code import retrieve_phone_code
import data


class UrbanRoutesLocators:

    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    map = (By.CLASS_NAME, 'gm-style')
    ask_button_taxi = (By.XPATH, ".//div[@class='results-text']/button[text()='Pedir un taxi']")
    rate_comfort = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
    phone_number_input = (By.CSS_SELECTOR, "div.np-text")
    modal_phone_number_input = (By.ID, 'phone')
    next_button_modal_phone = (By.XPATH, "//button[@type='submit'][@class='button full']")
    entry_sms_code = (By.ID, 'code')
    confirm_sms_button = (By.XPATH, "//button[@class='button full' and text()='Confirmar']")
    payment_method_link = (By.CLASS_NAME, 'pp-text')
    add_card_modal_button = (By.CLASS_NAME, "pp-plus")
    card_number_entry = (By.ID, 'number')
    card_cvv_entry = (By.CSS_SELECTOR, "input[placeholder='12']")
    card_form_blank_space = (By.CLASS_NAME, 'card-wrapper')
    add_card_button_link = (By.XPATH, "//button[@type='submit'][@class='button full' and text()='Enlace']")
    close_add_card_modal_button = (By.CSS_SELECTOR, "div.payment-picker button.close-button.section-close")
    entry_driver_comment = (By.ID, 'comment')
    reqst_blank = (By.CSS_SELECTOR, "input[type='checkbox'].switch-input")
    chk_blk_ts = (By.CSS_SELECTOR, "div.reqs-body > div span.slider.round")
    label_blanket_tissue = (By.XPATH, "//div[contains(text(),'Manta y pañuelos')]")
    reqst_two_icecream = (By.CSS_SELECTOR, "div.r-group-items > div:nth-child(1) div.counter-plus")
    count_two_icecream = (By.CSS_SELECTOR, "div.r-group-items > div:nth-child(1) div.counter-value")
    button_order_a_taxi_final = (By.CLASS_NAME, 'smart-button')
    route_details_button = (By.XPATH, "//button[@class='order-button' and img[@alt='burger']]")
    route_details_form = (By.CLASS_NAME, 'order-body')
    label_searching_taxi_form = (By.XPATH, "//div[@class='order-header-title' and text()='Buscar automóvil']")
    label_vehicle_plate = (By.XPATH, "//div[@class='number']")
    waiting_vehicle_minutes_label = (By.XPATH, "//div[@class='order-header-title']")
    request_button = (By.CLASS_NAME, 'smart-button')
    check_comfort_rate = (By.XPATH, "//div[@class='tcard active']//div[text()='Comfort']")


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    def __init__(self, driver):
        self.driver = driver
        self.selectors = UrbanRoutesLocators

    def wait_open_page(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.from_field))

    def wait_load_map(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.selectors.map))

    def wait_for_route_form_until_license_plate_displayed(self):
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(self.selectors. label_vehicle_plate))

    # Primer caso: Funciones para llenar los campos de ingreso de direcciones

    def set_from(self, address_from):
        self.driver.find_element(*self.from_field).send_keys(address_from)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def set_to(self, address_to):
        self.driver.find_element(*self.to_field).send_keys(address_to)

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_ask_taxi_button(self):
        self.driver.find_element(*self.selectors.ask_button_taxi).click()

    def enter_address_login(self, from_address, to_address):
        self.wait_open_page()
        self.set_from(from_address)
        self.set_to(to_address)
        self.wait_load_map()

    # Segundo caso:  Funciones para seleccionar la tarifa comfort
    def select_rate_comfort(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.selectors.rate_comfort))
        self.driver.find_element(*self.selectors.rate_comfort).click()

    def get_select_rate_comfort(self):
        return self.driver.find_element(*self.selectors.check_comfort_rate).text

    # Tercer caso: Funciones para ingresar el numero de telefono
    def click_phone_number(self):
        self.driver.find_element(*self.selectors.phone_number_input).click()

    def input_phone_number(self, phone_entry):
        self.driver.find_element(*self.selectors.modal_phone_number_input).send_keys(phone_entry)

    def click_modal_next_button_phone_number(self):
        self.driver.find_element(*self.selectors.next_button_modal_phone).click()

    def enter_sms_code(self):
        sms_response = retrieve_phone_code(
            driver=self.driver)
        self.driver.find_element(*self.selectors.entry_sms_code).send_keys(
            sms_response)

    def click_confirm_sms_button(self):
        self.driver.find_element(*self.selectors.confirm_sms_button).click()

    def get_phone_number(self):
        return self.driver.find_element(*self.selectors.phone_number_input).get_property('value')

    def grouping_phone_entry(self, phone_entry):
        self.click_phone_number()
        self.input_phone_number(phone_entry)
        self.click_modal_next_button_phone_number()
        time.sleep(1)
        self.enter_sms_code()
        self.click_confirm_sms_button()

    # Caso cuatro: Funciones para ingresar tarjeta de credito
    def click_payment_method_link(self):
        self.driver.find_element(*self.selectors.payment_method_link).click()

    def click_add_card_modal_button(self):
        self.driver.find_element(*self.selectors.add_card_modal_button).click()

    def input_card_number_entry(self):
        self.driver.find_element(*self.selectors.card_number_entry).send_keys(data.card_number)

    def input_card_cvv_entry(self):
        self.driver.find_element(*self.selectors.card_cvv_entry).send_keys(data.card_code)
        time.sleep(1)

    def click_card_form_blank_space(self):
        self.driver.find_element(*self.selectors.card_form_blank_space).click()

    def click_add_card_button_link(self):
        self.driver.find_element(*self.selectors.add_card_button_link).click()

    def click_close_add_card_modal_button(self):
        self.driver.find_element(*self.selectors.close_add_card_modal_button).click()

    def get_card_number_entry(self):
        card_number = self.driver.find_element(*self.selectors.payment_method_link).get_property('value')
        return card_number

    def get_card_cvv_entry(self):
        card_code = self.driver.find_element(*self.selectors.payment_method_link).get_property('value')
        return card_code

    def add_card_fuction(self):
        # Reune las funciones para agregar una tarjeta de crédito
        self.click_payment_method_link()
        self.click_add_card_modal_button()
        self.input_card_number_entry()
        self.input_card_cvv_entry()
        self.click_card_form_blank_space()
        self.click_add_card_button_link()
        self.click_close_add_card_modal_button()

    # Quinto caso: Comentario al conductor
    def input_driver_comment_entry(self, message_for_driver):
        self.driver.find_element(*self.selectors.entry_driver_comment).send_keys(message_for_driver)

    def get_driver_comment_entry(self):
        return self.driver.find_element(*self.selectors.entry_driver_comment).get_property('value')

    # Sexto caso: Añadir manta y pañuelos
    def add_blanket_tissue_requirements(self):
        self.driver.find_element(*self.selectors.reqst_blank).click()

    def get_check_blanket_tissue_selection(self):
        return self.driver.find_element(*self.selectors.chk_blk_ts).is_selected()
        # return checkbox.is_selected()

    # Septimo caso: Añadir 2 helados
    def add_request_two_icecreams(self):
        self.driver.find_element(*self.selectors.reqst_two_icecream).click()
        self.driver.find_element(*self.selectors.reqst_two_icecream).click()

    def get_check_selection_of_two_ice_creams(self):
        count_ice_cream = self.driver.find_element(*self.selectors.count_two_icecream)
        return int(count_ice_cream.text)

    # Octavo caso: Ventana emergente de pedir taxi
    def click_ask_taxi_final_button(self):  # Hace clic en el botón para pedir un taxi final
        self.driver.find_element(*self.selectors.button_order_a_taxi_final).click()
        EC.element_to_be_clickable((By.CLASS_NAME, 'smart-button'))

    def get_ask_taxi_final_button(self):
        button_order_a_taxi_final = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button.smart-button'))
        )
        return button_order_a_taxi_final
