# Tribunal Supremo Electoral TSE 
### Extraccion de Resultados Electorales 2019

---

## Requisitos

- __[Python3.6](https://medium.com/@moreless/install-python-3-6-on-ubuntu-16-04-28791d5c2167)__ - Este es un link donde puedes instalar python3.6.

---

## Pasos

1. Clona el repositorio en la carpeta deseada

```bash
git clone https://github.com/jinchuika/tse-scraper.git
```

2. Instalar pipenv

```bash
sudo pip3 install pipenv
```

3. Accediendo a la carpeta donde instalaste el proyecto `cd tse-scraper` instalar dependencias de python ```pipenv install```.

4. Para levantar el entorno virtual corre el comando

```
pipenv shell
```

5. En el documento `scraper.py` reemplazar las variables en por las rutas donde los archivos se guardaran 

```python
# obtén tu propio token desde la página del TSE
#https://resultados2019.tse.org.gt/201901/
token = ''

# la carpeta donde desees guardar los datos
output_folder_raw = ''

# la carpeta donde quieras guardar las imágenes
# dentro de esta carpeta debes crear otras 5 llamadas 0, 1, 2, 3, y 4
output_folder_images = ''
```

6. Por ultimo, para correr el scraper ejecuta el comando

```
python scraper.py
```
