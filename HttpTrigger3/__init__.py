import logging
import random
import string
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

def lett():
    return func.HttpResponse((random.sample(string.ascii_lowercase, 5)), status_code=200)