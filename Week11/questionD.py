class Container:

    def __init__(self, components: list[Component]) -> None:

        self.__components: list[Component] = []

        for i in range(len(components)):

            self.__components.append(components[i])

#The relationship is Aggregation. Because the "components"'s life cycle will not end after the container object is collected. Also because the "components" is not initialized in the container class.