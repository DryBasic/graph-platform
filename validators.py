import yaml 


class GlobalSchema:
    """Object to load global_schema.yml

    * Takes schema yaml, loads to dict, validates against neo4j rules + config style (check example)
    * Holds methods for validating graph mappings against global schema
    """

    def __init__(self, path='./global_schema.yml', print_val_results=True) -> None:
        self.validation_results = []
        self.print_val_results = print_val_results
        with open(path) as file: 
            self.schema = yaml.safe_load(file)

        self.validate_schema()        

    def validate_schema(self) -> None:
        self.validation_state(
            lambda x: x == ('node_types', 'edge_types'),
            'Appropriate keys')(tuple(self.schema.keys()))
        
        names = []
        edges = []
        for node_type in self.schema.get('node_types'):
            self.validation_state(
                lambda x: x == ('name', 'id_dtype', 'properties', 'edges'),
                f'"{node_type.get("name")}" Appropriate keys')(tuple(node_type.keys()))

            if (name := node_type.get('name')) not in names:
                names.append(node_type)
            else:
                self.validation_state(lambda: False
                    , f'All unique node_type names {name}')()
                break

        
        if not all(self.validation_results):
            raise Exception("One or more test cases failed. ")

    def validate_mapping(self, map_path, map_type) -> bool:
        pass

    def validation_state(self, func, msg) -> function:
        def wrapper(*args, **kwargs):
            state_bool = func(*args, **kwargs)
            state = 'Pass' if state_bool else 'Fail'
            self.validation_results.append(state_bool)
            if self.print_val_results:
                print(f'{msg}: {state}')
        return wrapper


    

