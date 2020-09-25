from flask import Flask, request
from Connection.neo_connection import Connect
from CreateNodes.create import Create
from CreateNodes.relational_nodes import RelationalNodes
from Delete.delete_all_data import DeleteAllData
from Delete.Delete_node import DeleteNode
from Read_all.get_all_nodes import GetNodes

service = Connect()
app = Flask(__name__)


@app.route("/create_node", methods=["POST"])
def create_node():
    my_node = Create()
    data = request.get_json()
    cre_node = my_node.create_nodes(data["unique_id"], data["name"], data["age"], data["gender"])
    return str(cre_node)


@app.route("/create_relation", methods=["POST"])
def create_relation():
    relation = RelationalNodes()
    data = request.get_json()
    cre_relation = relation.node_relation_type(data["relation_type"], data["person_a"], data["person_b"])
    return str(cre_relation)


@app.route("/delete_all_data", methods=['DELETE'])
def delete_all_data():
    clean_data = DeleteAllData()
    delete = clean_data.delete_all()
    return str(delete)


@app.route("/delete_a_node", methods=['DELETE'])
def delete_single_node():
    single_node_delete = DeleteNode()
    data = request.get_json()
    my_del = single_node_delete.single_node_delete(data['unique_id'], data['name'], data['age'], data['gender'])
    return str(my_del)


@app.route("/get_all_nodes", methods=['GET'])
def get_all_nodes():
    my_all_nodes = GetNodes()
    all_nodes = my_all_nodes.read_all_nodes()
    my_node_obj = []
    for node in all_nodes:
        my_node_obj.append(node)
    return str(my_node_obj)


if __name__ == "__main__":
    app.run()
