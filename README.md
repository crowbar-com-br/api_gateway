# Corew API Gateway
API Gateway for the Corew project

## Implementation

### Dependencies

* python3
* python-virtualenv
* python-pip

### Installation
On your terminal:

1. Create a VirtualEnv:
```
$ virtualenv corew_api_gateway/
```
2. Go to the env folder:
```
$ cd corew_api_gateway/
```
3. Change your source:
```
$ source bin/activate
```
4. Clone the repository:
```
$ git clone https://github.com/crowbar-com-br/corew_api_gateway.git
```
5. Go to the project folder:
```
$ cd corew_api_gateway/
```
6. Install the necessary packages:
```
$ pip install -r requirements.txt
```

### Usage
On your terminal:

1. Go to the src folder:
```
$cd src/
```
2. Start the HUG server:
```
$hug -f app.py
```
Or, in case of production:
```
$gunicorn app:__hug_wsgi__
```
Or, if you have SLL:
```
$gunicorn --certfile=server.crt --keyfile=server.key app:__hug_wsgi__
```
