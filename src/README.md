# Trabajo de Inserción Profesional - UNQuiBOT (Backend) - 1° Cuatrimestre 2023

<img width="100" alt="Logo UNQuiBOT" src="https://user-images.githubusercontent.com/33500215/227559578-94249582-061f-4523-ad1c-a90873906388.png">

## Autores ✒️

* **Leonardo Di Carlo** - [leonardodicarlo](https://github.com/leonardodicarlo)
* **Mariana Velazquez** - [vqzmariana](https://github.com/vqzmariana)

***

### Deploy 🔧

_Para correr el software localmente debemos tener instalado tanto Python 3 como Flask y las librerías PyTorch y nltk._

_Primero, nos asegurarnos que tenemos Python 3 correctamente instalado (chequeo a través del Terminal):_

	$ python3 -V
	
	En caso de no tener la versión 3 de Python, correr los siguientes comandos:

	$ sudo apt-get update
	$ sudo apt-get -y upgrade
	
	Además, es recomendado tener instalado *pip* para manejar los paquetes:

	$ sudo apt-get install -y python3-pip
	
_Segundo, instalar la librería PyTorch, que es la que generará y entranará nuestra red neuronal:_


	$ pip3 install torch torchvision torchaudio
	
	
_Tercero, se debe instalar la librería nltk, que es la que procesará el lenguaje con el que se interactue:_

	$ pip3 install nltk
	
_Cuarto, se debe instalar Flask, lo cual levantará en http://127.0.0.1:5000/predict una aplicación en escucha:_

	$ pip3 install Flask
	$ pip3 install flask-cors
	
_Por último, se debe correr el archivo *train.py* al menos una vez, ya que este generará el archivo *data.pth*:_

	$ python3 train.py

***

### Ejecución 💻

_Primeramente se debe dejar ejecutado y corriendo nuestro chat backend:_

	$ python3 app.py
	
_Luego hay que asegurarse de que está corriendo el Front de la aplicación, el cual se encuentra disponible en el siguiente repositorio:_
	
	$ https://github.com/leonardodicarlo/UNQuiBOT-Frontend

_Esta aplicación generará los request hacia http://127.0.0.1:5000/predict, que es donde está escuchando nuestro backend._

***
