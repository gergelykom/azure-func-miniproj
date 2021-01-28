import logging
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    num = requests.get('https://gregsmagicalminiproject.azurewebsites.net/api/HttpTrigger2?code=tM75WU1/ORVJeeRAogvqRyjCY6PeWEy3ZBTBJ93cVnQggfPbRH5u9Q==')
    lett = requests.get('https://gregsmagicalminiproject.azurewebsites.net/api/HttpTrigger3?code=/JfqhXeyRzErCq07pMk5n32PhJ0NJeLVrJGbG0ltS31/FtNWjNnvDA==')


return func.HttpResponse(str(num.text+lett.text), status_code=200)