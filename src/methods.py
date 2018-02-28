# for the following functions
# input type: int(gvkey)

from datetime import datetime
import pandas

from voluptuous import Schema, Required, MultipleInvalid


def get_company_name(**kwargs):
    """
    Example: "Murphy Oil Corporation"
    :return: string (official full name)
    """
    s = Schema({
        Required('df'): pandas.DataFrame,
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
        Required('df'): pandas.DataFrame,
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
    :author: dyj
    :return: dict
    """
    s = Schema({
        Required('df'): pandas.DataFrame,
        Required('df'): pandas.DataFrame,
        'row_id': int
    })
    try:
        s(kwargs)  # validate args

    except MultipleInvalid as e:
        print("error: {} occur while parse with required args".format(e.errors))
        df = kwargs['df']
        row_id = int(kwargs['row_id'])
        data = df.iloc[[row_id]]
        dict_ = {'open': data['open'], 'high': data['high'], 'low': data['low'],'close': data['close'],
                 'volume': data['volume']}
        return dict_
    except MultipleInvalid as e:
        print("error: {} occur while parse with required args".format(e.errors))
    except TypeError as e:
        print("TypeError: ".format(e.errors))


# --------------------------------------------------------------------


def datestr2date(**kwargs):
    """
    two allowed format: "20170202" or "2017-02-02"
    :param datestr:
    :return: datetime object (date)
    """
    s=Schema({
        Required('datestr'):str
    })
    try:
        s(kwargs)
        datestr=kwargs['datestr']
        return datetime.strptime(datestr, "%Y%m%d").date()
    except:
        pass
    try:
        datestr = kwargs['datestr']
        return datetime.strptime(datestr, "%Y-%m-%d").date()
    except MultipleInvalid as e:
        print(
            "Error: input date string must be a valid date in two of the following formats: 'YYYYMMDD' or 'YYYY-MM-DD'".format(e.errors))
        return None


# --------------------------------------------------------------------


def get_history_price(**kwargs):
    """
    input type: int(gvkey), dateObject(defined as above)
    return type: dict
    Example: {'open': 15, 'high': 16, 'low':14, 'close':15.5, 'volume': 154640}
    """
    s=Schema({
        Required('df'):pandas.DataFrame,
        'date':datetime,
        'gvkey':int
    })
    try:
        s(kwargs)
        df= kwargs['df']
        date_=kwargs['date']
        gvkey=kwargs['gvkey']
        df=df.loc[df['date']==date_ and df['gvkey']==gvkey]
        return dict(['open',df['open']],['high',df['high']],['low',df['low']],['close',df['close']],['volume',df['volume']])
    except MultipleInvalid as e:
        print("error: input data is not valid".format(e.errors))
        return None
    s = Schema({
        Required('df'): pd.DataFrame,
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



def MA(**kwargs):
    """
    Moving Average
    input type: pandas.DataFrame(df),int(n)
    n represents # days
    """
    s = Schema({
        Required('df'): pandas.DataFrame,
        'n': int
    })
    try:
        s(kwargs)
        df=kwargs['df']
        n=kwargs['n']
        return df.rolling_mean(df['close'],n)
    except MultipleInvalid as e:
        print("error: input data is not valid".format(e.errors))
def EMA(**kwargs):
    """
    ExponentialMoving Average
    input type: pandas.DataFrame(df),int(n)
    n represents # days
    """
    s = Schema({
        Required('df'): pandas.DataFrame,
        'n': int
    })
    try:
        s(kwargs)
        df=kwargs['df']
        n=kwargs['n']
        return df.ewma(df['close'],n)
    except MultipleInvalid as e:
        print("error: input data is not valid".format(e.errors))
def ROC(**kwargs):
    """
    Rate of Change
    input type: pandas.DataFrame(df),int(n)
    n represents # days
    """
    s = Schema({
        Required('df'): pandas.DataFrame,
        'n': int
    })
    try:
        s(kwargs)
        df=kwargs['df']
        n=kwargs['n']
        return df['close'].diff(n-1)/df['close'].shift(n-1)
    except MultipleInvalid as e:
        print("error: input data is not valid".format(e.errors))
def get_history_tech_ind(**kwargs):
    """
    'technical indicator'
    input type: int(gvkey), dateObject(defined as above)
    Example: {'MA':70, "EMA": ..}
    :return: dict
    """
    s=Schema({
        Required('df'): pandas.DataFrame,
        'date': datetime,
        'n':int,
        'gvkey':int
    })
    try:
        s(kwargs)
        df=kwargs['df']
        date_=kwargs['date']
        gvkey=kwargs['gvkey']
        row_id=df[df['date']==date_ and df['gvkey']==gvkey].index
        return dict(['MA_7days',MA(df[row_id-6:row_id+1],row_id,7)],['MA_30days',MA(df[row_id-29:row_id+1],row_id,30)],['ROC_52week',ROC(df[row_id+52*7-1:row_id+1],row_id,52*7)])
    except MultipleInvalid as e:
        print("error: input is not valid".format(e.errors))

def ahead_behind(**kwargs):
    """
    select ahead or behind
    input type: int(gvkey)
    """
    s = Schema({
        Required('df'): pandas.DataFrame,
        'date': datetime,
        'n': int,
        'gvkey': int
    })
    try:
        s(kwargs)
        df = kwargs['df']
        date= kwargs['date']
        gvkey = kwargs['gvkey']
        return "ahead" if get_history_tech_ind(df,date,gvkey)['ROC_52week'] >0 else "behind"
    except MultipleInvalid as e:
        print("error: input data is not valid".format(e.errors))
def increase_decrease(**kwargs):
    """
    select increase or decrease
    input type:int(gvkey)
    """
    s = Schema({
        Required('df'): pandas.DataFrame,
        'date': datetime,
        'n': int,
        'gvkey': int
    })
    try:
        s(kwargs)
        df = kwargs['df']
        date= kwargs['date']
        gvkey = kwargs['gvkey']
        return "increase" if get_history_tech_ind(gvkey,df,date)['ROC_52week']>0 else "decrease"
    except MultipleInvalid as e:
        print("error: input data is not valid".format(e.errors))
