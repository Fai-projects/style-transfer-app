# Style Transfer app Using Neural style transfer models
This is a webb app developed in python which uses the Neural style transfer models from ECCV 2016 paper named "perceptual losses for real-time style transfer and super-resolution". Initially we used opencv, fastapi and streamlit for styling, api and user interface. The following are the steps to run the app locally:

First clone the repository and download the style models by running 

```console
sh download_models.sh
```

These models will be saved in backend/models automatically. The next step is to run the app using docker (docker and docker-compose should be installed already) and you only need to run the docker-compose file with the following command:

```console
docker-compose up -d --build
```
This will built the docker images for both backend and frontend and you can use the app on the following url:

```console
http://localhost:8501/
```

Enjoy style transfer by providing a rgb image.