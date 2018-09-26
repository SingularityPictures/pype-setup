import toml
import unicode
import json
# TODO(jakub): jedno todo


class edict(dict):  # Similar to bunch, but less, and JSON-centric
    # based on class dotdict(dict):  # from http://stackoverflow.com/questions/224026/dot-notation-for-dictionary-keys

    __setattr__ = dict.__setitem__  # TBD: support assignment of nested dicts by overriding this?
    __delattr__ = dict.__delitem__

    def __init__(self, data):
        if type(data) in (unicode, str):
            data = json.loads(data)

        for name, value in data.iteritems():
            setattr(self, name, self._wrap(value))

    def __getattr__(self, attr):
        return self.get(attr, None)

    def _wrap(self, value):  # from class Struct by XEye '11 http://stackoverflow.com/questions/1305532/convert-python-dict-to-object
        if isinstance(value, (tuple, list, set, frozenset)):
            return type(value)([self._wrap(v) for v in value])  # recursion!
        else:
            if isinstance(value, dict):
                return edict(value)  # is there a relative way to get class name?
            else:
                return value


inf = 4
dictionary = {'table': {'key': 'value',
                        'subtable': {'key': 'another value'},
                        'inline': {'name': {'first': 'Tom', 'last': 'Preston-Werner'},
                                   'point': {'x': 1, 'y': 2}}},
              'x': {'y': {'z': {'w': {}}}},
              'string': {'basic': {'basic': 'I\'m a string. "You can quote me". Name\tJosé\nLocation\tSF.'},
                         'multiline': {'key1': 'One\nTwo',
                                       'key2': 'One\nTwo',
                                       'key3': 'One\nTwo',
                                       'continued': {'key1': 'The quick brown fox jumps over the lazy dog.',
                                                     'key2': 'The quick brown fox jumps over the lazy dog.',
                                                     'key3': 'The quick brown fox jumps over the lazy dog.'}},
                         'literal': {'winpath': 'C:\\Users\\nodejs\\templates',
                                     'winpath2': '\\\\ServerX\\admin$\\system32\\',
                                     'quoted': 'Tom "Dubs" Preston-Werner',
                                     'regex': '<\\i\\c*\\s*>',
                                     'multiline': {'regex2': "I [dw]on't need \\d{2} apples",
                                                   'lines': 'The first newline is\ntrimmed in raw strings.\n   All other whitespace\n   is preserved.\n'}}},
              'integer': {'key1': 99,
                          'key2': 42,
                          'key3': 0,
                          'key4': -17,
                          'underscores': {'key1': 1000, 'key2': 5349221, 'key3': 12345}},
              'float': {'fractional': {'key1': 1.0, 'key2': 3.1415, 'key3': -0.01},
                        'exponent': {'key1': 5e+22, 'key2': 1000000.0, 'key3': -0.02},
                        'both': {'key': 6.626e-34},
                        'underscores': {'key1': 9224617.445991227, 'key2': inf}},
              'boolean': {'True': True, 'False': False},
              'datetime': {'key1': 'datetime.datetime(1979, 5, 27, 7, 32, tzinfo="toml.TomlTz object at 0x10f814f98")',
                           'key2': 'datetime.datetime(1979, 5, 27, 0, 32, tzinfo="toml.TomlTz object at 0x10f81b470")',
                           'key3': 'datetime.datetime(1979, 5, 27, 0, 32, 0, 999999, tzinfo=" < toml.TomlTz object at 0x10f81b518 >" )'},
              'array': {'key1': [1, 2, 3],
                        'key2': ['red', 'yellow', 'green'],
                        'key3': [[1, 2], [3, 4, 5]],
                        'key4': [[1, 2], ['a', 'b', 'c']],
                        'key5': [1, 2, 3],
                        'key6': [1, 2]},
              'products': [{'name': 'Hammer', 'sku': 738594937},
                           {},
                           {'name': 'Nail', 'sku': 284758393, 'color': 'gray'}],
              'fruit': [{'name': 'apple',
                         'physical': {'color': 'red', 'shape': 'round'},
                         'variety': [{'name': 'red delicious'}, {'name': 'granny smith'}]},
                        {'name': 'banana', 'variety': [{'name': 'plantain'}]}]}

toml_formated = toml.dumps(dictionary)

print(toml_formated["table"])
