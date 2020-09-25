from Connection.neo_connection import Connect
session = Connect.connection()


class RelationalNodes:

    def node_relation_type(self, relation_type, person_a_name, person_b_name):
        if relation_type == "SON_OF":
            return session.run(
                "MATCH (a:person), (b: person) WHERE a.name = $person_a_name AND b.name = $person_b_name CREATE (a)-[:SON_OF]->(b)",
                person_a_name=person_a_name, person_b_name=person_b_name)
        elif relation_type == "DAUGHTER_OF":
            return session.run(
                "MATCH (a:person), (b: person) WHERE a.name = $person_a_name AND b.name = $person_b_name CREATE (a)-[:DAUGHTER_OF]->(b)",
                person_a_name=person_a_name, person_b_name=person_b_name)
        elif relation_type == "FATHER_OF":
            return session.run(
                "MATCH (a:person), (b: person) WHERE a.name = $person_a_name AND b.name = $person_b_name CREATE (a)-[:FATHER_OF]->(b)",
                person_a_name=person_a_name, person_b_name=person_b_name)
        elif relation_type == "MOTHER_OF":
            return session.run(
                "MATCH (a:person), (b: person) WHERE a.name = $person_a_name AND b.name = $person_b_name CREATE (a)-[:MOTHER_OF]->(b)",
                person_a_name=person_a_name, person_b_name=person_b_name)
        elif relation_type == "BROTHER_OF":
            return session.run(
                "MATCH (a:person), (b: person) WHERE a.name = $person_a_name AND b.name = $person_b_name CREATE (a)-[:BROTHER_OF]->(b)",
                person_a_name=person_a_name, person_b_name=person_b_name)
        elif relation_type == "SISTER_OF":
            return session.run(
                "MATCH (a:person), (b: person) WHERE a.name = $person_a_name AND b.name = $person_b_name CREATE (a)-[:SISTER_OF]->(b)",
                person_a_name=person_a_name, person_b_name=person_b_name)
        else:
            return "Incorrect_relation"

# my_obj = RelationalNodes()
# res = my_obj.node_relation_type("FATHER_OF", "Santosh_muleva", "Aaditya_muleva")
# print(res)
