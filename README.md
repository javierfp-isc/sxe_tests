# Tests de Odoo

## Objetivo

Este repositorio contiene herramientas para la realización de tests de Odoo para el módulo de SXE del ciclo de DAM

## Contenidos

Se ha creado el módulo de Odoo **sxe_tests** el cual contiene:

### Web Controller

Asociado a la URL: **sxe_tests/nombre_unidad**
Este servirá como punto de entrada para la realización de los tests. Veamos un ejemplo:

`http://localhost:8069/sxe_tests/implantacion/?login=admin&password=abc123.&metodo=test_modulo_instalado&modulo=account`

La URL anterior invoca al método *test_modulo* del modelo asociado a los tests de la unidad de nombre *implantacion*

Además se pasan los parámetros para el login de Odoo y la información necesaria para el método.

#### Respuestas del Web Controller

Los códigos de respuesta para interpretar los resultados devueltos por el Controller son:

- **EXITO**: Se ha pasado el test
- **FALLO**: No se ha pasado el test
- **ERROR**: Ha ocurrido algún error

### Modelos

Se creará un modelo por cada unidad, de este modo cada URL del controller estará asociada a una unidad (trozo de la URL que viene después de *sxe_tests*), cada unidad tendrá un modelo asociado donde se definirán los métodos de tests. Además los parámetros de cada método serán suministrados a través de la petición (vía GET, como en el ejemplo anterior, o vía POST)

Los modelos serán nombrados del modo siguiente: *tests.nombre_unidad*

Por ejemplo para la unidad de implantación el modelo asociado en Odoo a la realización de los tests es **tests.implantacion**

