#!/usr/bin/env python2
import sys
import json
import base64
import requests

try:
	print sys.argv[1]
except:
	print "You need to specify the image file name."
with open(sys.argv[1], "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

data = {
      'requests': [
        {
          'image': {
            'content': encoded_string
          },
          'features': [
            {
              'type': 'TEXT_DETECTION'
            }
          ]
        }
      ]
    }
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#https://cloud.google.com/vision/docs/auth
url = "https://vision.googleapis.com/v1/images:annotate?key=INSERT_API_KEY_HERE"
r = requests.post(url, data=json.dumps(data), headers=headers)
vision_data = r.json()
print vision_data['responses'][0]['textAnnotations'][0]['description']
