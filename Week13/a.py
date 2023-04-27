from abc import ABC

class Node(ABC):
    def __init__(self) -> None:
        self.__attibutes = {}
        self.__content: str = ""
        self.__children = []
    
    def html(self) -> str:
        pass

    def appendChild(child):
        pass

class Html(Node):
    def __init__(self, htmlAtts) -> None:
        super().__init__()
        self.__



def main():
    divAtts = {}
    divAtts['id'] = 'first'
    divAtts['class'] = 'foo'
    divA = Div('This is a test A', divAtts)
    divAtts = {}
    divAtts['id'] = 'second'
    divAtts['class'] = 'bar'
    divB = Div('This is a test B', divAtts)
    divAtts = {}
    divAtts['id'] = 'third'
    divAtts['class'] = 'dump'
    divC = Div('This is a test C', divAtts)

    b = B('This is a simple HTML file')
    divC.appendChild(b)
    body = Body()
    body.appendChild(divA)
    body.appendChild(divB)
    body.appendChild(divC)
    title = Title('Example')
    head = Head()
    head.appendChild(title)
    htmlAtts = {}
    htmlAtts['lang'] = 'en'
    html = Html('', htmlAtts)
    html.appendChild(head)
    html.appendChild(body)
    print(html.html())