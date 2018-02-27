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

def get_today_price():
    '''
    return type: dict
    Example: {'open': 15, 'high': 16, 'low':14, 'close':15.5, 'volume': 154640}
    Note: This function can also be realized by calling get_history_price() and
    assigning today's date. 
    '''
    pass


#--------------------------------------------------------------------
from datetime import datetime
def datestr2date(datestr):
    '''
    two allowed format: "20170202" or "2017-02-02"
    return type: datetime object (date)
    '''
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

def get_history_price():
    '''
    input type: int(gvkey), dateObject(defined as above)
    return type: dict
    Example: {'open': 15, 'high': 16, 'low':14, 'close':15.5, 'volume': 154640}
    '''
    pass

def get_history_tech_ind():
    '''
    'technical indicator'
    input type: int(gvkey), dateObject(defined as above), 
    return type: dict
    Example: {'MA':70, "EMA": ..}    
    
    '''
    pass
