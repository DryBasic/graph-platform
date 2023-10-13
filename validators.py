import yaml
import gs_shape as shape

class GlobalSchema:
    """Object to load global_schema.yml

    * Takes schema yaml, loads to dict, validates against neo4j rules + config style (check example)
    * Holds methods for validating graph mappings against global schema
    """

    def __init__(self, path='./global_schema.yml') -> None:
        with open(path) as file: 
            self.schema = yaml.safe_load(file)

        self.validate_schema()

    def validate_schema(self) -> None:
        """
        Validates schema shape using the "schema" package.
        Validates referential properties of global schema in accordance with neo4j rules:
            1. Edges should be referenced by both partners
            2. Node types should be unique
            3. Edge types should be unique

        Will raise exception for validation failures.
        """
        shape.global_schema.validate(self.schema)

        node_tree = {i['name']:i for i in self.schema['node_types']}
        if len(set(node_tree.keys())) != len(node_tree):
            raise Exception('Duplicate node_type names')

        for node, attr in node_tree.items():

            edge_tree = {i['name'] for i in attr.get('edges')}

            for edge in attr.get('edges'):
                edge_name = edge.get('name')
                partner = edge.get('edge_partner')
                
                if partner not in node_tree:
                    raise Exception(f'"{node}" partner "{partner}" does not exist')
                partner_edges = node_tree[partner]['edges']
                if edge_name not in [i['name'] for i in partner_edges]:
                    raise Exception(f'"{node}" partner "{partner}" lacks edge {edge_name}')

    def validate_mapping(self, map_path, map_type) -> bool:
        pass

    # def validation_state(self, func, msg):
    #     def wrapper(*args, **kwargs):
    #         state_bool = func(*args, **kwargs)
    #         state = 'Pass' if state_bool else 'Fail'
    #         self.validation_results.append(state_bool)
    #         if self.print_val_results:
    #             print(f'{msg}: {state}')
    #     return wrapper


    

