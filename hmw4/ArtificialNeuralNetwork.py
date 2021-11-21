import random
import string

nodes_per_layer=[4,3,2]

class Node:
    def __init__(self):
        self.children=[]
        self.node_name=''.join([random.choice(string.ascii_letters) for i in range(3)])
        self.children_connection_weights=[]

    def make_children(self,current_layer, nodes_per_layer_map):
        #check for limits
        if current_layer >= len(nodes_per_layer_map):
            return

        #for each node, makechildren
        for i in range(nodes_per_layer_map[current_layer]):
            self.children.append(Node())

        #recursion
        self.children[0].make_children(current_layer+1, nodes_per_layer_map)

        #connect all childrens
        for i in range(1, len(self.children)):
            self.children[i].children = self.children[0].children[:]

    def print_names(self, current_layer, nodes_per_layer_map):
        indent='    ' * current_layer

        #check for limit
        if current_layer >= len(nodes_per_layer_map):
            print(f"{indent}{self.node_name}")
            return

        print(f"{indent}{self.node_name} is connected to: ")

        #print weights if true, else ignore
        for i in range(len(self.children)):
            try:
                print(f"{indent} Connection weight: {self.children_connection_weights[i]}")
            except:
                pass

            self.children[i].print_names(current_layer+1, nodes_per_layer_map)
   
    def make_connection_weight(self, current_layer, nodes_per_layer_map):
        #check for limits
        if current_layer >= len(nodes_per_layer_map):
            return

        self.children_connection_weights=[0.0] * len(self.children)

        #create random weights between 0-1 for each node
        for i in range(len(self.children)):
            self.children_connection_weights[i]=random.uniform(0, 1)
            self.children[i].make_connection_weight(current_layer+1, nodes_per_layer_map)
        return

#make node
new_node=Node()
#make nodes
new_node.make_children(0, nodes_per_layer)
new_node.print_names(0, nodes_per_layer)
#make weights
new_node.make_connection_weight(0, nodes_per_layer)
#print
new_node.print_names(0, nodes_per_layer)
