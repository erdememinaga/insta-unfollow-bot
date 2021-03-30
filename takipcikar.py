from user import username, password,nickname
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



class Instagram():
    def __init__(self):
        f = open("user.txt", "r")
        user = f.readline()
        sifre = f.readline()
        hesap = f.readline()
      
        username = user.replace("kullanciadi:","")
        password = sifre.replace("sifre:","")
        nickname = hesap.replace("takipedilecekhesap:","")
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.username = username    
        self.password = password
        self.nickname = nickname
        
    try:
        def giris(self):
            self.browser.get('https://www.instagram.com/accounts/login')
            time.sleep(3)
            usernameinput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
            passwordinput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
            time.sleep(5)

            usernameinput.send_keys(self.username)
            passwordinput.send_keys(self.password)
            passwordinput.send_keys(Keys.ENTER)
            time.sleep(5)
        def hesabagit(self):
            self.browser.get(f"https://www.instagram.com/{self.username}/")
            time.sleep(5)
        def takip(self):
            postone = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a")
            postone.click()
            time.sleep(5)
            xs = 0
            for j in range(1000):
                    for i in range(1,12):
                        if i > 0:
                            
                            at = str(i)
                            #ak = f"body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child({at}) > div > div.Igw0E.rBNOH.YBx95.ybXk5._4EzTm.soMvl > button"
                            time.sleep(3)
                            #ak = str(ak)
                            #action = webdriver.ActionChains(self.browser)
                            #dialog = self.browser.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.isgrP")
                            c = self.browser.find_element_by_css_selector(f"body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child({at}) > div > div.Igw0E.rBNOH.YBx95.ybXk5._4EzTm.soMvl > button")
                            atr = c.value_of_css_property("color")      

                            
                            if i < 11:
                                if atr == "rgba(255, 255, 255, 1)":
                                    print("ZATEN TAKİPTEN ÇIKILMIŞ")
                            
                            
                                else:
                                    time.sleep(5)
                                    c.click()
                                    
                                    print("BİR KİŞİ DAHA TAKİPTEN ÇIKILDI")
                                    xs = xs + 1
                                    print("TOPLAM",xs," KİŞİ TAKİPTEN ÇIKILDI")
                                    
                                    try:
                                        a = self.browser.find_element_by_css_selector("body > div:nth-child(19) > div > div > div > div.mt3GC > button.aOOlW.-Cab_")
                                        if a:
                                            a.click()
                                    except:
                                        print("dewamke")
                                    
                                
                                    
                            elif i == 11:    
                                b = self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button")
                                b.click()
                                print("cikis")
                                self.browser.get(f"https://www.instagram.com/{self.username}/")

                                time.sleep(3)
                                insta.takip()

    except:
        print("bastan")
        insta.giris()   
       



insta = Instagram()
insta.giris()   
insta.hesabagit()
insta.takip()
