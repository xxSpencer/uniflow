from flow import Flow
from uniflow.op.basic.expand_op import ExpandOp
from uniflow.op.basic.reduce_op import ReduceOp
from uniflow.node import Node
from typing import Any, Mapping, Sequence

class ExpandReduceFlow(Flow):
    def run(self, nodes: Sequence[Node]) -> Sequence[Node]:
    # def run(self, nodes):
        reduced_nodes = []
        for node in nodes:
        
            expand_op = ExpandOp("expander")
            expanded_nodes = expand_op(node)
            
            reduce_op = ReduceOp("reducer") 
            reduced_node = reduce_op(expanded_nodes)
        reduced_nodes.append(reduced_node)
        return reduced_nodes