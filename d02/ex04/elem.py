#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.
    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        return super().__str__().replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace('\n', '\n<br />\n')


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    class ValidationError(Exception):
        def __init__(self) -> None:
            super().__init__("Invalid type")

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):

        possible_errors = (not (self.check_type(content)
                           or content is None)) \
            or (tag_type != "double" and tag_type != "simple")
        if possible_errors:
            raise self.ValidationError

        self.tag = tag
        self.attr = attr
        self.content = []

        if content:
            self.add_content(content)

        self.tag_type = tag_type

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        tag = self.tag
        attr = self.__make_attr()
        content = self.__make_content()

        if self.tag_type == 'double':
            # se o tipo de tag for "double", adiciona o conteúdo entre as tags de abertura e fechamento
            result = "<{0}{1}>{2}</{0}>".format(tag, attr, content)
        elif self.tag_type == 'simple':
            # se o tipo de tag for "simple", retorna apenas a tag de abertura com os atributos
            result = "<{}{} />".format(tag, attr)

        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            if len(str(elem)) != 0:
                result += f"{elem}\n"
        result = "  ".join(line for line in result.splitlines(True))
        if len(result.strip()) == 0:
            return ""
        return result

    # método para adicionar conteúdo ao elemento
    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (
            isinstance(content, Elem)
            or type(content) == Text
            or (
                type(content) == list
                and all(
                    [type(elem) == Text
                     or isinstance(elem, Elem) for elem in content]
                )
            )
        )


if __name__ == '__main__':
    # Criação da estrutura HTML
    title = Text("Hello ground!")
    header1 = Text("Oh no, not again!")
    img_src = {"src": "http://i.imgur.com/pfp3T.jpg"}
    html = Elem("html", content=[
        Elem("head", content=Elem("title", content=[title])),
        Elem("body",
             content=[
                 Elem("h1", content=[header1]),
                 Elem("img", img_src, tag_type="simple"),
             ],
             ),
    ],
    )
    print(html)
