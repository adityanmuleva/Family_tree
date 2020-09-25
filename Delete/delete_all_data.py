from Connection.neo_connection import Connect
session = Connect.connection()


class DeleteAllData:
    def delete_all(self=None):
        return session.run("MATCH (n) DETACH DELETE n")


# my_obj = DeleteAllData.delete_all()
# print("Database cleared")
