
import json
import codecs
from jsonschema import validate


# load schema and json file 
schema_file = './graphson_schema.json'
schema = json.load( codecs.open(schema_file, 'r', encoding='utf-8') )

obj_file = './tests/normal_test_graph.json'
obj = json.load( codecs.open(obj_file, 'r', encoding='utf-8') )

# If no exception is raised by validate(), the instance is valid.
validate(obj, schema)

obj_file = './tests/extended_test_graph.json'
obj = json.load( codecs.open(obj_file, 'r', encoding='utf-8') )

# If no exception is raised by validate(), the instance is valid.
validate(obj, schema)

print 'passed!'