# Cron Job | Credenciales
Este repositorio busca guardar Cron Jobs para mantener API keys y access tokens actualizados.
En lugar de hostearlo en n8n y consumir créditos, está pensado para que se ejecute localmente mediante scripts ligeros en Python.

---

# Access Token Finnegans
El Access Token de Finnegans para acceder a la API tiene una *duración limitada*. Es desconocida su duración, pero aproximadamente tiene una validez de una hora. Para evitar hacer peticiones a la API cada vez que se haga una petición, **se pide un Access Token una vez por hora**, y se guarda en algún sitio accesible para los servicios que lo necesiten.

---

## Cómo levantar el servicio

Obtener las credenciales de OAuth 2.0 en la consola de Google Cloud habilitando la API de Google Sheets.
Para más información ver [aquí](https://developers.google.com/identity/oauth2/web/guides/get-google-api-clientid).

### macOS / Linux

```bash
# Crear el entorno virtual
python3 -m venv .venv

# Activar el entorno virtual
source .venv/bin/activate

# Instalar dependencias
pip install -r finnegans-accesstoken/requirements.txt

# Ejecutar el script
cd finnegans-accesstoken/
python refresh_token.py
```

### Windows (PowerShell)

```powershell
# Crear el entorno virtual
python -m venv .venv

# Activar el entorno virtual
.venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r finnegans-accesstoken\requirements.txt

# Ejecutar el script
cd finnegans-accesstoken\
python refresh_token.py
```

### Windows (CMD)

```cmd
:: Crear el entorno virtual
python -m venv .venv

:: Activar el entorno virtual
.venv\Scripts\activate.bat

:: Instalar dependencias
pip install -r finnegans-accesstoken\requirements.txt

:: Ejecutar el script
cd finnegans-accesstoken\
python refresh_token.py
```

> [!NOTE]
> La primera vez que ejecutes el script, se te abrirá el navegador pidiendo iniciar sesión y que se acepte la conexión con la aplicación de escritorio (este script).
> El resto de las veces funcionará sin problemas.
