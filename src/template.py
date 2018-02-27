import re
from src import methods


class Template():
    matches = None
    text = None

    def __init__(self, t):
        self.text = t
        self.matches = re.findall('\{.*?\}', text)

    def generate(self, row_id):
        res = self.text
        for name in self.matches:
            name = name[1:-1]
            if name == 'company_name':
                method_to_call = getattr(methods, 'get_' + name)
                para = method_to_call(word="hi")
                target = '{' + name + '}'
                print(target + " " + para)
                res = res.replace(target, para)

        return res


if __name__ == "__main__":
    t = None
    with open('./templates/template1.txt', 'r') as f:
        text = f.read()
        t = Template(text)
    print(t.generate(1))




