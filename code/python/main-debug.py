# encoding: utf-8

import json
import base64
import logging
import urllib

import json
import pymysql.cursors


LOG = logging.getLogger()

def tree():
    config = {
        'host': 'cn.srehub.com',
        'user': 'work',
        'password': 'work',
        'db': 'work',
        'charset': 'utf8',
        'cursorclass': pymysql.cursors.DictCursor,
        }
    cursor = pymysql.connect(**config)
#    cursor = db.cursor()
    cursor.execute("select * from tree;")
    datas = cursor.fetchall()
    tree = {}
    for data in datas:
       #print data
       tree['id'] = data[0]
       tree['name'] = data[1]
       tree['iconClass'] = data[2]
       tree['open'] = data[3]
       tree['children'] = data[4]
       # print tree
       break
    #print "Database version : %s " % data
    db.close()
    #return json.dumps(tree)
    return tree['id']


def spider(cip="118.28.8.8") :
    ipipurl = "http://freeapi.ipip.net/" + cip    
    sp = urllib.urlopen( ipipurl )
    ret = sp.read() 
    return ret

def handler(event, context):
    LOG.info('event: %s', event)
    evt = json.loads(event)

    clientIP = evt['headers']['X-Forwarded-For']
    runmode = evt['queryParameters']['runmode']
    ipinfo = spider( clientIP)
    ret = {'msg':'hello function compute.', 'lang':'python', 'clientIP': clientIP, 'ipinfo': ipinfo }
    if "debug" == runmode :
        #ret = {'msg':'hello function compute!', 'lang':'python'}
        #body = evt['body']
        ret = {'output': {'msg':'hello function compute.', 'lang':'python'}, 'input': evt}
    responseBody = json.dumps(ret)
    if evt['isBase64Encoded']:
        responseBody = json.loads(base64.b64decode(body))

    return {
        'statusCode': 200,
        'isBase64Encoded': False,
        'body': responseBody
    }
