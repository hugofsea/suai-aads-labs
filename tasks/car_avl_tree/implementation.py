import json
from typing import Optional, TextIO, Any

from datastructures import AVLTree, AVLTreeNode
from datastructures.avl_tree import IData, K
from instances import Car


class CarWithKey(Car, IData):
    @property
    def key(self) -> K:
        return self.price


class CarAVLTree(AVLTree[CarWithKey]):
    def __to_dict(self, node: AVLTreeNode[CarWithKey]) -> Optional[dict[str, Any]]:
        if node is None:
            return None

        return {
            'data': node.data.model_dump(),
            'left': self.__to_dict(node.left),
            'right': self.__to_dict(node.right),
        }

    def dump(self, file: TextIO) -> None:
        json.dump(
            self.__to_dict(self._root),
            file,
            indent=4
        )

    @classmethod
    def load(cls, file: TextIO):
        avl_tree = cls()
        data: dict[str, Any] = json.load(file)
        stack = [data]

        while stack:
            item = stack.pop()

            if item is None:
                continue

            avl_tree.insert(CarWithKey(**item['data']))
            stack.append(item['left'])
            stack.append(item['right'])

        return avl_tree
