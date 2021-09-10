from typing import Generic, TypeVar
T = TypeVar("T")

ContentRow = list[T]
Sparse_List = dict[int, ContentRow]

tab_char = "\t"
return_char = "\n"


class SparseArray(Generic[T]):
    def __init__(self):
        self.myList: Sparse_List = {}

    def add_value_at(self, value: T, loc: int):
        if loc in self.myList:
            self.myList[loc].append(value)
        else:
            self.myList[loc] = [value]

    def __str__(self) -> str:
        output = ""
        for key in sorted(self.myList.keys()):
            output += f"{key}{tab_char}{self.myList[key][0]}"
            if len(self.myList[key]) > 1:
                output += f"{tab_char}{self.myList[key][1]}"
            output += return_char
        return output

    def values_at(self, index: int) -> ContentRow:
        if index in self.myList:
            return self.myList[index]
        else:
            return []
