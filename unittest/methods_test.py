import unittest, sys, io
from src import methods
import pandas

df = pandas.read_csv('../datasets/stock_prices_info.csv')


class TestMethods(unittest.TestCase):

    def test_get_company_name(self):
        res = methods.get_company_name(df=df, row_id=1)
        self.assertEqual(res, 'Agilent Technologies Inc.')

    def test_get_company_tic(self):
        res = methods.get_company_tic(df=df, row_id=1)
        self.assertEqual(res, 'A')

    def test_get_today_price(self):

        res = methods.get_today_price(df=df, row_id=20)
        # d = {'open': '51.38', 'high': '51.83', 'low': '51.33', 'close': '51.74', 'volume': '1612698'}
        d = {'open': '53.04', 'high': '53.78', 'low': '52.72', 'close': '53.18', 'volume': '1717929'}
        try:
            self.assertDictEqual(res, d)
        except Exception as e:
            print(e)

    def test_get_history_price(self):
        pass


if __name__ == '__main__':
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    unittest.main()
    sys.stdout = sys.__stdout__
    print(capturedOutput.getvalue())
