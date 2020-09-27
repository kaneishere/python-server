import logging
import json
import xml.etree.ElementTree as ET

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

CIRCLE = "{http://www.w3.org/2000/svg}circle"
POLYLINE = "{http://www.w3.org/2000/svg}polyline"

@app.route('/bucket-fill', methods=['POST'])
def bucket_fill():
    data = request.get_data();
    root = ET.fromstring(data)
    logging.info("tree {}".format(root))
    children = []
    for child in root.iter('*'):
        children.append(child) 

    circles = []
    buckets = []
    pipes = []

    for child in children:
        if child.tag == CIRCLE:
            circles.append((int(child.attrib['cx']), int(child.attrib['cy'])))
        elif child.tag == POLYLINE:
            points = child.attrib['points'].split()
            if len(points) == 2:
                pipe = []
                for point in points:
                    x, y = map(int,point.split(','))
                    pipe.append((x,y))
                pipes.append(pipe)
            
            elif len(points) == 4:
                bucket = []
                for point in points:
                    x, y = map(int, point.split(','))
                    bucket.append((x,y))
                buckets.append(bucket)

    logging.info("circles: {}".format(circles))
    logging.info("buckets: {}".format(buckets))
    logging.info("pipes: {}".format(pipes))
                

    
    # print(data)
    # logging.info("data sent for evaluation {}".format(data))
    # data.sort() 
    # logging.info("My result :{}".format(data))
    # return json.dumps(data);
    return ""


