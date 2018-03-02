import re
from src import methods
import pandas as pd


class Template():
    matches = None
    text = None

    def __init__(self, t):
        self.text = t
        self.matches = re.findall('\{.*?\}', text)

    def generate(self, df, row_id):
        res = self.text
        for name in self.matches:
            target = name[1:-1]
            method_to_call = getattr(methods, 'get_' + target)
            para = method_to_call(df=df, row_id=row_id)
            print(name, para)
            res = res.replace(name, str(para))

        return res


if __name__ == "__main__":
    t = None
    with open('./templates/template1.txt', 'r') as f:
        text = f.read()
        t = Template(text)

    df = pd.read_csv('./datasets/stock_prices.csv')
    article = t.generate(df, 1)
    print(article)







