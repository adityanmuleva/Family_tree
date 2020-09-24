from Connection.neo_connection import Connect
session = Connect.connection()


class DeleteNode:
    def __init__(self, unique_id, person_name, age, gender):
        self.unique_id = unique_id
        self.person_name = person_name
        self.age = age
        self.gender = gender

    def single_node_delete(self):
        return session.run("MATCH (a: person{unique_id: $unique_id, name: $person_name, age: $age, gender: $gender}) DETACH DELETE a",
                           unique_id=self.unique_id, person_name=self.person_name, age=self.age, gender=self.gender)


my_obj = DeleteNode("Sant_id", "Santosh_muleva", 43, "Male")
res = my_obj.single_node_delete()
print("node_deleted")
