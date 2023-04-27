class Body(Node):
    def html(self):
        str = '<body'
        for k, v in self.attributes.items():
            str += ' ' + k + '="' + v + '"'
        str += '>'

        for c in self.children:
            