print("Type ja of nee")
true = str(input('Is de kaas geel?'))
if true == "ja":
	true = str(input('Zitten er gaten in?'))
	if true == "ja":
		true = str(input('is de kaas belachlijk duur?'))
		if true == "ja":
			print("Emmenthaler")
			input("Press enter to exit ;)")
		elif true == "nee":
			print("Leerdammer")
			input("Press enter to exit ;)")
	elif true == "nee":
		true = str(input('is de kaas hard als steen?'))
		if true == ("ja"):
			print("Pamigiano Reggiano")
			input("Press enter to exit ;)")
		elif true == ("nee"):
			print("Goudse kaas")
			input("Press enter to exit ;)")
elif true == "nee":
	true = str(input('Heeft de kaas blauwe schimmels?'))
	if true == "ja":
	    true = str(input('Heeft de kaas een korst?'))
	    if true == "ja":
	    	print("Camembert")
	    	input("Press enter to exit ;)")
	    elif true == "nee":
	    	print("Mozzarella")
	    	input("Press enter to exit ;)")
	elif true == "nee":
		  true = str(input('Heeft de kaas een korst?'))
		  if true == "ja":
		  	print("Blue de rochbaron")
		  	input("Press enter to exit ;)")
		  elif true == "nee":
		  	print("Foume d'Ambert")
		  	input("Press enter to exit ;)")