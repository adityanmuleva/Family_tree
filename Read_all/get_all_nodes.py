from Connection.neo_connection import Connect
session = Connect.connection()


class GetNodes:
    def read_all_nodes(self):
        return session.run("MATCH (n) RETURN n")


my_get_nodes = GetNodes()
res = my_get_nodes.read_all_nodes()
for nodes in res:
    print(nodes)
