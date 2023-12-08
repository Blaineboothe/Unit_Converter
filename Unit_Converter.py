#Blaine Boothe 8/30/23
def convert_kg(kg):
    pd_2 = kg * 2.20462
    oc = kg * 35.274
    print(str(kg)+" kilograms converted is "+str(pd_2)+ " pounds and "+str(oc)+ " ounces.")
def convert_pounds(pd):
    kg_2 = pd * 0.453592
    oc_2 = pd * 16
    print(str(pd)+ " pounds converted is "+str(kg_2)+ " kilograms and "+str(oc_2)+ " ounces.")
def convert_ounces(oc):
    kg_3 = oc * 0.0283
    pd_2 = oc * 0.0625
    print(str(oc)+ " ounces converted is "+str(kg_3)+" kilograms and "+str(pd_2)+ " pounds.")

convert_kg(10)
convert_pounds(10)
convert_ounces(10)