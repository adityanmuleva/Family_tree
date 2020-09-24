from Connection.neo_connection import Connect
session = Connect.connection()


class Create:
    def __init__(self, unique_id, person_name, age, gender):
        self.person_name = person_name
        self.age = age
        self.gender = gender
        self.unique_id = unique_id

    def create_nodes(self):
        return session.run("CREATE (a: person{unique_id: $unique_id, name: $person_name, age: $age, gender: $gender})",
                           unique_id=self.unique_id, person_name=self.person_name, age=self.age, gender=self.gender)


my_obj = Create("Sant_id", "Santosh_muleva", 43, "Male")
res = my_obj.create_nodes()
print("node_created")
