
# SoundBoarding API assessment

This serves as instructions for setting up the API for the soundboarding API development assessment.

## Installation

This project requires python to be initially installed in your computer. Preferrably python version `3.13.9` or higher since this was the version used in developing the API.

If you already have python installed, and you prefer the dependency modules for the project to be installed in a virtual environment, you could run this command inside the `/backend` directory:

```
python -m venv venv
```

and run this command to enable the virtual environment:

Linux:
```
.\venv\Scripts\activate
```
Windows:
```
source venv/bin/activate
```

Now, make sure that you are in the `/backend` directory before we install the requirements using 
```
pip install -r requirements.txt
```
After all packages have been installed, make sure that you have the app.db under the backend directory (it should be there), otherwise, create a new db and name it app.db . Then start the API using the command:

```
uvicorn app.main:app
```

By default, this will run on port 8000. For the purpose of easier assessment, the default values of the settings/config file is already provided and .env is optional.

## Testing the API

We could test using either of the following:
- Swagger docs
- Postman

### Using Swagger Docs:

Go to any browser, then go the url `http://localhost:8000/docs`. Here you can see the list of all endpoints and their paramaters, body, headers as well as their schemas.

Some endpoints are protected (specifically the get and post for sessions) and require authentication before usage. You can initially create your own user using the `POST` `/users` and use the credentials to authenticate either via the authentication button (top right of the docs) or via the protected endpoint.

There is a `sampledata.json` provided in the directory which contains a few samples you can use for requesting to the API

