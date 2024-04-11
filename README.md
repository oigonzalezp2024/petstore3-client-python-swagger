
---

# Python Swagger Petstore3 - Cliente

***

El presente proyecto es un cliente de la API Petstore3,
que es la herramienta demostrativa que Swagger utiliza 
para exponer el potencial de sus funcionalidades de 
servicios web.

---

## Documentación técnica de la experiencia

***

### Configuración del entorno de desarrollo.
| Paso   | Descripción                       | comando                             |
| :----  | :----                             | :---                                |
| Paso 1 | Crear el entorno de trabajo.      | python -m venv env                  |
| Paso 2 | Activar el entorno de trabajo.    | ./env/Scripts/activate              |
| Paso 3 | Actualizar el gestor de paquetes. | python -m pip install --upgrade pip |
| Paso 4 | Instalar la librería setuptools.  | python -m pip install setuptools    |
| Paso 5 | Prepare la receta de librerías.   | python setup.py install          |
| Paso 6 | Ejecución de la demo.   | py demo1.py |

***

### Librerías del proyecto.
| librería  | Descripción                | Comando                           |
| :----     | :---                       | :---                              |
| pyAudio   | Permite trabajar con audio | pip install setuptools            |

Librerías mencionadas en requirements
<pre>
certifi >= 14.05.14
six >= 1.10
python_dateutil >= 2.5.3
setuptools >= 21.0.0
urllib3 >= 1.15.1
</pre>

Luego de la primera ejecución exitosa de setup.py, 
se ejecutó el siguiente comando para validar que 
librerías estaban presentes en ese momento:
> pip freeze > requirementsDemo.txt
<pre>
certifi==2024.2.2
python-dateutil==2.9.0.post0
six==1.16.0
swagger-client==1.0.0
urllib3==2.2.1
</pre>
---

### Realice sus pruebas, actualizaciones o modificaciones.
> Puedes actualizar, contribuir y mejorar el presente software, es libre. Licencia GNU v3.  
No esta permitido modificar la licencia de trabajos derivados de este proyecto.  
Por norma internacional debes conservar el mismo tipo de licencia.

#### Actualizar la receta.

Si agregas nuevas librerías al proyecto, no olvides actualizar la receta (requirementsDemo.txt). Recuerda que el cliente Swagger ya venía con un requirements.txt, personalmente recomiendo llevar un control de las librerías bastante detallado por separado:

``` CMD
pip freeze > requirementsDemo.txt
```

---

#### Comprobar que todo está en orden.
| Paso   | Descripción                                   | comando                               |
| :----  | :----                                         | :---                                  |
| Paso 1 | Desactive el entorno de trabajo.              | deactivate                            |
| Paso 2 | Elimine el entorno anterior. | rm -R env   |
| Paso 3 | Elimine el entorno anterior. | rm -R build |
| Paso 4 | Elimine el entorno anterior. | rm -R dist  |
| Paso 5 | Elimine el entorno anterior. | rm -R swagger_client.egg-info |
| Paso 6 | Cree un entorno de python.                    | python -m venv env                    |
| Paso 7 | Active el entorno de trabajo.                 | ./env/Scripts/activate                |
| Paso 8 | Actualice el gestor de paquetes.              | python -m pip install --upgrade pip   |
| Paso 9 | Instale la librería necesaria para operar. | python -m pip install setuptools       |
| Paso 10 | Prepare la receta de librerías.   | python setup.py install |
| Paso 11 | Realice pruebas de rutina. | py demo1.py |
| Paso 12 | Si genera error... | Cambiar el valor de <b>pet_id</b> en demo1.py por uno que sea valido. |
| Paso 13 | Para volver a probar | Ctrl + C |
| Paso 14 | Vuelva a ejecutar. | py demo1.py |
| Paso 15 | Finalice su gestión.                          | deactivate                            |

***
