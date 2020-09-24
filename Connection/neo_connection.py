from neo4j import GraphDatabase


class Connect:
    def connection(self=None):
        graphdb = GraphDatabase.driver(uri="bolt://127.0.0.1:7687", auth=("neo4j", "welcome123"))
        return graphdb.session()
