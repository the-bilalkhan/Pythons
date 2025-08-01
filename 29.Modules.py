# We Import Converter Modules From File "ConverterModules.py"

#import ConverterModules    #Use Whole Module Document By Importing Full Document

from ConverterModules import lbs_to_kg  #Use Specific Function Of Module By Importing Specific Function
from ConverterModules import kg_to_lbs  #Use Specific Function Of Module By Importing Specific Function

weight = kg_to_lbs(45)
print(weight)

weight = lbs_to_kg(45)
print(weight)
