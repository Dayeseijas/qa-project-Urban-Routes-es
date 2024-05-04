from selenium import webdriver
import data
from urbanroutespage import UrbanRoutesPage
from selenium.webdriver.support.wait import WebDriverWait


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):  # Configuración inicial de la clase de prueba
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    # 1. Prueba para configurar la dirección.
    def test_one_set_address(self):

        self.address_from = data.address_from
        self.address_to = data.address_to

        self.routes_page.enter_address_login(self.address_from, self.address_to)
        assert self.routes_page.get_from() == self.address_from
        assert self.routes_page.get_to() == self.address_to

    # 2. Prueba para seleccionar la tarifa Comfort.
    def test_two_select_comfort_rate(self):
        # Realiza la seleccion de tarifa comfort
        self.routes_page.click_ask_taxi_button()
        WebDriverWait(self.driver, 2)
        self.routes_page.select_rate_comfort()
        assert self.routes_page.get_select_rate_comfort() == 'Manta y pañuelos'

    # 3. Prueba para ingresar el número de teléfono.
    def test_three_entry_phone(self):
        phone_number = data.phone_number

        self.routes_page.grouping_phone_entry(phone_number)
        assert self.routes_page.get_phone_number() == phone_number

    # 4. Prueba para Agregar una tarjeta de crédito.
    def test_four_add_card(self, card_number, card_code):  # Caso de prueba: Agregar detalles de tarjeta de crédito

        self.routes_page.add_card_fuction()
        # comprobacion de que el numero de tarjeta y el codigo de la misma sean los correctos
        assert self.routes_page.get_card_number_entry() == card_number
        assert self.routes_page.get_card_cvv_entry() == card_code

    # 5. Prueba para escribir un mensaje para el conductor.
    def test_five_input_driver_message(self):  # Caso de prueba: Ingresar mensaje a conductor
        message_for_driver = data.message_for_driver

        # Llama la función para ingresar detalles del conductor y verificar los resultados
        self.routes_page.input_driver_comment_entry(message_for_driver)
        assert self.routes_page.get_driver_comment_entry() == message_for_driver

    # 6. Prueba para pedir una manta y pañuelos
    def test_six_add_request_blanket_tissue(self):  # Caso de prueba: Activar opción de manta y pañuelo
        self.routes_page.add_blanket_tissue_requirements()

        assert self.routes_page.get_check_blanket_tissue_selection()

    # 7. Prueba para pedir 2 helados
    def test_seven_add_request_two_icecreams(self):  # Caso de prueba: Añadir opción de 2 helados
        self.routes_page.add_request_two_icecreams()

        assert self.routes_page.get_check_selection_of_two_ice_creams() == data.ice_cream_numbers

    # 8. Prueba para que aparezca el modal para pedir un taxi
    def test_eight_search_taxi_modal_appears(self):  # Aparece ventana emergente para buscar taxi

        self.routes_page.click_ask_taxi_final_button()
        WebDriverWait(self.driver, 40)

    @classmethod
    def teardown_class(cls):
        # Cierra el navegador al finalizar todos los tests
        cls.driver.quit()
