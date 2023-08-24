import os
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options 
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import pandas as pd

path = r"C:\Users\Ron\Desktop\selenium_drivers\geckodriver.exe"
service = Service(executable_path=path)


website = "https://in.indeed.com/jobs?q=data+analyst&l=India&vjk=6a5e66eb21630bf2"
driver = webdriver.Firefox(service = service)
driver.get(website)


joblist = []
containers = driver.find_elements(by="xpath", value='//div[@class ="job_seen_beacon"]')
for container in containers:
    try:
        data = {
            "job_title":container.find_element(by="xpath", value='./table[1]/tbody/tr/td/div[1]/h2').text,
            "company":container.find_element(by="xpath", value='./table[1]/tbody/tr/td/div[2]/span[1]').text,          
            "rating":container.find_element(by="xpath", value='./table[2]/tbody/tr[2]/td/div/span/span').text,                
            "location":container.find_element(by="xpath", value='./table[1]/tbody/tr/td/div[2]/div').text,
            "date":container.find_element(by="xpath", value= './table[2]/tbody/tr[2]/td/div/span').text
                        
        }
        print(data)
        # /html/body/main/div/div[1]/div/div/div[5]/div[1]/div[5]/div/ul/li[1]/div/div[1]/div/div[1]/div
        joblist.append(data)
    except IndexError:
        continue
    



df = pd.DataFrame(joblist)
print(df.head())
df.to_csv("jobsff.csv")
driver.quit()