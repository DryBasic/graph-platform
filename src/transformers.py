import validators as val
import lib.GraphToRDB as g2r

class FormatTransformer:
    """"""
    def __init__(self, input_format: str, **kwargs):
        FORMATS = ('json', 'graph', 'rdb')
        if input_format not in FORMATS:
            raise ValueError(f'`{input_format}` not valid. Must be one of {FORMATS}')
        self.format = input_format

    def load_json(self, mappings: dict):
        pass

    def load_graph(self, mappings: dict):
        pass

    def load_relational(self, mappings: dict):
        pass
    
    def to_json(self):
        match self.format:
            case 'relational':
                self.relational_to_json()
            case 'graph':
                self.graph_to_json()
            case 'json':
                raise Exception('Data is already in json format')
            
    def to_graph(self):
        match self.format:
            case 'relational':
                self.relational_to_graph()
            case 'graph':
                raise Exception('Data is already in graph format')
            case 'json':
                self.json_to_graph()

    def to_relational(self):
        match self.format:
            case 'relational':
                raise Exception('Data is already in relational format')
            case 'graph':
                self.relational_to_graph()
            case 'json':
                self.relational_to_json()

    def graph_to_json(self):
        pass

    def graph_to_relational(self):
        """Generates a dict with the following keys pointing to a tuple of tuples:
        * nodeTypes(nodeID, nodeType)
        * edges(edgeID, edgeType), hasInverse)
        * nodeProperties(nodeID, propName, propDType, propValue)
        * edgeProperties(edgeID, propName, propDType, propValue)
        * connections(edgeID, fromNodeID, toNodeID)
        """
        pass

    def json_to_graph(self):
        pass

    def json_to_relational(self):
        """Generates a dict with the following keys pointing to a tuple of tuples:
        * nodeTypes(nodeID, nodeType)
        * edges(edgeID, edgeType), hasInverse)
        * nodeProperties(nodeID, propName, propDType, propValue)
        * edgeProperties(edgeID, propName, propDType, propValue)
        * connections(edgeID, fromNodeID, toNodeID)
        """
        pass

    def relational_to_graph(self):
        pass

    def relational_to_json(self):
        pass