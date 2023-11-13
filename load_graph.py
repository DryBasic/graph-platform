import yaml
from string import Template
from neo4j import GraphDatabase

class CypherGen:
    def __init__(self) -> None:
        self.prop_template = Template('''\t${property}: row.${column}\n''')
        self.entity_template = Template('''
        LOAD CSV WITH HEADERS FROM "file:///${csvname}" AS row
        WITH row
        CREATE (:${label} ${properties});''')
        self.edge_template = Template('''
        LOAD CSV WITH HEADERS FROM "file:///${csvname}" AS row
        MATCH (n1:${from_label} {${from_id}:row.${from_col}}), (n2:${to_label} {${to_id}:row.${to_col}})
        CREATE (n1)-[:${label} ${properties}]->(n2);
        ''')

    def create_nodes_from_csv(self, csvname, label, properties=[]):
        ps = self._gen_properties(properties)
        create = self.entity_template.substitute(
            csvname=csvname, label=label,
            properties=ps
        )
        return create

    def create_edges_from_csv(self, csvname, label, from_label, from_id, from_col, to_label, to_id, to_col, properties=[]):
        ps = self._gen_properties(properties)
        create = self.edge_template.substitute(
            csvname=csvname,
            label=label,
            from_label=from_label,
            from_id=from_id,
            from_col=from_col,
            to_label=to_label,
            to_id=to_id,
            to_col=to_col,
            properties=ps
        )
        return create

    def _gen_properties(self, props: list|dict) -> str:
        if isinstance(props, list):
            props = {i:i for i in props}
        elif not isinstance(props, dict):
            raise TypeError("properties must be specified as a `list` or a `dict` of property_name, column_name mappings")

        properties =[]
        for prop, colname in props.items():
            properties.append(self.prop_template.substitute(
                property=prop, column=colname))
        

        pstring = ','.join(properties)
        if props:
            pstring = '{\n'+pstring+'}'
        return pstring

with open('config/neo4j_load_csv.yml') as f:
    neo_schema = yaml.safe_load(f)

gen = CypherGen()

with GraphDatabase.driver(neo_schema.get('URI'),
    auth=(neo_schema.get('USER'), neo_schema.get('PASS'))) as driver: 

    for node in neo_schema.get("nodes"):
        query = gen.create_nodes_from_csv(**node)
        driver.execute_query(
            query,
            database_="neo4j",  
        )

    for edge in neo_schema.get("edges"):
        query = gen.create_edges_from_csv(**edge)
        driver.execute_query(
            query,
            database_="neo4j",  
        )
    