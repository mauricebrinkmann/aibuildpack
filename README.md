# aibuildpack
AI Buildpack: Enable AI@CF

## Buildpack

1. mkdir hack
2. cd hack
3. vi ai.json
4. cf push hack -b https://github.com/mauricebrinkmann/aibuildpack.git <https://github.com/mauricebrinkmann/aibuildpack.git>

## API

To start api only:

1. `sudo pip install -U Flask`
2. `cd api`
3. `python server.py`

### Flask

https://flask.palletsprojects.com/en/1.1.x/quickstart/
