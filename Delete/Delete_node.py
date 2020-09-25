from Connection.neo_connection import Connect
session = Connect.connection()


class DeleteNode:
    def single_node_delete(self, unique_id, person_name, age, gender):
        return session.run(
            "MATCH (a: person{unique_id: $unique_id, name: $person_name, age: $age, gender: $gender}) DETACH DELETE a",
            unique_id=unique_id, person_name=person_name, age=age, gender=gender)


# my_obj = DeleteNode()
# res = my_obj.single_node_delete("Sant_id", "Santosh_muleva", 43, "Male")
# print("node_deleted")
