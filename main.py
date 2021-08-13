#imports
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

over_all_result = list()

def lms_gpa_adder(ag):
    base_url_lms = "http://lms.uaf.edu.pk/login/index.php"
    driver=webdriver.Chrome(executable_path='F:\Outputs\Python Outputs\Web Scraping\Overall Result Compare\chromedriver.exe')
    #load the web browser
    driver.get(base_url_lms)
    #get the elements
    ag_no_field = driver.find_element_by_id("REG")
    search_btn = driver.find_element_by_xpath("/html/body/div[3]/div/section/div/div/div/div[4]/div[1]/div[2]/div/div[1]/form/div[2]/input[3]")
    #enter the ag no into the feild and serach
    ag_no_field.send_keys(ag)
    ActionChains(driver).click(search_btn).perform()
    rows = len(driver.find_elements_by_xpath("/html/body/table[2]/tbody/tr"))
    cols = len(driver.find_elements_by_xpath("/html/body/table[2]/tbody/tr[2]/td"))

    for i in range(2,rows+1):
        course_code = (driver.find_element_by_xpath("/html/body/table[2]/tbody/tr["+str(i)+"]/td[4]")).text.upper()
        total_marks = (driver.find_element_by_xpath("/html/body/table[2]/tbody/tr["+str(i)+"]/td[11]")).text.upper()
        credit_hrs = (driver.find_element_by_xpath("/html/body/table[2]/tbody/tr["+str(i)+"]/td[6]")).text.upper()
        credit_hrs = credit_hrs[0]
        sub_result = list()
        sub_result.append(course_code)
        sub_result.append(total_marks)
        sub_result.append(credit_hrs)
        over_all_result.append(sub_result)
        
        
    driver.close()
    return over_all_result

def cgpa_cal(result_list):
    oneCreditSet =[ [8, 1], [9, 1.5], [10, 2], [11, 2.33], [12, 2.67], [13, 3], [14, 3.33],
                    [15, 3.67], [16, 4]
            ];
    twoCreditSet =[ [16, 2], [17, 2.5], [18, 3], [19, 3.5], [20, 4], [21, 4.33], [22, 4.67],
                    [23, 5], [24, 5.33], [25, 5.67],
                    [26, 6], [27, 6.33], [28, 6.67], [29, 7], [30, 7.33], [31, 7.67], [32, 8]
            ];

    threeCreditSet = [ [24, 3],
            [25, 3.5], [26, 4], [27, 4.5], [28, 5], [29, 5.5], [30, 6], [31, 6.33], [32,
            6.67],
            [33, 7], [34, 7.33], [35, 7.67], [36, 8],
            [37, 8.33], [38, 8.67], [39, 9], [40, 9.33], [41, 9.67], [42, 10], [43,
            10.33],
            [44, 10.67], [45, 11], [46, 11.33], [47, 11.67],
            [48, 12]
    ];

    fourCreditSet = [ [32, 4],
            [33, 4.5], [34, 5], [35, 5.5], [36, 6], [37, 6.5], [38, 7], [39, 7.5], [40,
            8],
            [41, 8.33], [42, 8.67], [43, 9], [44, 9.33],
            [45, 9.67], [46, 10], [47, 10.33], [48, 10.67], [49, 11], [50, 11.33], [51,
            11.67],
            [52, 12], [53, 12.33],
            [54, 12.67], [55, 13], [56, 13.33], [57, 13.67], [58, 14], [59, 14.33], [60,
            14.67],
            [61, 15], [62, 15.33], [63, 15.67],
            [64, 16]
    ];

    fiveCreditSet = [ [40, 5], [41, 5.5], [42, 6], [43, 6.5], [44, 7], [45, 7.5], [46, 8],
                    [47, 8.5],
                    [48, 9], [49, 9.5], [50, 10], [51, 10.33], [52, 10.67], [53, 11], [54,
                    11.33],
                    [55, 11.67], [56, 12], [57, 12.33], [58, 12.67],
                    [59, 13], [60, 13.33], [61, 13.67], [62, 14], [63, 14.33], [64, 14.67], [65,
                    15],
                    [66, 15.33], [67, 15.67], [68, 16], [69, 16.33],
                    [70, 16.67], [71, 17], [72, 17.33], [73, 17.67], [74, 18], [75, 18.33], [76,
                    18.67],
                    [77, 19], [78, 19.33], [79, 19.67],
                    [80, 20]
            ];

    total_qp =float()
    total_credits = int()
    for i in range(0,len(result_list)):
            marks = int(result_list[i][1])
            credit_hr = int(result_list[i][2])

            total_credits  = total_credits + credit_hr
            if credit_hr == 1:
                    total_qp = total_qp + qpCalculator(marks,oneCreditSet)
                    continue
            elif credit_hr == 2:
                    total_qp = total_qp + qpCalculator(marks,twoCreditSet)
                    continue 
            elif credit_hr == 3:
                    total_qp = total_qp + qpCalculator(marks,threeCreditSet)
                    continue
            elif credit_hr == 4:
                    total_qp = total_qp + qpCalculator(marks,fourCreditSet)
                    continue
            elif credit_hr == 5:
                    total_qp = total_qp + qpCalculator(marks,fiveCreditSet)
                    continue

    cgpa = float(total_qp/total_credits)
    return cgpa               
def qpCalculator(marks,set_qp):
     qp = float()
     if marks < set_qp[0][0]:
        qp = 0
     elif marks > set_qp[1][0] and marks <= set_qp[len(set_qp)-1][0]:
        for i in range(0,len(set_qp)):
            if marks == set_qp[i][0]:
                qp = set_qp[i][1]
                break    
     elif marks > set_qp[len(set_qp)-1][0]:
             qp = set_qp[len(set_qp)-1][1]
     
     return qp
