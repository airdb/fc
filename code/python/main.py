# encoding: utf-8

import json
import base64
import logging

LOG = logging.getLogger()

def handler(event, context):
    LOG.info('event: %s', event)
    evt = json.loads(event)

    #body = evt['body']
    ret = {'msg':'hello function compute.', 'type':'fc', 'input': evt}
    responseBody = json.dumps(ret)
    if evt['isBase64Encoded']:
        responseBody = json.loads(base64.b64decode(body))

    return {
        'statusCode': 200,
        'isBase64Encoded': False,
        'body': responseBody
    }
