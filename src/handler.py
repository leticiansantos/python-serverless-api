import json
import requests
from ddtrace import tracer
import time
import logging

# Set logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Using Automatic Instrumentation
def get_request_1():
    logger.info("Requesting cat ninja API")
    response = requests.get('https://catfact.ninja/fact')
    return response

# Using Decorator
@tracer.wrap(service="cat_service_2", resource="cat_facts_2")
def get_request_2():
    response = requests.get('https://catfact.ninja/fact')
    return response

# Using Context Manager
def get_request_3():
    with tracer.trace("cat_operation_3", service="cat_service_3", resource="cat_facts_3"):
        response = requests.get('https://catfact.ninja/fact')
    return response

# Using Manual
def get_request_4():
    span = tracer.trace("cat_operation_4", service="cat_service_4", resource="cat_facts_4")
    logger.info("Getting some sleep")
    time.sleep(.2)
    response = requests.get('https://catfact.ninja/fact')
    span.set_tag("custom_key", "custom_value") # Adding a custom span tag
    span.finish()
    return response

def hello(event, context):
    get_request_1()

    cat_facts = get_request_2()
    cat_facts_json = cat_facts.json()

    get_request_3()

    get_request_4()

    response = {"statusCode": 200, "body": json.dumps(cat_facts_json)}

    return response