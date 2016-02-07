"""
Written by Bilal Ahmad Khan
Project: Discover Python (Python 2.7)
Taxes and Tip Calculator
"""

print "Welcome to the taxes and tip calculator!"					#Prints the given string
_priceBeforeTax=float(raw_input("What is the price before tax? "))	#Ask the user to input price before tax, convert it to float and save it to a variable
_taxes=float(raw_input("What are the taxes? (in %) "))				#Ask the user to input tax in percentage, convert it to float and save it to a variable
_tip=float(raw_input("What do you want to tip? (in %) "))			#Ask the user to input the tip, convert it to float and save it to a variable
_total=_priceBeforeTax+((_taxes*_priceBeforeTax)/100)				#Calculate resulting price after tax
_total=_total+((_total*_tip)/100)									#Calculate total price after tip
print "The price you need to pay is: $%.6f." % _total				#Print the result with 6 fixed decimal places
