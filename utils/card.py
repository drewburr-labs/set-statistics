class Card():
    def __init__(self, attributes: "list[int]"):
        self.__attributes = attributes

    def __radd__(self, other):
        if other == 0:
            # Handle start of sum()
            return self.__attributes
        else:
            return self.__add__(other)

    def __add__(self, other):
        """
        Add attribues of another card of the same attribute size.
        Can add bare attributes list, if desired.
        """
        result: "list[int]" = []
        otherValues: "list[int]" = None
        if type(other) == type(self):
            # other is card
            otherValues = other.__attributes
        elif type(other) == type(result):
            # other is attributes list
            otherValues = other
        else:
            raise TypeError(
                "Unable to add type Card to type: " + str(type(other)))

        if len(self.__attributes) != len(otherValues):
            raise ValueError(
                f"Unable to add Card with different attributes. Got {str(len(otherValues))}, expected {str(len(self.__attributes))}")

        for a, b in zip(self.__attributes, otherValues):
            result.append(a+b)

        return result

    # def __iter__(self) -> "list[int]":
    #     return list(self.__attributes)

    # def __next__(self):
    #     return self.__iter__()

    def __copy__(self):
        return Card(self.__attributes)

    def __str__(self):
        return str(self.__attributes)

    def __repr__(self):
        return self.__str__()
