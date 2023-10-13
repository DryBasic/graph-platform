from schema import Schema, And, Use, Optional, SchemaError

global_schema = Schema({
    'node_types': [{
        'name': str,
        'id_dtype': str,
        'properties': [{
            'name': str,
            'dtype': str
        }],
        'edges': [{
            'name': str,
            'edge_partner': str
        }]
    }],
    'edge_types': [{
        'name': str,
        'direction': str,
        'has_inverse': bool,
        'from': str,
        'to': str,
        Optional('properties'): [{
            'name': str,
            'dtype': str
        }]
    }]
})
