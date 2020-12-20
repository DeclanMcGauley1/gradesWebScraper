from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

#locate all of the relevant paths and buttons for the webpage
PATH = "C:\Program Files (x86)\chromedriver.exe"
EMAILFIELD = (By.ID, "i0116")
PASSWORDFIELD = (By.ID, "i0118")
NEXTBUTTON = (By.ID, "idSIButton9")
NOBUTTON = (By.ID, "idBtn_Back")
GRADESBUTTON = (By.LINK_TEXT, "View Grades")


browser = webdriver.Chrome(PATH)
browser.get("https://canvas.swansea.ac.uk/")

# wait for email field and enter email
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys("mySchoolEmailLegitIPromise@school.ac.uk")
# Click Next
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
#wait for password field and enter password
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys("mySuperSecretUniPassword")
# Click Login
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
#clicks the no button on the confirmation pannel
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NOBUTTON)).click()
#Clicks on the view grades button
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(GRADESBUTTON)).click()

#a dictionary of all my courses and their corresponding row in the grades table
courses = {
    "cs230": 7,
    "cs250": 8,
    "cs270": 10,
    "cs205": 12
}


#opens the file and writes the correct information from each module
with open("D:\Atom Python\webScraping\Grades.txt", "w") as writer:
    for key in courses:
        course = browser.find_element_by_xpath(f"//table/tbody/tr[{courses[key]}]/td[1]")
        grade = browser.find_element_by_xpath(f"//table/tbody/tr[{courses[key]}]/td[2]")
        writer.writelines(course.text + "\n")
        writer.writelines(grade.text + "\n")

browser.quit()
