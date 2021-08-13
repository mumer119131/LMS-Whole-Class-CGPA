
from base_data import baseData
from main import *
import json

class_result = dict()
for i in baseData:
    
    result = lms_gpa_adder(i)
    cgpa = cgpa_cal(result)
    class_result[baseData[i]] = round(cgpa,2)
    with open("result.json","a+") as f:
        json.dump(class_result,f,indent=4)     

