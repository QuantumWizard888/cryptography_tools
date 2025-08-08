# CRYPTOGRAPHY TOOLS 🔐

## Minimalistic API tools (based on FastAPI) for hash generation and cryptography

CRYPTOGRAPHY TOOLS is an API-based minimalistic asynchronous (yeah) web application written in Python (FastAPI) for hash generation and other cryptogrphic needs.

Featues:

* **Hash generation**: SHA-256, SHA-512, Argon2
* **base64 encoding/decoding**
* **Random string generation**

It uses:

* **Framework**: FastAPI
* **Data validation**: pydantic
* **Cryptography**: base64, hashlib, secrets, argon2-cffi
* **ASGI HTTP Server**: Uvicorn
* **Tests**: pytest-asyncio, httpx

### 📦 Installation

1. Consider you already unpacked the app archive file. First you have to create virtual environment and activate it:
```
cd cryptography_tools
python3 -m venv .venv
. .venv/bin/activate
```
ℹ️ **NOTE**: If you want to make some changes to CRYPTOGRAPHY TOOLS - make it while virtual environment is activated. Don't forget to exit virtual environment after you finish your work:
```
deactivate
```

2. Install all required modules using:
```
pip install -r requirements
```

3. Run the application with this command:
```
python3 main.py
```

⚠️ **WARNING!**: Do not use this command for production environment! Escpecially the with ```reload = True``` option. In addition: most likely you have to adjust the way you run the application to your needs.

### 📚 How to?

After running the application you can access the documentation using this web address:
```
http://127.0.0.1:8000/docs
```

### ⚗️ Tests

To run tests simply execute this command while in the root diectory of the project:
```
python3 -B -m pytest -v tests/test_crypto_tools_core.py
```
