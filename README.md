# Trabajo de Inserción Profesional - UNQuiBOT (Backend) - 1° Cuatrimestre 2023

<img width="100" alt="Logo UNQuiBOT" src="https://user-images.githubusercontent.com/33500215/227559578-94249582-061f-4523-ad1c-a90873906388.png">

## Autores ✒️

* **Leonardo Di Carlo** - [leonardodicarlo](https://github.com/leonardodicarlo)
* **Mariana Velazquez** - [vqzmariana](https://github.com/vqzmariana)

***

### Deploy 🔧

_Para correr el software localmente debemos tener instalado tanto Python 3 como algún gestor de paquetes (recomendamos pip3)._

_Primero, con este repositorio clonado, se debe generar un entorno virtual ubicados dentro del Proyecto:_

	$ virtualenv unquibot_env
	
	Se genera un directorio nuevo, entonces:

	$ source unquibot_env/bin/activate

	
_Segundo, con nuestro entorno virtual activo, se deben instalar todas las dependencias a través del archivo requirements.txt:_


	$ pip3 install -r requirements.txt
	
	
_Tercero, se debe configurar en su IDE como archivo de entrada a app.py_
	
	
_Por último, se debe correr el archivo *train.py* al menos una vez, ya que este generará el archivo *data.pth*:_

	$ python3 train.py

***

### Ejecución 💻

	
_Hay que asegurarse de que está corriendo el Front de la aplicación, el cual se encuentra disponible en el siguiente repositorio:_
	
	$ https://github.com/leonardodicarlo/UNQuiBOT-Frontend

_Esta aplicación generará los request hacia http://127.0.0.1:5000/predict, que es donde está escuchando nuestro backend._

***
