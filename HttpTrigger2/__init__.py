import logging
import random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

def num():
    numlist = random.sample(range(1,9), 5)
    return func.HttpResponse((numlist), status_code=200)