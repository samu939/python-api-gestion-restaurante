# API Gestión de Restaurante 🍝

## Ejecución del proyecto:
🐳 Docker: 
```
docker compose up -d
docker ps
```
Una vez corrido el comando anterior, es necesario tener presente el código que se muestra en pantalla.(copiar el id en portapapeles del contenedor python-api-gestion-restaurante-server)
```
docker exec -i -t (id contenedor) /bin/bash
alembic upgrade head
```
La API se encontrará en la ruta:
```
http://localhost:8000
```
💻 Ambiente virtual:
```
python -m venv venv
pip install -r requirements.txt
```
Para ejecutar el servidor:
```
uvicorn main:app --reload
```
Para ejecutar pruebas:
```
pytest
```
