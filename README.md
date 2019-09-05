# Py-chassis
Provides a chassis to build Python Micro-services
 
**API Doc:** https://app.swaggerhub.com/apis/deniojunior/py-chassis

---

### Configuration

A file named **config.yaml** must be created in the root folder containing the following configuration:

```
name: [PROJECT_NAME]
``` 

### Development

Next install dependencies using the following command for [Pipfile](https://github.com/deniojunior/py-chassis/blob/prod/Pipfile):
```bash
pipenv sync --dev --three
```

To run the application, you must use the following command:

```bash
pipenv run python run.py -c config.yaml
```

It's also possible to start the application with gunicorn:

```bash
pipenv run gunicorn -w 2 --timeout 3600 -b 0.0.0.0:8080 "app.server:create_app(config='config.yaml')"
```

### Tests
To run tests, at project path, execute: 

```bash
pipenv run coverage run --omit="tests/*" --include="app/*" --branch -m unittest discover -s tests/unit -p "*_test.py"
```

### Docker

Build docker image:

```bash
docker build -t py-chassis .
```

Run docker container:

```bash
docker container run -p 80:8080 -d --name microserivce py-chassis
```
