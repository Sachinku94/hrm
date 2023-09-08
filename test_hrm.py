from Utilities.Baseclass import BaseClass
from Objects.admin import AdminPage
import time
class TestOne(BaseClass):
    def test_hrm(self):
        
   
        adminPage= AdminPage(self.driver)
        Adm=adminPage.adim()
        Adm.click()
        Click=adminPage.navigate()
        
        for clicks in Click:
          
         try:  
            clicks.click()
            time.sleep(4)
            drop=adminPage.dropdown()
            for drops in drop:
                drops.click()
         except Exception:
             () 
    