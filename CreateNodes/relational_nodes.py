from Connection.neo_connection import Connect
session = Connect.connection()


class RelationalNodes:
    def __init__(self, person_a_name, person_b_name):
        self.person_a_name = person_a_name
        self.person_b_name = person_b_name

    def relation_son_of(self):
        return session.run(
            "MATCH (a:person), (b: person) WHERE a.name = $person_a_name AND b.name = $person_b_name CREATE (a)-[:SON_OF]->(b)",
            person_a_name=self.person_a_name, person_b_name=self.person_b_name)

    def relation_daughter_of(self):
        return session.run(
            "MATCH (a:person), (b: person) WHERE a.name = $person_a_name AND b.name = $person_b_name CREATE (a)-[:DAUGHTER_OF]->(b)",
            person_a_name=self.person_a_name, person_b_name=self.person_b_name)

    def relation_father_of(self):
        return session.run(
            "MATCH (a:person), (b: person) WHERE a.name = $person_a_name AND b.name = $person_b_name CREATE (a)-[:FATHER_OF]->(b)",
            person_a_name=self.person_a_name, person_b_name=self.person_b_name)

    def relation_mother_of(self):
        return session.run(
            "MATCH (a:person), (b: person) WHERE a.name = $person_a_name AND b.name = $person_b_name CREATE (a)-[:MOTHER_OF]->(b)",
            person_a_name=self.person_a_name, person_b_name=self.person_b_name)

    def relation_brother_of(self):
        return session.run(
            "MATCH (a:person), (b: person) WHERE a.name = $person_a_name AND b.name = $person_b_name CREATE (a)-[:BROTHER_OF]->(b)",
            person_a_name=self.person_a_name, person_b_name=self.person_b_name)

    def relation_sister_of(self):
        return session.run(
            "MATCH (a:person), (b: person) WHERE a.name = $person_a_name AND b.name = $person_b_name CREATE (a)-[:SISTER_OF]->(b)",
            person_a_name=self.person_a_name, person_b_name=self.person_b_name)


my_obj = RelationalNodes("Aaditya_muleva", "Santosh_muleva")
res = my_obj.relation_son_of()
print(res)
