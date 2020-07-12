# Flask RESTPlus API POC (flask-resplus-api-poc)

## Usage

Clone the repo:

```console
$ git clone https://github.com/rsouza01/flask-resplus-api-poc/
$ cd flask-resplus-api-poc
```


Create and activate virtualenv:

```console
$ virtualenv -p python3 env
$ source env.sh
(env) $ pip3 install -r requirements.txt
```

Run the server via CLI

```console
(env) $ ./start-server.sh
```
    
And try the endpoints:

```console
(env) $ ./tests/start-tests.sh
```

## Testing

To run unit tests:

```console
(env) $ python -m unittest discover test/unit -v
```

For component tests:

```console
(env) $ python -m unittest discover test/component -v
```

## Author

**Rodrigo de Souza**

* Website: http://www.rodrigosouza.net.br
* Github: [@rsouza01](https://github.com/rsouza01)
* LinkedIn: [@rsouza01](https://linkedin.com/in/rsouza01)

## Show your support

Give a ⭐️ if this project helped you!


## [References](REFERENCES.md)


## License

flask-resplus-api-poc is released under the [MIT License](LICENSE).

