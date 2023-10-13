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

    def validate_schema(self):
        # validate schema shape using "schema" package
        shape.global_schema.validate(self.schema)

        # validate referential properties in accordance with neo4j rules
        # 1: edges should be referenced by both partners 
        # 2: node types should be unique
        # 3: edge types should be unique
        for node in self.schema.get('node_types'):
            name = node.get('name')
            for edge in node.get('edges'):
                pass

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


    

