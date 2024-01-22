import abc
from typing import Sequence

from uniflow.op.op import Op
from uniflow.node import Node

class ExpandOp(Op):
    def __init__(self, name: str, split_func=None) -> None:
        '''Constructor of ExpandOp.
        
        Args:
            name (str): Name of the op.
            split_func (callable): Function to split root node into expand_1 and expand_2. 
                    Default splits value_dict by half.
        '''
        super().__init__(name) 
        self._split_func = split_func
    def __call__(self, root: Node) -> Sequence[Node]:
        '''Call ExpandOp on root node.
        
        Args:
            root (Node): Input root node.
            
        Returns:
            List[Node]: expand_1 and expand_2 output nodes.
        '''
        if self._split_func is None:
            length = len(root.value_dict)
            half_length = length // 2

            # 分别创建两个新字典
            dict1 = {}
            dict2 = {}

            # 遍历排序后的键列表并将键值对添加到两个新字典中
            for i, key in enumerate(root.value_dict):
                if i < half_length:
                    dict1[key] = root.value_dict[key]
                else:
                    dict2[key] = root.value_dict[key]

            expand_1 = Node("expand_1", dict1)
            expand_2 = Node("expand_2", dict2)
        else:
            expand_1, expand_2 = self._split_func(root.value_dict)
            
        return [expand_1, expand_2]