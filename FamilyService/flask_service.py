from flask import Flask, request
from Connection.neo_connection import Connect
from CreateNodes.create import Create
from CreateNodes.relational_nodes import RelationalNodes
from

my_node = Create()
relation = RelationalNodes()


service = Connect()
app = Flask(__name__)


@app.route("/create_node", methods=["POST"])
def create_node():
    data = request.get_json()
    cre_node = my_node.create_nodes(data["unique_id"], data["name"], data["age"], data["gender"])
    return str(cre_node)


@app.route("/create_relation", methods=["POST"])
def create_relation():
    data = request.get_json()
    cre_relation = relation.node_relation_type(data["relation_type"], data["person_a"], data["person_b"])
    return str(cre_relation)


if __name__ == "__main__":
    app.run()
