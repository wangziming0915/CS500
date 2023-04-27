class Container:

    def __init__(self, components: list[Component]) -> None:

        self.__components: list[Optional[Component]] = [None] * 10

 

    def add_component(self, index: int, component: Component):

        self.__components[index] = component

#The relastionship is composition. It is because the components object is initialized inside the container class.