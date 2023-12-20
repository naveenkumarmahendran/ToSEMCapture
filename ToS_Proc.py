from time import sleep
from datetime import datetime
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager


def Tos_EM_Capture():

    print("ToS: Process Started: " + datetime.now().strftime("%m-%d-%Y, %H:%M:%S"))  # Start Time

    username = "rekhamusatda1"
    password = "Csenthil1121@1"
    url = "https://trade.thinkorswim.com/trade?symbol=SPX"

    BrowserOptions = webdriver.ChromeOptions()
    # BrowserOptions.add_argument('--headless')
    # BrowserOptions.add_argument('--disable-gpu')
    # BrowserOptions.add_experimental_option('excludeSwitches', ['enable-logging'])

    # driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe',options=BrowserOptions)
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=BrowserOptions)
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")

    driver.get(url)
    driver.maximize_window()

    driver.find_element_by_name("su_username").send_keys(username)
    driver.find_element_by_name("su_password").send_keys(password)
    driver.find_element_by_name("authorize").click()
    driver.find_element_by_class_name("alternates").click()

    driver.find_element_by_name("init_secretquestion").click()
    driver.find_element_by_name("su_secretquestion").send_keys("erode")
    driver.find_element_by_xpath("//div/input[@id='accept']").click()

    driver.find_element_by_xpath("//fieldset//div//div/label[@for='trustthisdevice0_1']").click()
    driver.find_element_by_name("authorize").click()

    sleep(5)

    driver.find_element_by_xpath("//*[@id='trade-page']/div/section[1]/button/span/h2").click()

    sleep(5)

    Opt_Expiry_Name = driver.find_element_by_xpath("//*[@id='trade-page']/div/section[1]/ul/li[2]/button/div[1]/div")

    if " AM " in Opt_Expiry_Name.text:
        Opt_Expiry_Name = driver.find_element_by_xpath("//*[@id='trade-page']/div/section[1]/ul/li[3]/button/div[1]/div")
        Opt_Expiry_EM = driver.find_element_by_xpath("//*[@id='trade-page']/div/section[1]/ul/li[3]/button/div[2]/div")
        Time_Stamp = datetime.now().strftime("%m-%d-%Y, %H:%M:%S")
    else:
        Opt_Expiry_Name = driver.find_element_by_xpath("//*[@id='trade-page']/div/section[1]/ul/li[2]/button/div[1]/div")
        Opt_Expiry_EM = driver.find_element_by_xpath("//*[@id='trade-page']/div/section[1]/ul/li[2]/button/div[2]/div")
        Time_Stamp = datetime.now().strftime("%m-%d-%Y, %H:%M:%S")

    Email_Message = Opt_Expiry_Name.text + " | " + Opt_Expiry_EM.text + " @ " + Time_Stamp.__str__()

    driver.quit()

    print(Email_Message)
    print("ToS: Process Completed: " + datetime.now().strftime("%m-%d-%Y, %H:%M:%S"))  # End Time
    return Email_Message
