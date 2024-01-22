import abc
from typing import Sequence

from uniflow.op.op import Op
from uniflow.node import Node

class ReduceOp(Op):
    def __init__(self, name: str, _merge_func=None) -> None:
        '''Constructor of ExpandOp.
        
        Args:
            name (str): Name of the op.
            _merge_func (callable): Function to merge expand_1 and expand_2. 
                    Default merge function.
        '''
        super().__init__(name) 
        self._merge_func = _merge_func
    def __call__(self, expand1: Node, expand2: Node) -> Sequence[Node]:
        '''Call ReduceOp for merging two Nodes.
        
        Args:
            expand1 (Node): Input first Node.
            expand1 (Node): Input second Node.
            
        Returns:
            merge_node(Node): Merged version of expand1 and expand2.
        '''
        reduce_1_dict = {}
        if self._merge_func is None:
            for kv1, kv2 in zip(expand1.value_dict.items(), expand2.value_dict.items()):
                merge_key = f"{kv1[0]} {kv2[0]}"
                merge_value = f"{kv1[1]} {kv2[1]}"
                reduce_1_dict[merge_key] = merge_value       
            reduce_1 = Node("reduce_1", reduce_1_dict)     
        else:
            reduce_1 = self._merge_func
            
        return reduce_1