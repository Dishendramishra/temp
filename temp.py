import numpy as np
from tabulate import tabulate
import sys

BEEF_MEAL = 16.95
CHICKEN_MEAL = 14.95
VEGAN_MEAL = 11.95

GRATUITY_RATE = 0.18

ROOM1_COST = 50.0
ROOM2_COST = 175.0

ROOM_TAX = 0.06

chicken_meals = int(input("Enter no. of chicken_meals: "))
beef_meals = int(input("Enter no. of beef_meals: "))
vegan_meals = int(input("Enter no. of vegan_meals: "))

total_seats = chicken_meals+beef_meals+vegan_meals

if total_seats <= 0:
    sys.exit("Total number of meals must be > 0 ")

tax_status = None
while True:
    tax_status = input("Tax exempted (Y/N): ")
    if tax_status.upper() in ["Y","N"]:
        break
    
room_cost = None
room_tax = 0
meals_cost = None
gratuity = None
grand_total = None

if total_seats <=50:
    room_cost = ROOM1_COST
else:
    room_cost = ROOM2_COST

if tax_status.upper() == "N":
    room_tax = room_cost*ROOM_TAX

meals_cost = chicken_meals*CHICKEN_MEAL +\
             beef_meals*BEEF_MEAL+\
             vegan_meals*VEGAN_MEAL

gratuity = meals_cost*GRATUITY_RATE

grand_total = room_cost+room_tax+meals_cost+gratuity

meals_qty = ""
meals_info = ""

if  chicken_meals >0:
    meals_qty += str(chicken_meals)+"x"+str(CHICKEN_MEAL)+" = $ "+str(round(chicken_meals*CHICKEN_MEAL,2))+"\n"
    meals_info += "Chicken meals"

if  beef_meals >0:
    meals_qty += str(beef_meals)+"x"+str(BEEF_MEAL)+" = $ "+str(round(beef_meals*BEEF_MEAL,2))+"\n"
    meals_info += "\nBeef meals"

if  vegan_meals >0:
    meals_qty += str(vegan_meals)+"x"+str(VEGAN_MEAL)+" = $ "+str(round(vegan_meals*VEGAN_MEAL,2))
    meals_info += "\nVegan meals"

bill = np.array([["Operator","John Wick"],
                ["Total No. of Guests",total_seats],
                ["Room Cost","$ "+str(round(room_cost,2))],
                ["Room Tax","$ "+str(round(room_tax,2))],
                [meals_info, meals_qty],
                ["Total Food Cost","$ "+str(round(meals_cost,2))],
                ["Gratutity","$ "+str(round(gratuity,2))],
                ["GRAND TOTAL","$ "+str(round(grand_total,2))]])

table = tabulate(bill,tablefmt="fancy_grid",numalign=u'decimal')
print(table)