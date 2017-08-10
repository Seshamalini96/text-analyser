import os
import json
import io
from watson_developer_cloud import WatsonException 
from watson_developer_cloud import ToneAnalyzerV3
from os.path import join, dirname
tone_analyzer = ToneAnalyzerV3(
  version='2016-05-19',
  username='723c7035-8191-44b2-a57c-3c2d38862583',
  password='ZT2opDWzIeKU',
)

#with open(join(os.path.dirname(os.path.realpath(__file__)), 'exm.json')) as tone_json:
with open(join(dirname(__file__),'exm.json')) as tone_json:
 jsonobj = json.load(tone_json)
 leng=len(jsonobj["words"])
 wholesentence=" "
 for i in range (0, leng):
  wholesentence+=jsonobj["words"][i]["name"] + " "
 tone = tone_analyzer.tone(wholesentence, tones='emotion',
    content_type='text/plain')

print(json.dumps(tone, indent=2))

