# Backend for the application
if you want to get familiar with the backend which is using fastapi and style transfer models to generate the output of the given image. First you need to create and activate a virtual environment.

```console
python3 -m venv .venv
source .venv/bin/activate
```
Then install the requirements with requirements.txt file

```console
pip install -r requirements.txt
```
Then you can run the main.py to check if your backend server is working at `localhost/8080`.

```console
python3 main.py
```
Or alternatively you can simply build and run a docker image from the Dockerfile.

```console
docker build -t backend .
docker run backend
```