'''
days = number of days invested
rate = Absolute Reutrn Rate
ini_nav = initial net asset value
curr_nav = current net asset value
start  = net asset value at beginning of the investment
end = net asset value at end of the investment
initial = initial investment amount
intrest = rate every period
'''
from datetime import datetime

def is_leap(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    else:
        return False        

"""
MUTUAL FUNDS
"""
# annulaize the retuns --  simple annualised return
def mutual_funds_simple_annualised_return(rate,days):
    try:
        if is_leap(datetime.now().year)  == True:
            true_days = 366
        else:
            true_days = 365    
        return (((1 + rate) ** (true_days/days)) - 1) * 100
    except Exception as error:
        print(error)

# holding period is less than 12 months -- point to point or absolute return
def mutual_funds_current_return(ini_nav,curr_nav):
    try:
        return ((curr_nav - ini_nav)/(ini_nav)) * 100
    except Exception as error:
        print(error)

# time period > 1 year -- Compound annual growth rate (CAGR)
def mutual_funds_cagr_y(start,end,years):
    try:
        return (((end/start) ** (1/years)) - 1) * 100
    except Exception as error:
        print(error)

def mutual_funds_cagr_m(start,end,months):
    try:
        return (((end/start) ** (12/months)) - 1) * 100
    except Exception as error:
        print(error)

def mutual_funds_cagr_d(start,end,days):
    try:
        return (((end/start) ** (365/days)) - 1) * 100
    except Exception as error:
        print(error)

def mutual_funds_lumpsum(initial,intrest,period):
    try:
        return (initial * ((1 + intrest) ** period) - initial) / 100
    except Exception as error:
        print(error)

"""
PPF
"""
def ppf(ppf_amt):
    return (ppf_amt*1.08)

"""
Fixed deposits
"""
def fd(time, inv_amt):
    if (time == 1):
        returns = {'Indusind Bank':inv_amt * 1.08, 'RBL Bank':inv_amt * 1.08, 'Lakshmi Vilas Bank':inv_amt * 1.0775, 'Karnataka Bank':inv_amt * 1.075, 'City Union Bank':inv_amt * 1.0735}
        return returns
        #print('\nFixed Deposit Return Ammounts: ')
        #for key in returns.keys():
        #    print(key, returns[key])

    elif (time == 2):
        returns = {'SBI Bank':inv_amt * 1.0805, 'PNB Bank':inv_amt * 1.0801, 'Raj Vilas Bank':inv_amt * 1.0785, 'IDFC Bank':inv_amt * 1.075, 'South Indian Bank':inv_amt * 1.076}
        return returns
        #print('\nFixed Deposit Return Ammounts: ')
        #for key in returns.keys():
        #    print(key, returns[key])

    elif (time == 3):
        returns = {'AU Small Finance Bank':inv_amt * 1.0824, 'DCB Bank':inv_amt * 1.0805, 'Bank of Baroda':inv_amt * 1.0785, 'Dena Bank':inv_amt * 1.076, 'HSBC Bank':inv_amt * 1.076}
        return returns
        #print('\nFixed Deposit Return Ammounts: ')
        #for key in returns.keys():
        #    print(key, returns[key])

    else:
        returns = {'Axis':inv_amt * 1.0777, 'Union Bank':inv_amt * 1.0775, 'Bank of India':inv_amt * 1.0785, 'Indian Overseas Bank':inv_amt * 1.075, 'Oriental Bank of India':inv_amt * 1.076}
        return returns
        #print('\nFixed Deposit Return Ammounts: ')       
        #for key in returns.keys():
        #    print(key, returns[key])            
