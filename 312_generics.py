# non-generic
type IntOrStr = int | str

# generic
type ListOrSet[T] = list[T] | set[T]

class Box[T]:
    def __init__(self, item: T):
        self.item = item

    def get_item(self) -> T:
        return self.item
    
    def set_item(self, new_item: T) -> None:
        self.item = new_item

# generic function
def get_first_item[T](items: list[T]) -> T:
    return items[0]

def main() -> None:
    # ints
    int_box = Box(123)
    int_item = int_box.get_item()
    print(int_item)

    # strings
    str_box = Box("I'm a Generic!")
    str_item = str_box.get_item()
    print(str_item)

    # lists
    list_box = Box([1, 2, 3, 4])
    list_item = list_box.get_item()
    print(list_item)

    # generic
    first_item = get_first_item([1, 2, 3, 4])
    print(first_item)

if __name__ == "__main__":
    main()