from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, Callable

type K = float | int


class IData(ABC):
    @property
    @abstractmethod
    def key(self) -> K:
        ...


class EmptyTreeError(Exception):
    ...


@dataclass
class AVLTreeNode[T: IData]:
    data: T
    height: int = 1
    left: Optional['AVLTreeNode[T]'] = None
    right: Optional['AVLTreeNode[T]'] = None

    @property
    def key(self) -> int:
        return self.data.key


class AVLTree[T: IData]:
    def __init__(self):
        self._size: int = 0
        self._root: Optional[AVLTreeNode[T]] = None

    def __str__(self) -> str:
        result: list[str] = ["AVLTree\n"]
        if not self.is_empty():
            self.__create_str_tree(result, "", self._root, True)
        return "".join(result)

    @property
    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def __height(self, p: Optional[AVLTreeNode[T]]) -> int:
        if p is None:
            return 0
        return p.height

    def __balance_factor(self, p: Optional[AVLTreeNode[T]]) -> int:
        return self.__height(p.right) - self.__height(p.left)

    def __update_height(self, p: Optional[AVLTreeNode[T]]) -> None:
        left_height = self.__height(p.left)
        right_height = self.__height(p.right)

        p.height = left_height + 1 if left_height > right_height else right_height + 1

    def __rotate_right(self, p: AVLTreeNode[T]) -> AVLTreeNode[T]:
        q = p.left
        p.left = q.right
        q.right = p
        self.__update_height(p)
        self.__update_height(q)
        return q

    def __rotate_left(self, q: AVLTreeNode[T]) -> AVLTreeNode[T]:
        p = q.right
        q.right = p.left
        p.left = q
        self.__update_height(q)
        self.__update_height(p)
        return p

    def __balance(self, p: AVLTreeNode[T]) -> AVLTreeNode[T]:
        self.__update_height(p)

        if self.__balance_factor(p) >= 2:
            if self.__balance_factor(p.right) < 0:
                p.right = self.__rotate_right(p.right)
            return self.__rotate_left(p)

        if self.__balance_factor(p) <= -2:
            if self.__balance_factor(p.left) > 0:
                p.left = self.__rotate_left(p.left)
            return self.__rotate_right(p)

        return p

    def __insert(self, p: Optional[AVLTreeNode[T]], data: T) -> AVLTreeNode[T]:
        if p is None:
            return AVLTreeNode[T](data)
        if data.key < p.key:
            p.left = self.__insert(p.left, data)
        else:
            p.right = self.__insert(p.right, data)
        return self.__balance(p)

    def insert(self, data: T) -> None:
        self._root = self.__insert(self._root, data)
        self._size += 1

    def __find_minimum_root_node(self, node: Optional[AVLTreeNode[T]]) -> AVLTreeNode[T]:
        current_node = node.left
        if current_node is None:
            return node
        while current_node.left is not None:
            current_node = current_node.left

        return current_node

    def __remove_node_with_min_key(self, node: Optional[AVLTreeNode[T]]) -> AVLTreeNode[T]:
        if node.left is None:
            return node.right
        node.left = __remove_node_with_min_key(node.left)
        return self.__balance(node)

    def __remove(self, node: Optional[AVLTreeNode[T]], key: K) -> Optional[AVLTreeNode[T]]:
        if node is None:
            return None

        if key < node.key:
            node.left = self.__remove(node.left, key)
        elif key > node.key:
            node.right = self.__remove(node.right, key)
        else:
            q = node.left
            r = node.right
            if r is None:
                return q

            min_node = self.__find_minimum_root_node(r)
            min_node.right = self.__remove_node_with_min_key(r)
            min_node.left = q
            return self.__balance(min_node)

        return self.__balance(node)

    def remove(self, key: K) -> None:
        if self.is_empty():
            raise EmptyTreeError('tree is empty')

        _, is_found = self.find(key)
        if not is_found:
            raise KeyError(f'there is no item with key {key}')

        self._root = self.__remove(self._root, key)
        self._size -= 1

    def find(self, key: K) -> tuple[Optional[T], bool]:
        if self.is_empty():
            raise EmptyTreeError('tree is empty')

        current_node: AVLTreeNode[T] = self._root

        while current_node.key != key:
            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right

            if current_node is None:
                return None, False

        return current_node.data, True

    def get_min(self) -> T:
        if self.is_empty():
            raise EmptyTreeError('tree is empty')

        current_node: AVLTreeNode[T] = self._root
        last_node: Optional[AVLTreeNode[T]] = None

        while current_node is not None:
            last_node = current_node
            current_node = current_node.left

        return last_node.data

    def get_max(self) -> T:
        if self.is_empty():
            raise EmptyTreeError('tree is empty')

        current_node: AVLTreeNode[T] = self._root
        last_node: Optional[AVLTreeNode[T]] = None

        while current_node is not None:
            last_node = current_node
            current_node = current_node.right

        return last_node.data

    def __create_str_tree(
            self,
            result: list[str],
            prefix: str,
            node: Optional[AVLTreeNode[T]],
            is_tail: bool
    ):
        if node.right is not None:
            new_prefix = prefix
            if is_tail:
                new_prefix += "│   "
            else:
                new_prefix += "    "
            self.__create_str_tree(result, new_prefix, node.right, False)

        result.append(prefix)
        if is_tail:
            result.append("└── ")
        else:
            result.append("┌── ")
        result.append(str(node.key) + "\n")

        if node.left is not None:
            new_prefix = prefix
            if is_tail:
                new_prefix += "    "
            else:
                new_prefix += "│   "
            self.__create_str_tree(result, new_prefix, node.left, True)

    # ------------ симетричный обход дерева ------------
    def symmetric_traversal(
        self,
        func: Callable[[T], None]
    ) -> None:
        if self.is_empty():
            raise EmptyTreeError("EmptyTreeException")
        self.__symmetric_traversal(self._root, func)

    def __symmetric_traversal(
        self,
        local_root: Optional[AVLTreeNode[T]],
        func: Callable[[T], None]
    ) -> None:
        if local_root is not None:
            self.__symmetric_traversal(local_root.left, func)
            func(local_root.data)
            self.__symmetric_traversal(local_root.right, func)

    # ------------ Неупорядоченный обход ------------
    def traversal_after_processing(self, func: Callable[[T], None]) -> None:
        if self.is_empty():
            raise EmptyTreeError("EmptyTreeException")
        self.__traversal_after_processing(self._root, func)

    def __traversal_after_processing(
        self,
        local_root: Optional[AVLTreeNode[T]],
        func: Callable[[T], None]
    ) -> None:
        if local_root is not None:
            func(local_root.data)
            self.__symmetric_traversal(local_root.left, func)
            self.__symmetric_traversal(local_root.right, func)

    def traversal_before_processing(self, func: Callable[[T], None]) -> None:
        if self.is_empty():
            raise EmptyTreeError("EmptyTreeException")
        self.__traversal_before_processing(self._root, func)

    def __traversal_before_processing(self, local_root: Optional[AVLTreeNode[T]],
                                      func: Callable[[T], None]) -> None:
        if local_root is not None:
            self.__symmetric_traversal(local_root.left, func)
            self.__symmetric_traversal(local_root.right, func)
            func(local_root.data)


if __name__ == "__main__":
    ...
