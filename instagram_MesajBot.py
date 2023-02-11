"""
Kodların çalışması için 'Firefoxun son sürümü',
'Selenium Kütüphanesi' ve Firefox için webdriver olan 'geckodriver' indirmeniz gerekiyor ve indirdiğiniz exe dosyasını bilgisayarınız Path'ine eklemeniz gerekiyor.
Uygulama çalışırken elle müdahale gerekmeyecektir.
Programı kullanmadan önce kodun içerisindeki YourUserName kısmına Kullanıcı adınızı ve YourPassword kısmına şifrenizi girmeyi unutmayınız.
"""

#----------------------------------------------------------------------------------------------------------

from selenium import webdriver
import time
#Gerekli Kütüphaneler Ekleniyor.
#Otomatize işlemleri için Selenium Webdriver
#Ve tarayıcı yüklenirken işlemleri bekletmek için time kütüphanesi
browser = webdriver.Firefox()

browser.get("https://www.instagram.com")
#Web browser ataması yapılıp instagram adresine gidiliyor
time.sleep(2)
#Adres yüklenirken diğer komut işletilmeyip 2 saniye bekleniyor


username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")
#Kullanıcı adı ve parola alanlarına erişim sağlanıyor ve değişkene atanıyor.

username.send_keys("YourUserName")
password.send_keys("YourPassword")
# YourUserName yazan yeri kullanıcı adınızla değiştirin
# YourPassword yazan yeri parolanızla değiştirin
#kullanıcı adı ve parolaya Değerler gönderiliyor

time.sleep(1)
#sayfa bekletiliyor ki devam eden işlemler
#önceki kodun gönderdiği derğerler yerine yazılmadan yapılmasın


login = browser.find_element_by_css_selector(".L3NKy > div:nth-child(1)")
login.click()
time.sleep(4)
#Login butonu bulunup tıklama komutu gönderiliyor
#ve giriş yapılana kadar beklemesi sağlanıyor

kaydetme = browser.find_element_by_css_selector("button.sqdOP:nth-child(1)")
kaydetme.click()
time.sleep(2)
#Giriş bilgilerini kaydetme sorgusuna kaydetme butonuna tıklanarak cevap veriliyor

simdidegil = browser.find_element_by_css_selector("button.aOOlW:nth-child(2)")
simdidegil.click()
time.sleep(2)
#İnstagramın sorduğu giriş bilgilerini kaydet sorgusuna şimdi değil tıklaması yapılıyor

dmkutu = browser.find_element_by_css_selector(".xWeGp > svg:nth-child(1)")
dmkutu.click()
time.sleep(2)
#Dm kutusu bulunup tıklannıyor.

ilkMesajKutusu = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a")
ilkMesajKutusu.click()
time.sleep(2)
#Mesajlardaki ilk sırada olan kişinin mesaj penceresi açılıyor



for x in range(16):
        mesaj = browser.find_element_by_css_selector(".ItkAi > textarea:nth-child(1)")
        mesaj.send_keys("bot işlem ")
        gonder = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
        gonder.click()
#Döngüde range(x) x kere mesaj.send_keys(" ") içine yazılan mesaj gönderiliyor      

