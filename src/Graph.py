from schema import Schema, And, Or, Optional
from yaml import safe_load

ACCEPTED_TYPES = ("str", "int", "float")

class SafeDict:
    def __init__(self) -> None:
        pass

class Graph:
    def __init__(self):
        self._initialize_graph()

    def _initialize_graph(self):
        self.NodeTypes = {}
        self.EdgeTypes = {}
        self.nodes = {}
        self.edges = {}

    def load_schema_from_yaml(self, path: str):
        self._initialize()
        
        with open(path) as f:
            schema = safe_load(f)

        # validator.global_schema.validate(schema)
        elementTypes = self._linearize_schema(schema)
        for element, elementType in elementTypes:
            self.add_ElementType(element,
                label=elementType.get("label"),
                properties=elementType.get("properties"))
            
    def create_rdb_schema(self):
        rdb = {}
        for nodeType in self.NodeTypes:
            rdb[node.label]

    def add_ElementType(self, element:str, label:str, properties: dict=None):
        append_to = None
        match element:
            case "node":
                append_to = self.NodeTypes
            case "edge":
                append_to = self.EdgeTypes
            case _:
                raise ValueError(f'"{element}" not valid argument. Must be "node" or "edge"')
        

    def add_NodeType(self, label:str, properties: dict=None):
        nodeType = NodeType(label)
        if label not in self.NodeTypes:
            self.NodeTypes[label] = nodeType
        else:
            raise ValueError(f'NodeType of label "{label}" already exists.')

    def add_EdgeType():
        pass

    def add_node():
        pass

    def add_edge():
        pass

    @staticmethod
    def _linearize_schema(schema: dict):
        pass

    # def delete_node(self, key):
    #     self._delete("nodes", key)

    # def delete_edge(self, key):
    #     self._delete("edges", key)

    # def delete_NodeType(self, key):
    #     self._delete("NodeTypes", key)

    # def delete_EdgeType(self, key):
    #     self._delete("EdgeTypes", key)

    # def _delete(self, collection, key):
    #     delete_from = None
    #     match collection:
    #         case "nodes":
    #             delete_from = self.nodes
    #         case "edges":
    #             delete_from = self.edges
    #         case "NodeTypes":
    #             delete_from = self.NodeTypes
    #         case "EdgeTypes":
    #             delete_from = self.EdgeTypes
    #     delete_from.pop(key)


class ElementType:
    def __init__(self, label:str, properties: list=[]) -> None:
        self.label = label
        for property in properties:
            self._validate_property(property)
        self.properties = properties

    def _generate_schema(self) -> None:
        schema = Schema()
        self._schema = schema

    def _validate_element(self, data):
        if self.properties != self.schema_properties:
            self._generate_schema()

        self.schema.validate(data)
    
    @staticmethod
    def _validate_property(property):
        schema = Schema({
            'name': str,
            'dtype': And(str, lambda x: x in ACCEPTED_TYPES)
        })
        schema.validate(property)


class NodeType(ElementType):
    def __init__(self, label: str) -> None:
        super().__init__(label)


class EdgeType(ElementType):
    def __init__(self, label: str) -> None:
        super().__init__(label)

class Node:
    def __init__(self, nodeType):
        pass