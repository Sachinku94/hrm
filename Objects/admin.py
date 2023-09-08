from selenium.webdriver.common.by import By

class AdminPage:
 def __init__ (self,driver):
     self.driver=driver
     
 adm= (By.XPATH,("//ul/li[@class='oxd-main-menu-item-wrapper'][1]"))    
 navigations=(By.XPATH,("//ul/li[@class='oxd-topbar-body-nav-tab --parent']"))
 dropdownsli=(By.XPATH,("//ul[@class='oxd-dropdown-menu']/li")) 
 def adim(self):
     return self.driver.find_element(*AdminPage.adm)
 def navigate(self):
     return self.driver.find_elements(*AdminPage.navigations)   
 def dropdown(self):
     return self.driver.find_elements(*AdminPage.dropdownsli)