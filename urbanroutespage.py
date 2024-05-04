from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from sms_code import retrieve_phone_code
from locators import UrbanRoutesLocators
import data


# Esta clase representa a la pagina web de Urban Routes
class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    def __init__(self, driver):
        self.driver = driver
        self.selectors = UrbanRoutesLocators

        # Funciones de espera:

    # Espera que la pagina abra
    def wait_open_page(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.from_field))

    # Espera que el mapa se cargue
    def wait_load_map(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.selectors.map))

    # Espera hasta que aparezca el elemento del número de placa al finalizar el contador
    def wait_for_route_form_until_license_plate_displayed(self):
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(self.selectors. label_vehicle_plate))

    # Primer caso: Funciones para llenar los campos de ingreso de direcciones

    # Ingresa la dirección de inicio
    def set_from(self, address_from):
        self.driver.find_element(*self.from_field).send_keys(address_from)

    # Obtiene la dirección de inicio
    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    # Ingresa la direccion de destino
    def set_to(self, address_to):
        self.driver.find_element(*self.to_field).send_keys(address_to)

    # Obtiene la dirección de destino
    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    # Hace clic en el botón de pedir un taxi
    def click_ask_taxi_button(self):
        self.driver.find_element(*self.selectors.ask_button_taxi).click()

    # Reunir en un metodo el ingreso de las direcciones y hacer clic en el botón de pedir un taxi
    def enter_address_login(self, from_address, to_address):
        self.wait_open_page()
        self.set_from(from_address)
        self.set_to(to_address)
        self.wait_load_map()

    # Segundo caso:  Funciones para seleccionar la tarifa comfort
    def select_rate_comfort(self):  # Selecciona la tarifa comfort
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.selectors.rate_comfort))
        self.driver.find_element(*self.selectors.rate_comfort).click()

    def get_select_rate_comfort(self):  # Obtiene la selección de la tarifa comfort
        return self.driver.find_element(*self.selectors.label_blanket_tissue).text

    # Tercer caso: Funciones para ingresar el numero de telefono
    def click_phone_number(self):  # Hace clic en el campo de número de teléfono que abre una ventana emergente
        self.driver.find_element(*self.selectors.phone_number_input).click()

    def input_phone_number(self, phone_entry):  # Ingresa el número de teléfono en la ventana emergente
        self.driver.find_element(*self.selectors.modal_phone_number_input).send_keys(phone_entry)

    def click_modal_next_button_phone_number(self):  # Hace clic en el botón siguiente de la ventana emergente
        self.driver.find_element(*self.selectors.next_button_modal_phone).click()

    def enter_sms_code(self):  # Ingresa el código SMS que se obtiene mediante la función retrieve_phone_code
        sms_response = retrieve_phone_code(
            driver=self.driver)  # Extrae la función que obtiene el codigo SMS y se pasa a una variable
        self.driver.find_element(*self.selectors.entry_sms_code).send_keys(
            sms_response)  # Ubica el selector del campo y se coloca la variable donde se almacena el codigo.

    def click_confirm_sms_button(self):  # Hace clic en el botón de confirmación del código SMS
        self.driver.find_element(*self.selectors.confirm_sms_button).click()

    def get_phone_number(self):  # Obtiene el número de teléfono ingresado
        return self.driver.find_element(*self.selectors.modal_phone_number_input).get_property('value')

    def grouping_phone_entry(self, phone_entry):  # Reune el proceso de ingreso de teléfono, código SMS y confirmación
        self.click_phone_number()
        self.input_phone_number(phone_entry)
        self.click_modal_next_button_phone_number()
        time.sleep(1)
        self.enter_sms_code()
        self.click_confirm_sms_button()

    # Caso cuatro: Funciones para ingresar tarjeta de credito
    def click_payment_method_link(self):  # Hace clic en el enlace de forma de pago
        self.driver.find_element(*self.selectors.payment_method_link).click()

    def click_add_card_modal_button(self):  # Hace clic en el botón para ingresar tarjeta
        self.driver.find_element(*self.selectors.add_card_modal_button).click()

    def input_card_number_entry(self):  # Ingresa el número de tarjeta
        self.driver.find_element(*self.selectors.card_number_entry).send_keys(data.card_number)

    def input_card_cvv_entry(self):  # Ingresa código CVV de la tarjeta
        self.driver.find_element(*self.selectors.card_cvv_entry).send_keys(data.card_code)
        time.sleep(1)

    def click_card_form_blank_space(self):  # Hace clic en el espacio del formulario de tarjeta
        self.driver.find_element(*self.selectors.card_form_blank_space).click()

    def click_add_card_button_link(self):  # Hace clic en el botón para agregar la tarjeta
        self.driver.find_element(*self.selectors.add_card_button_link).click()

    def click_close_add_card_modal_button(self):  # Hace clic en el botón para cerrar la ventana de agregar tarjeta
        self.driver.find_element(*self.selectors.close_add_card_modal_button).click()

    def get_card_number_entry(self):  # Obtiene el número de tarjeta ingresado
        card_number = self.driver.find_element(*self.selectors.card_number_entry).get_property('value')
        return card_number

    def get_card_cvv_entry(self):  # Obtiene el código CVV de la tarjeta ingresado
        card_code = self.driver.find_element(*self.selectors.card_cvv_entry).get_property('value')
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
    def input_driver_comment_entry(self, message_for_driver):  # Ingresa el comentario para el conductor
        self.driver.find_element(*self.selectors.entry_driver_comment).send_keys(message_for_driver)

    def get_driver_comment_entry(self):  # Obtiene el comentario para el conductor
        return self.driver.find_element(*self.selectors.entry_driver_comment).get_property('value')

    # Sexto caso: Añadir manta y pañuelos
    def add_blanket_tissue_requirements(self):  # Hace clic en el checkbox para activar manta y pañuelos
        self.driver.find_element(*self.selectors.reqst_blank).click()

    def get_check_blanket_tissue_selection(self):  # Comprueba que manta y pañuelos está seleccionado
        return self.driver.find_element(*self.selectors.chk_blk_ts).is_selected()
        # return checkbox.is_selected()

    # Septimo caso: Añadir 2 helados
    def add_request_two_icecreams(self):  # Hace clic en el checkbox 2 veces para añadir helados
        self.driver.find_element(*self.selectors.reqst_two_icecream).click()
        self.driver.find_element(*self.selectors.reqst_two_icecream).click()

    def get_check_selection_of_two_ice_creams(self):  # Se obtiene la cantidad de helados seleccionados
        count_ice_cream = self.driver.find_element(*self.selectors.count_two_icecream)
        return int(count_ice_cream.text)

    # Octavo caso: Ventana emergente de pedir taxi
    def click_ask_taxi_final_button(self):  # Hace clic en el botón para pedir un taxi final
        self.driver.find_element(*self.selectors.button_order_a_taxi_final).click()
