
# for the following functions
# input type: int(gvkey)
def get_company_full_name():
    '''
    return type: string (official full name)
    Example: "Murphy Oil Corporation"
    '''
    pass

def get_company_tic():
    '''
    return type: string (ticker)
    Example: "MUR"
    '''
    pass

def get_company_hq():
    '''
    return type: string (headquarter)
    Example: "Cambridge, MA"
    '''
    pass

def get_today_prices():
    '''
    return type: dict
    Example: {'open': 15, 'high': 16, 'low':14, 'close':15.5, 'volume': 154640}
    '''
    pass


#--------------------------------------------------------------------
from datetime import datetime
def datestr2date(datestr):
    """ two allowed format: "20170202" or "2017-02-02" """
    try:
        return datetime.strptime(datestr, "%Y%m%d").date()
    except:
        pass
    try:
        return datetime.strptime(datestr, "%Y-%m-%d").date()
    except:
        print("Error: input date string must be a valid date in two of the following formats: 'YYYYMMDD' or 'YYYY-MM-DD'")
        return None

#--------------------------------------------------------------------    
# for the following functions
# input type: int(gvkey), dateObject(defined as above)
def get_today_prices()