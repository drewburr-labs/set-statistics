class Card():
    def __init__(self, attributes: "list[int]"):
        self.__attributes = attributes

    def __radd__(self, obj):
        if obj == 0:
            # Handle start of sum()
            return self.__attributes
        else:
            return self.__add__(obj)

    def __add__(self, obj):
        """
        Add attribues of another card of the same attribute size.
        Can add bare attributes list, if desired.
        """
        result: "list[int]" = []
        objValues: "list[int]" = None
        if type(obj) == type(self):
            # obj is card
            objValues = obj.__attributes
        elif type(obj) == type(result):
            # obj is attributes list
            objValues = obj
        else:
            raise TypeError(
                "Unable to add type Card to type: " + str(type(obj)))

        if len(self.__attributes) != len(objValues):
            raise ValueError(
                f"Unable to add Card with different attributes. Got {str(len(objValues))}, expected {str(len(self.__attributes))}")

        for a, b in zip(self.__attributes, objValues):
            result.append(a+b)

        print(f"Card sum result: {result}")
        return result

    # def __iter__(self) -> "list[int]":
    #     return list(self.__attributes)

    # def __next__(self):
    #     return self.__iter__()

    def __copy__(self):
        return Card(self.__attributes)
