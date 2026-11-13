Cuando una persona escribe la URL de una aplicación web en el navegador, el primer paso es identificar a qué equipo debe conectarse. Para ello se necesita realizar el comando en CMD ipconfig y revisar la linea direccion ipv4 le arrojara la IP 192.168.x.x, el navegador utiliza el nombre del sitio para obtener la dirección IP del equipo donde está alojada la aplicación. Una vez obtenida esa dirección, establece la comunicación con el servidor utilizando un puerto determinado.

A continuación, el cliente (el navegador del usuario) envía una petición mediante el protocolo HTTP. Esa petición se conoce como request y contiene información sobre el recurso que se desea consultar. Si el usuario envía información desde un formulario, la petición puede utilizar el método POST para transportar los datos al servidor.

Cuando la petición llega al servidor, entra en funcionamiento el backend de la aplicación. En este caso, el backend está desarrollado con Python utilizando el framework Flask. Flask recibe la solicitud y la dirige a la ruta correspondiente según la URL solicitada. La ruta contiene la lógica necesaria para procesar la información recibida, realizar validaciones o ejecutar las operaciones requeridas por la aplicación.

Después de procesar la petición, Flask prepara la información que se mostrará al usuario. Para ello utiliza un template, que sirve como plantilla para generar la página web dinámica. En el template se integra el contenido que será enviado al navegador.

El resultado generado se convierte en un documento HTML, que define la estructura de la página. Para controlar la apariencia visual se utilizan hojas de estilo CSS. Además, Bootstrap proporciona componentes y estilos prediseñados que facilitan la creación de interfaces con un diseño uniforme y adaptable a distintos dispositivos.

Si la aplicación incorpora comportamiento interactivo en el navegador, puede intervenir JavaScript para ejecutar acciones del lado del cliente sin necesidad de recargar completamente la página. Sin embargo, solo participa cuando la aplicación ha sido desarrollada para utilizarlo.

Finalmente, el servidor envía una response al cliente mediante HTTP. Esta respuesta contiene el código HTML generado, junto con los archivos CSS, Bootstrap y, en caso de existir, JavaScript. El navegador recibe esa información, interpreta el contenido y construye la interfaz visible para el usuario. De esta manera, el frontend se muestra en pantalla con el resultado final obtenido a partir de la petición realizada al backend.

*Diagrama de Flujo*

    A[ Usuario escribe la URL en el navegador] --> B[ El navegador busca la dirección IP del servidor]
    B --> C[ Conexión con la IP y el puerto de la aplicación]
    C --> D[ Envío de una petición HTTP POST]
    D --> E[ Flask recibe la solicitud]
    E --> F[ La ruta adecuada procesa la petición]
    F --> G[ Python ejecuta la lógica del backend]
    G --> H[ Flask genera un template HTML]
    H --> I[ El servidor envía la response]
    I --> J[ El navegador aplica CSS y Bootstrap]
    J --> K[ El usuario visualiza el resultado]

Explicación:

El proceso comienza cuando el usuario escribe la dirección de la aplicación en el navegador. El navegador actúa como cliente y busca la dirección IP del equipo donde se encuentra la aplicación. Una vez localizada, establece la conexión con el servidor utilizando una combinación IP:puerto.

Si el usuario envía información mediante un formulario, el navegador envía una petición HTTP de tipo POST. Esta request llega al servidor, donde Flask la recibe y la dirige a la ruta correspondiente.

Dentro de la ruta se ejecuta el código desarrollado en Python, encargado de realizar el procesamiento necesario en el backend. Cuando el procesamiento termina, Flask utiliza un template para generar el documento HTML que contendrá el resultado.

Finalmente, el servidor devuelve una response al navegador. El frontend interpreta el HTML, aplica los estilos definidos mediante CSS y Bootstrap, y muestra la información procesada al usuario en pantalla.

## Evidencias de ejecución

- [Inicio](<capturas/INICIO.png>)
- [Empresa](<capturas/EMPRESA.png>)
- [Servicios](<capturas/SERVICIOS.png>)
- [Contacto](<capturas/CONTACTO.png>)
- [Compra](<capturas/CALCULADORA COMPRAS.png>)
- [Salario sin horas extra](<capturas/CALCULADORA SALARIO.png>)
- [Salario con horas extra](<capturas/salario desc.png>)
- [Conversión de temperatura](<capturas/CALCULADORA TEMPERATURA.png>)

## Interpretación de los cálculos

- **Compra sin descuento:** 5 artículos a $100 dan un subtotal de $500. Como no supera $1,000, no se aplica descuento y el total es $500. Para el caso de referencia, 5 artículos a $250 dan un subtotal de $1,250; el descuento del 10 % es $125 y el total es $1,125.
- **Salario sin horas extra:** 8 horas a $350 por hora dan $2,800; todas se pagan como horas normales.
- **Salario con horas extra:** 45 horas a $100 por hora se calculan como 40 horas normales ($4,000) y 5 horas extra al doble ($1,000), para un total de $5,000.
- **Temperatura:** la evidencia muestra 65 °C, equivalentes a 149 °F y 338.15 K. Para el caso de referencia, 25 °C equivalen a 77 °F y 298.15 K.