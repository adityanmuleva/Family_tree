from Connection.neo_connection import Connect
session = Connect.connection()


class DeleteAllData:
    @staticmethod
    def delete_all():
        return session.run("MATCH (n) DETACH DELETE n")


my_obj = DeleteAllData.delete_all()
print("Database cleared")
