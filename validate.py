
import json
import codecs
from jsonschema import validate

def loadJson(file):
	obj = json.load( codecs.open(file, 'r', encoding='utf-8') )
	return obj

# load schema and json file 
schema = loadJson('./graphson_schema.json')
obj = loadJson('./tests/normal_test_graph.json')
validate(obj, schema) # If no exception is raised by validate(), the instance is valid.

# load extended format json file
obj = loadJson('./tests/extended_test_graph.json')
validate(obj, schema)

# load stucco schema and stucco test file 
schema = loadJson('./stucco_schema.json')
obj = loadJson('./tests/stucco_test_graph.json')
validate(obj, schema)

# load another stucco test file
schema = loadJson('./tests/stucco_larger_test_graph.json')
validate(obj, schema)

print 'passed!'