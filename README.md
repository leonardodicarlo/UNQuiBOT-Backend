# Trabajo de Inserción Profesional - UNQuiBOT (Backend) - 1° Cuatrimestre 2023

## Autores ✒️

* **Leonardo Di Carlo** - [leonardodicarlo](https://github.com/leonardodicarlo)
* **Mariana Velazquez** - [vqzmariana](https://github.com/vqzmariana)

***

### Deploy 🔧

_Para correr el software localmente debemos tener instalado tanto Python 3, como las librerías PyTorch y nltk._

_Primero, nos asegurarnos que tenemos Python 3 correctamente instalado (chequeo a través del Terminal):_

	```
	$ python3 -V
	```
	_En caso de no tener la versión 3 de Python, correr los siguientes comandos:_

	```
	$ sudo apt-get update
	$ sudo apt-get -y upgrade
	```
	_Además, es recomendado tener instalado *pip* para manejar los paquetes:_

	```
	$ sudo apt-get install -y python3-pip
	```
_Segundo, instalar la librería PyTorch, que es la que generará y entranará nuestra red neuronal:_

	```
	$ pip3 install torch torchvision torchaudio
	```
	
_Tercero, se debe instalar la librería nltk, que es la que procesará el lenguaje con el que se interactue:_

	```
	$ pip3 install nltk
	```
_Por último, se debe correr el archivo *train.py* al menos una vez, ya que este generará el archivo *data.pth*:

	```
	$ python3 train.py
	```
---
