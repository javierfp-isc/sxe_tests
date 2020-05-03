# Repositorio sxe_tests

## Objetivo

Este repositorio contiene herramientas para la realización de tests en las tareas del módulo de SXE del ciclo de DAM

## Estructura del repositorio

**Este repositorio dispondrá de una rama (branch) para cada tarea a validar,** el nombre de la rama será un identificador ilustrativo de la tarea. Por ejemplo: la branch **implantacion_1** del repositorio será la asociada a la tarea identificada como implantacion_1, etc.

Por tanto deberemos descargar la branch adecuada. **Por ejemplo para ejecutar los tests de la tarea implantacion_1:**

`git clone -b implantacion_1 git@github.com:javierfp-isc/sxe_tests.git`

El mismo procedimiento se aplicaría a las demás tareas descargando la rama adecuada.

## Contenidos

### Módulo Odoo para ejecución de tests

Se ha creado un módulo de Odoo en el directorio **modulo/sxe_tests** el cual contiene:

#### Web Controller

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

#### Modelos asociados

Se creará un modelo por cada unidad, de este modo cada URL del controller estará asociada a una unidad (trozo de la URL que viene después de *sxe_tests*), cada unidad tendrá un modelo asociado donde se definirán los métodos de tests. Además los parámetros de cada método serán suministrados a través de la petición (vía GET, como en el ejemplo anterior, o vía POST)

Los modelos serán nombrados del modo siguiente: *tests.nombre_unidad*

Por ejemplo para la unidad de implantación el modelo asociado en Odoo a la realización de los tests es **tests.implantacion**

#### Instalación del módulo de Odoo para realizar los tests

Antes de nada hay que instalar el **módulo de Odoo sxe_tests** mencionado en el apartado anterior. El módulo se encuentra dentro del directorio **modulo** del repositorio, por tanto deberemos incorporar ese módulo en un directorio accesible desde el **addons_path** de la instancia de Odoo en el que lo vamos a instalar.

Supongamos que nuestro directorio de módulos de Odoo en el anfitrión es ~/odoo. Entonces ejecutamos:

`cp -r modulo ~/odoo/sxe_tests`

Por tanto en el addons path del container de Odoo, suponiendo que el directorio **~/odoo del anfitrión está mapeado en /opt/odoo/src**, pondríamos:

**addons_path=...,/opt/odoo/src/sxe_tests**

### Directorio de tests

En el directorio **tests** del repositorio nos encontramos la infraestructura para la realización de tests. Utilizaremos **ansible** para tal fin.

### Realización de los test

Los tests son un conjunto de pruebas que se lanzarán de forma automática en el escenario y que comprobarán si has realizado correctamente los pasos y ejercicios indicados en la práctica.

### Variables para la ejecución

Dentro del archivo **test.yaml**  hay una lista de variables que deberéis especificar para cada práctica. El tipo y número dependerá de la misma, pero como mínimo deberéis indicar vuestro **nombre** y **el token de acceso** a gitlab de vuestro usuario.

`#Variables que debe especificar el alumno`

`NOMBREALUMNO: Javier Fernández Peón`

`GITLABTOKEN: 9HMCTHQDCJAfeqsPjtzY`

*NOTAD que al ser formato YAML la sintaxis es del tipo clave: valor*

### Ejecución de los tests

Una vez instalado el módulo anterir para lanzar los test nos situamos dentro del directorio **tests** del repositorio y lanzamos desde la terminal el comando:

`ansible-playbook test.yaml`

Veremos en la salida del comando los mensajes de error si alguno de los test falla.

Si todo los tests se pasan con éxito al final del comando veremos un mensaje del tipo

**"ENHORABUENA!. Has superado todos los test"**

En caso contrario, si alguno falla el mensaje será:

**"LO SIENTO!. No has superado todos los test"**

por tanto deberás de revisar cual ha fallado y realizar las correcciones oportunas

### Archivos de log

Puedes ver también el resultado de la ejecución de los test, además de en la salida de la terminal, en los archivos

**log/test.log**: Toda la salida

**log/report.log**: Salida resumida y formateada para una lectura sencilla (en formato markdown)

## Entrega

Una vez que finalices correctamente la práctica, es decir con todos los test superados, para realizar la entrega de los resultados de ejecución de la misma deberás ejecutar el comando:

`ansible-playbook test.yaml -e entregar=yes`

Si hay algún error en los tests lo verás como se explica en el apartado anterior, **en cuyo caso la entrega no se realizará**

### Entrega forzada

Si quieres realizar la entrega **aún cuando algún test haya fallado** ejecuta el comando:

`ansible-playbook test.yaml -e entregar=yes -e force=yes`

