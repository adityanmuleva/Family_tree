from Connection.neo_connection import Connect
session = Connect.connection()


class Create:
    def create_nodes(self, unique_id, person_name, age, gender):
        return session.run("CREATE (a: person{unique_id: $unique_id, name: $person_name, age: $age, gender: $gender})",
                           unique_id=unique_id, person_name=person_name, age=age, gender=gender)


# my_obj = Create()
# res = my_obj.create_nodes("Aadi_id", "Aaditya_muleva", 21, "Male")
# print("node_created")
