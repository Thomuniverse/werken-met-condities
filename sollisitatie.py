print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+      Sollicitatieformulier  "Circusdirecteur voor circus HotelDeBotel"    +
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Er wordt u een aantal relevante vragen gesteld...
Gelieve die naar eer en geweten in te vullen
Als blijkt dat u aan de criteria voldoet dan komt u in
aanmerking voor een serieus sollicitatiegesprek!
Ontspan maar blijf wakker, hier komen de vragen""")

name = input('Wat is uw naam?')
cm = int(input('Hoelang bent u?'))
sex = input('Bent u een man of vrouw? m/v')
kg = int(input('Hoe zwaar bent u?'))
input('Heeft u een huisdier? j/n')
hoed = input('Bent u in bezig van een hoge hoed? j/n')
overleven = input('Heeft u de certificaat "Overleven met gevaarlijk personeel"? j/n')
rijbewijs = input('Heeft u een geldig vrachtwagen rijbewijs? j/n')
diploma = input('Bent u in bezit van MBO-4 ondernemen diploma? j/n')
praktijk = input('''Heeft u Meer dan 4 jaar praktijkervaring met dieren-dressuur OF
meer dan 5 jaar ervaring met jongleren OF meer dan 3 jaar praktijkervaring met acrobatiek j/n''')
if sex == 'm':
	snor = input('Heeft u Snor breder dan 10 cm? j/n')
else:
	snor = input('Heeft u rood krulhaar langer dan 20 cm? j/n')

if cm >= 150 and kg >= 90 and hoed == 'j' and overleven == 'j' and rijbewijs == 'j' and diploma == 'j' and praktijk == 'j' and snor == 'j':
	print(f"""---------------------------------------------------------------------------------------------
|Beste {name},
|Proficiat! U komt in aanmerking voor een sollicitatiegesprek, stuur snel uw CV
---------------------------------------------------------------------------------------------""")
	input('Klik enter om uw cv te versturen')
else:
	print(f"""---------------------------------------------------------------------------------------------
|Beste {name},
|u voldoet niet aan onze strange eisen voor de functie van Circusdirecteur, het spijt ons!
---------------------------------------------------------------------------------------------""")
	input('Klik enter om het programma af te sluiten')
