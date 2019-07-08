import json
import os
import sys

import click
import requests


API_KEY = os.getenv('OMDBAPI_KEY', '')
if not API_KEY:
    print("OMDBAPI_KEY environment variable is missing")
    sys.exit(1)


OMDBAPI_ENDPOINT = 'http://www.omdbapi.com/?apikey={}'.format(API_KEY)


@click.group()
def cli():
    pass


@cli.command()
@click.argument('name')
@click.option('--output', default="raw", help="text(default), json, csv")
def rating(name, output):
    movie_url = "{}&t={}".format(OMDBAPI_ENDPOINT, name)
    result = requests.get(movie_url)

    d = json.loads(result.text)
    ratings = d.get('Ratings', [])

    if output.lower() == 'raw':
        print(ratings)
    elif output.lower() == 'json':
        print(json.dumps(ratings))
    elif output.lower() == 'csv':
        csv = ''
        for r in ratings:
            csv += '{},{}\n'.format(r.get('Source', ''), r.get('Value', ''))
        print(csv)
    else:
        print('Error: Unknown output format {}'.format(output))

if __name__ == '__main__':
    cli()
