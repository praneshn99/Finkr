from calci import *
import sys, json

# FD_interest_rates = {'HDFC Bank':7.3, 'State Bank of India':6.8, 'Axis Bank':7.55, 'Punjab National Bank':6.85, 'Bank of India':6.65}
MF_interest_rates = {'HDFC Bank Short Term Cap':22.6, 'State Bank of India Savings MF':7.39, 'Axis Bank Equity Fund':20.81, 'Punjab National Bank Long Term Equity Fund':9.85, 'Bank of India': 7.86}
FD_interest_rates = {'Indusind Bank':1.08, 'RBL Bank':1.08, 'Lakshmi Vilas Bank':1.0775, 'Karnataka Bank':1.075, 'City Union Bank':1.0735, 'SBI Bank':1.0805, 'PNB Bank':1.0801, 'Raj Vilas Bank':1.0785, 'IDFC Bank':1.075, 'South Indian Bank':1.076,'AU Small Finance Bank':1.0824, 'DCB Bank':1.0805, 'Bank of Baroda':1.0785, 'Dena Bank':1.076, 'HSBC Bank':1.076,'Axis':1.0777, 'Union Bank':1.0775, 'Bank of India':1.0785, 'Indian Overseas Bank':1.075, 'Oriental Bank of India':1.076}
    

# function to read input from channel.js
def read_in():
    
    lines = sys.stdin.readlines()

    # Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])


def main():
	
	try:
		lines = read_in()

		# current investment return variables
		initial_nav = int(lines[0]['value'])
		current_nav = int(lines[1]['value'])
		rate_of_returns = int(lines[2]['value'])
		investment_period = int(lines[3]['value']) # days 

		
		present_nav = 0
		if investment_period//365 < 1:
			present_nav = mutual_funds_current_return(initial_nav, current_nav)
		else:
			present_nav = mutual_funds_simple_annualised_return(rate_of_returns, investment_period)
		
		# expected investment return variable
		start_nav = int(lines[4]['value'])
		end_nav = int(lines[5]['value'])
		investment_type = lines[6]['value']
		if lines[7]['value']:
			interest = int(lines[7]['value']) # only for lumpsum MF
		else:
			interest = False
		time_period = int(lines[8]['value']) # years

		expected_nav = 0
		if investment_type == 'SIP':
			expected_nav = mutual_funds_cagr_y(start_nav, end_nav, time_period)

			# comparing MF rates
			suggestions = {}
			for i in MF_interest_rates.keys():
				if MF_interest_rates[i] >= expected_nav:
					suggestions[i] = MF_interest_rates[i]
		
			if len(suggestions) == 0:
				print('\nSorry no suggestions found on Mutual Funds ! Your expected return rate was:',expected_nav)
			else:
				print('\nSuggestions on Mutual Funds are: ')
				for key in suggestions.keys():
					print(key, suggestions[key])
				print('\nYour expected return rate was: ',expected_nav)
		else:
			expected_nav = mutual_funds_lumpsum(start_nav, interest, time_period)
			print('\nYour expected return amount with LUMPSUM investment is: ',expected_nav)

		start_nav_1 = start_nav
		if start_nav < 150000:
			ppf_return = 0
			for i in range(1,time_period+1):
				ppf_return = ppf(start_nav)
				start_nav = ppf_return
			print('\nYour PPF return ammount is: ', ppf_return)	
		
		print('\nFixed Deposit Suggestions: ')
		returns = fd(time_period, start_nav_1)
		for key in returns.keys():
			returns[key] = returns[key]*(FD_interest_rates[key]**(time_period-1))

		for key in returns.keys():
			print(key, returns[key])

	except Exception as error:

		print('Caught Error: ', error)

if __name__ == '__main__':
	main()
