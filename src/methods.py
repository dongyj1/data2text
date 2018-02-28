# for the following functions
# input type: int(gvkey)

from datetime import datetime
import pandas
from voluptuous import Schema, Required, MultipleInvalid


def get_company_full_name(**kwargs):
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
        kwargs
    except MultipleInvalid as e:
        print("error: {} occur while parse with required args".format(e.errors))
    pass


def get_company_tic(**kwargs):
    """
    Example: "MUR"
    :return: string (ticker)
    """
    pass


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
    pass


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
    pass


def get_history_tech_ind(**kwargs):
    """
    'technical indicator'
    input type: int(gvkey), dateObject(defined as above),
    Example: {'MA':70, "EMA": ..}
    :return: dict
    """
    pass
