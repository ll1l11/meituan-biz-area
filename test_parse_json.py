# -*- coding: utf-8 -*-
# import yaml  # pip install pyaml
import demjson

content = '{ format:"hierarchy" }'

# result = yaml.load(content)
result = demjson.decode(content)
print(result)
