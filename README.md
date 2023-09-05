# Health Universe - FastAPI Template 🚀

**Welcome to the [Health Universe](https://www.healthuniverse.com) community!**
Health Universe is an open-source cloud deployment platform and community for machine learning (ML) and AI from science to medicine.

This template provides a starter [FastAPI](https://fastapi.tiangolo.com) application deployable to Health Universe.

## Local Quickstart

In the root directory, open your console and run:
```console
pip install -r requirements.txt
```
Then, run the following command to start the application:
```console
uvicorn src.main:app --reload
```
Open up http://127.0.0.1:8000/docs in your browser to view the Swagger UI.
## Structure

This repository is organized into a modular structure to enhance maintainability and scalability.


```plaintext
{your_folder_name_here}/
    ├── src/
        ├── api_diagnostics/
        │   ├── router.py
        │   ├── schemas.py
        │   └── __init__.py
        ├── chads_vasc_score/
        │   ├── router.py
        │   ├── schemas.py
        │   ├── utils.py
        │   └── __init__.py
        ├── __init__.py
        ├── config.py
        └── main.py
```
