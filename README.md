Utility movie_rating is a simple lookup to OMDBAPI for movie ratings given a movie name.  It can output ratings in the raw, json or csv format.  Default raw format will be used if output option is not specified.


### Setup on host

Install the Python library dependencies from requirement.txt file.
```
pip install -r requirements.txt
```

## Running Python CLI

The CLI requires that a valid OMDBAPI key be exported as environemnt variable OMDBAPI_KEY.

```
export OMDBAPI_KEY=<your valid OMDBAPI_KEY>
```

Executing the rating lookup from Python CLI:

```
python movie_rating.py rating <movie name> --output <raw/json/csv>
```


### Containerization

## Building the container
```
docker build -t movierating .
```

## Example running from continer

```
docker run -e OMDBAPI_KEY=<OMDBAPI_KEY> movierating Aquaman json
```
