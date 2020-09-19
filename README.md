# Data Engineer

## Dependencies

* [Docker](https://docs.docker.com/engine/install/)
* [Docker Compose](https://docs.docker.com/compose/install/)

## Tools

* [Direnv](https://direnv.net/)
* [Portainer](https://www.portainer.io/)
* [Pyenv](https://github.com/pyenv/pyenv)
* [pyenv-installer](https://github.com/pyenv/pyenv-installer)

## Running Services

Create and start containers. Option `-d` Detached mode: Run containers in the background.

```bash
docker-compose up -d
```

## Services

* Postgres running on port `5432`
* Pgadmin4 web-client for postgres. Running on port `8080`. [http://localhost:8080](http://localhost:8080)

### Postgres

| host      | port | user          | password      | database      |
|-----------|------|---------------|---------------|---------------|
| localhost | 5432 | data_engineer | data_engineer | data_engineer |

### Pgadmin4

| host      | port | email                   | password      |
|-----------|------|-------------------------|---------------|
| localhost | 8080 | data_engineer@email.com | data_engineer |

### Portainer

Install portainer local

```bash
docker run --name portainer --restart=unless-stopped -d \
    -p 8000:8000 -p 9000:9000 \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /opt/data/portainer_data:/data portainer/portainer
```

## Running scripts local

### Create a virtualenv

```bash
python -m venv .venv && source .venv/bin/activate
```

### Install and Update packages

```bash
pip install -U pip setuptools && pip install -r requirements.txt && pip install -r requirements-dev.txt
```

### Execute script

```bash
python data_engineer/app.py
  first_name  last_name              email
0       Jose      Silva     jose@email.com
1      Maria      Alves    maria@email.com
2    Antonio    Cardoso  antonio@email.com
3      Pedro      Silva    pedro@email.com
4     Carlos  Rodrigues   carlos@email.com
```
