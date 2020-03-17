from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

options = Options()
options.headless = False
driver = webdriver.Firefox(options=options, executable_path=r'/opt/geckodriver')


def create_task():

    driver.find_element_by_xpath("//a[@href='/Dashboard/Create']").click()
    create_header = driver.find_element_by_xpath("//h4").text
    if create_header == "Create New Task":
        print("Connected to create page.")
    else:
        print("Unable to connect to create page.")

    driver.find_element_by_xpath("//input[@name='TaskName']").send_keys("Contact COO of Microsoft.")
    driver.find_element_by_xpath("//input[@name='StartTime']").send_keys("03/17/2020, 12:40 PM")
    driver.find_element_by_xpath("//input[@name='Deadline']").send_keys("03/17/2020, 02:40 PM")
    driver.find_element_by_xpath("//input[@id='Important']").click()
    driver.find_element_by_xpath("//input[@id='HighComplexity']").click()
    driver.find_element_by_xpath("//input[@value='Create']").click()

    dashboard_title = driver.find_element_by_xpath("//h1").text
    if dashboard_title == "Dashboard":
        print("Task created successfully.")
    else:
        print("Unable to connect to dashboard")

    #matching_task = driver.find_element_by_xpath("//td[@class=]").text

    # if matching_task == "Contact COO of Microsoft.":
    #     print("Task successfully created.")
    # else:
    #     print("Unable to create task.")


def dashboard_connect():

    driver.find_element_by_xpath("//button[@id='dashboard']").click()
    dashboard_title = driver.find_element_by_xpath("//h1").text
    if dashboard_title == "Dashboard":
        print("Connected to dashboard")
    else:
        print("Unable to connect to dashboard")

    create_task()


def enter_credentials():

    print("Entering username and password")
    driver.find_element_by_xpath("//input[@name='username']").send_keys("test")
    driver.find_element_by_xpath("//input[@name='password']").send_keys("password")
    driver.find_element_by_xpath("//button[@id='submit']").click()
    welcome_page = driver.find_element_by_xpath("//h1").text
    if welcome_page == "Welcome":
        print("Login Successful. Connected to welcome page.")
    else:
        print("Unable to confirm successful login.")

    dashboard_connect()


def website_connect():

    print("Connecting to localhost.")
    driver.get('https://localhost:5001')

    page_header = driver.find_element_by_xpath("//h2").text
    if page_header == "Login Page":
        print("Connected to home page.")
        enter_credentials()
    else:
        print("Unable to reach home page.")



website_connect()

