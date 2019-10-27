# pic_creator_micros_II_2019
Repositorio con el paquete IMCR para la generación de imágenes de prueba para el Proyecto del "do Semestre del 2019 del Curso Microcontroladores y Microprocesadores de la Carrea de Mecatrónica del Tecnológico de Costa Rica

Como usar:

1) De consola de linux:
  - Instalar el paquete con pip3 install git+https://github.com/RodolfoPiedraC/pic_creator_micros_II_2019
  - Digitar: micros_imcr PATH donde PATH es la dirección al json

2) Directamente de python:
  - Instalar el paquete con pip3 install git+https://github.com/RodolfoPiedraC/pic_creator_micros_II_2019
  - En una consola de python3 realizar:
    from micros_imcr import imcr_tool
    imcr_tool.micros_imcr_tool(PATH)
    NOTA: PATH es la dirección al json
