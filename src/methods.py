# for the following functions
# input type: int(gvkey)

from datetime import datetime
import pandas as pd
from voluptuous import Schema, Required, MultipleInvalid


def get_company_name(**kwargs):
    """
    Example: "Murphy Oil Corporation"
    :return: string (official full name)
    """
    s = Schema({
        Required('df'): pd.DataFrame,
        'row_id': int
    })
    try:
        s(kwargs) # validate args
        df = kwargs['df']
        cpn_name = list(df.groupby('ticker')['Name'].head(1))
        row_id = kwargs['row_id']
        return cpn_name[row_id]
    except MultipleInvalid as e:
        print("error: {} occur while parse with required args".format(e.errors))



def get_company_tic(**kwargs):
    """
    Example: "MUR"
    :return: string (ticker)
    """
    s = Schema({
        Required('df'): pd.DataFrame,
        'row_id': int
    })
    try:
        s(kwargs)  # validate args
        df = kwargs['df']
        ticker = list(df.groupby('ticker')['ticker'].head(1))
        row_id = kwargs['row_id']
        return ticker[row_id]

    except MultipleInvalid as e:
        print("error: {} occur while parse with required args".format(e.errors))


def get_company_hq(**kwargs):
    """
    Example: "Cambridge, MA"
    :return: string (headquarter)
    """
    pass


def get_today_price(**kwargs):
    """
    Example: {'open': 15, 'high': 16, 'low':14, 'close':15.5, 'volume': 154640}
    Note: This function can also be realized by calling get_history_price() and
    assigning today's date.
    :return: dict
    """
    s = Schema({
        Required('df'): pandas.DataFrame,
        'row_id': int
    })
    try:
        s(kwargs)  # validate args

    except MultipleInvalid as e:
        print("error: {} occur while parse with required args".format(e.errors))


# --------------------------------------------------------------------


def datestr2date(**kwargs):
    """
    two allowed format: "20170202" or "2017-02-02"
    :param datestr:
    :return: datetime object (date)
    """
    try:
        return datetime.strptime(datestr, "%Y%m%d").date()
    except:
        pass
    try:
        return datetime.strptime(datestr, "%Y-%m-%d").date()
    except:
        print(
            "Error: input date string must be a valid date in two of the following formats: 'YYYYMMDD' or 'YYYY-MM-DD'")
        return None


# --------------------------------------------------------------------


def get_history_price(**kwargs):
    """
    input type: int(gvkey), dateObject(defined as above)
    return type: dict
    Example: {'open': 15, 'high': 16, 'low':14, 'close':15.5, 'volume': 154640}
    """
    s = Schema({
        required('df'): pandas.DataFrame,
        'date': datetime
    })
    try:
        s(kwargs)
        df = kwargs['df']
        date_ = kwargs['date']
        df = df.loc[df['date'] == date_]
        return dict(['open', df['open']], ['high', df['high']], ['low', df['low']], ['close', df['close']],
                    ['volume', df['volume']])
    except MultipleInvalid as e:
        print("error: input data is not valid".format(e.errors))
        return None




def get_history_tech_ind(**kwargs):
    """
    'technical indicator'
    input type: int(gvkey), dateObject(defined as above),
    Example: {'MA':70, "EMA": ..}
    :return: dict
    """
    s = Schema({
        required('df'): pandas.DataFrame,
        'date': datetime,
        'n': int
    })

    def MA(df, row_id, n):
        """
        Moving Average
        input type: pandas.DataFrame(df),int(row_id),int(n)
        n represents # days
        """
        try:
            df = df.iloc[row_id - n + 1:row_id + 1]
            return df.rolling_mean(df['close'], n)
        except:
            print ("Error:input is not valid")

    def EMA(df, row_id, n):
        """
        ExponentialMoving Average
        input type: pandas.DataFrame(df),int(row_id),int(n)
        n represents # days
        """
        try:
            df = df.iloc[row_id - n + 1:row_id + 1]
            return df.ewma(df['close'], n)
        except:
            print("Error: input is not valid")

    def ROC(df, row_id, n):
        """
        Rate of Change
        input type: pandas.DataFrame(df),int(row_id),int(n)
        n represents # days
        """
        try:
            df = df.iloc[row_id - n + 1:row_id + 1]
            return df['close'].diff(n - 1) / df['close'].shift(n - 1)
        except:
            print ("invalid input")

    try:
        s(kwargs)
        df = kwargs('df')
        date_ = kwargs('date')
        row_id = df[df['date'] == date_].index
        return dict(['MA_7days', MA(df, row_id, 7)], ['MA_30days', MA(df, row_id, 30)],
                    ['ROC_52week', ROC(df, row_id, 52 * 7)])
    except MultipleInvalid as e:
        print("error: input is not valid".format(e.errors))
