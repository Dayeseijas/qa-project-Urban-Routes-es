En el siguiente proyecto se ha realizado la automatización de las pruebas para el pedido de un taxi en la aplicación web de Urban.Routes, utilizando Selenium. Las pruebas tienen como objetivo llevar a cabo las siguientes operaciones:

-Acceder a la URL de Urban-Routes
-Configuración de las direcciónes de origen y de destino.
-Esperar que cargue el mapa y hacer clic en "Pedir un taxi"
-Selección de la tarifa Comfort
-Ingresar campo de número de teléfono (así mismo, dentro de esta función recuperar un codigo SMS)
-Agregar una forma de pago: una tarjeta de crédito (incluyendo numero de tarjeta y codigo CVV)
-Escribir un mensaje para el conductor del taxi
-Petición de una manta y pañuelos
-Petición de 2 helados
-Mostrar el modal para buscar un taxi.

Para ejecutar las pruebas, es necesario clonar el repositorio e instalar los paquetes necesario (Selenium y Pytest) Los pasos para instalar estos paquetes son los siguientes:

Para Pytest:
-Ir a la pestaña de python packages, buscar e instalar los paquetes mencionados.
-Ir a la pestaña de la consola y escribir: pip install pytest

Para Selenium:
-Descargar e Instalar el controlador para el navegador que vas a utilizar, tener en cuenta la version de tu navegador, para descargarlo hacer click en el siguiente enlace: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/driver_location/

Instrucciones para ejecución de las pruebas

Módulos 

data.py: Contiene datos de prueba, como la URL de Urban Routes, direcciones de origen y destino, números de teléfono y detalles de tarjetas.
sms_code.py: Indica una función para recuperar el código SMS necesario para la verificación.
locators.py: Define la clase UrbanRoutesLocators que almacena los selectores de elementos de la interfaz de usuario.

Clases 

UrbanRoutesPage: Indica métodos para interactuar con la interfaz de Urban Routes, desde el ingreso de direcciones hasta la confirmación del pedido.
TestUrbanRoutes: Contiene casos de prueba utilizando la biblioteca de pruebas pytest. Configura y cierra el navegador, y lleva a cabo las ocho pruebas.

Ejecuta las pruebas de TestUrbanRoutes que se ubican en el archivo main.py.