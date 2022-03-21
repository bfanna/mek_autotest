import configparser
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

config = configparser.ConfigParser()
config.read('mek.ini', encoding='utf-8')
targetURL = config['mek']['url']


class Mek100Contact(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.caseURL = targetURL + config['mek']['contactUrl']
        self.expectedText1 = config['case_100']['expectedText1']
        self.expectedText2 = config['case_100']['expectedText2']
        self.expectedText3 = config['case_100']['expectedText3']

    def test(self):
        """Case 100 - Contact page"""
        driver = self.driver
        driver.get(self.caseURL)
        check1 = self.expectedText1 in driver.page_source
        check2 = self.expectedText2 in driver.page_source
        check3 = self.expectedText3 in driver.page_source
        self.assertTrue(check1 & check2 & check3, "kapcsolat page text is missing")

    def tearDown(self):
        self.driver.close()


class Mek200BasicSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.caseURL = targetURL
        self.author = config['case_200']['inputAuthor']
        self.expectedText = config['case_200']['expectedText1']

    def test(self):
        """Case 200 - Basic search / Search by Author"""
        driver = self.driver
        driver.get(self.caseURL)
        driver.find_element(By.NAME, "dc_creator").send_keys(self.author)
        driver.find_element(By.NAME, "Image3").click()
        check = self.expectedText in self.driver.page_source
        self.assertTrue(check, "search result not found")

    def tearDown(self):
        self.driver.close()


class Mek300SICAuthor(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.expectedText = config['case_3xx']['expectedTextView']

    def test(self):
        """Case 300 - Search in Collection / By Author"""
        driver = self.driver
        driver.get(targetURL)
        driver.find_element(By.NAME, 'dc_creator').send_keys('Szerb Antal')
        driver.find_element(By.NAME, 'Image3').click()
        driver.find_element(By.XPATH, "//*[contains(text(), 'A Pendragon-legenda')]").click()
        check = self.expectedText in self.driver.page_source
        self.assertTrue(check, 'book not found')

    def tearDown(self):
        self.driver.close()


class Mek301SICTitle(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.expectedText = config['case_3xx']['expectedTextView']

    def test(self):
        """Case 301 - Search in Collection / By Title"""
        driver = self.driver
        driver.get(targetURL)
        driver.find_element(By.NAME, 'dc_title').send_keys('Nóra')
        driver.find_element(By.NAME, 'Image3').click()
        driver.find_element(By.XPATH, "//*[contains(text(), 'Ibsen, Henrik:')]").click()
        check = self.expectedText in self.driver.page_source
        self.assertTrue(check, 'book not found')

    def tearDown(self):
        self.driver.close()


class Mek302SICTopic(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.expectedText = config['case_3xx']['expectedTextView']

    def test(self):
        """Case 302 - Search in Collection / By Topic"""
        driver = self.driver
        driver.get(targetURL)
        driver.find_element(By.NAME, 'dc_subject').send_keys('sci-fi')
        driver.find_element(By.NAME, 'Image3').click()
        driver.find_element(By.XPATH, "//*[contains(text(), 'Alapítvány és Asimov')]").click()
        check = self.expectedText in self.driver.page_source
        self.assertTrue(check, 'book not found')

    def tearDown(self):
        self.driver.close()


class Mek303SICId(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.inputID = config['case_303']['inputID']
        self.expectedText = config['case_303']['expectedText']

    def test(self):
        """Case 303 - Search in Collection / By ID"""
        driver = self.driver
        driver.get(targetURL)
        driver.find_element(By.NAME, 'id').send_keys(self.inputID)
        driver.find_element(By.NAME, 'Image3').click()
        check = self.expectedText in self.driver.page_source
        self.assertTrue(check, 'book not found')

    def tearDown(self):
        self.driver.close()


class Mek304SICmp3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.expectedText = config['case_3xx']['expectedTextListen']

    def test(self):
        """Case 304 - Search in Collection / By mp3 format"""
        driver = self.driver
        driver.get(targetURL)
        driver.find_element(By.NAME, 'mp3').click()
        driver.find_element(By.XPATH, "//*[contains(text(), 'Kalevala')]").click()
        check = self.expectedText in self.driver.page_source
        self.assertTrue(check, 'audiobook not found')

    def tearDown(self):
        self.driver.close()


class Mek305SICepub(unittest.TestCase):  # search in collection - by EPUB format

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.expectedText = config['case_3xx']['expectedTextView']

    def test(self):
        """Case 305 - Search in Collection / By epub format"""
        driver = self.driver
        driver.get(targetURL)
        driver.find_element(By.NAME, 'epub').click()
        driver.find_element(By.XPATH, "//*[contains(text(), 'Alternatív munkaerőpiac')]").click()
        check = self.expectedText in self.driver.page_source
        self.assertTrue(check, 'book not found')

    def tearDown(self):
        self.driver.close()


class Mek306SICPRC(unittest.TestCase):  # search in collection - by PRC format

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.expectedText = config['case_3xx']['expectedTextView']

    def test(self):
        """Case 306 - Search in Collection / By PRC format"""
        driver = self.driver
        driver.get(targetURL)
        driver.find_element(By.NAME, 'prc').click()
        driver.find_element(By.XPATH, "//*[contains(text(), 'Buddha beszédei')]").click()
        check = self.expectedText in self.driver.page_source
        self.assertTrue(check, 'book not found')

    def tearDown(self):
        self.driver.close()


class Mek307SICCC(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.expectedText = config['case_3xx']['expectedTextView']

    def test(self):
        """Case 307 - Search in Collection / By CC Licence"""
        driver = self.driver
        driver.get(targetURL)
        driver.find_element(By.NAME, 'cc').click()
        driver.find_element(By.XPATH, "//*[contains(text(), 'Algebrai példatár')]").click()
        check = self.expectedText in self.driver.page_source
        self.assertTrue(check, 'book not found')

    def tearDown(self):
        self.driver.close()


class Mek308SICAdv1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.expectedText = config['case_3xx']['expectedTextView']

    def test(self):
        """Case 308 - Search in Collection / Advanced - Title, alt title, author, author type"""
        driver = self.driver
        driver.get(targetURL)
        driver.find_element(By.NAME, 'Image2').click()
        driver.find_element(By.XPATH, "//select[@name='s1']/option[text()=' Főcím  ']").click()
        driver.find_element(By.NAME, 'm1').send_keys('the bases of law')
        driver.find_element(By.XPATH, "//select[@name='s2']/option[text()=' Párhuzamos cím  ']").click()
        driver.find_element(By.NAME, 'm2').send_keys('a jog alapjai')
        driver.find_element(By.XPATH, "//select[@name='s3']/option[text()=' Szerző  ']").click()
        driver.find_element(By.NAME, 'm3').send_keys('horváth barna')
        driver.find_element(By.XPATH, "//select[@name='s4']/option[text()=' Szerzői minőség  ']").click()
        driver.find_element(By.NAME, 'm4').send_keys('szerző', Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[contains(text(), 'The bases of law')]").click()
        check = self.expectedText in self.driver.page_source
        self.assertTrue(check, 'book not found')

    def tearDown(self):
        self.driver.close()


class Mek309SICAdv2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.expectedText = config['case_3xx']['expectedTextView']

    def test(self):
        """Case 309 - Search in Collection / Advanced - Original title, subject, era subject, language, original language"""
        driver = self.driver
        driver.get(targetURL)
        driver.find_element(By.NAME, 'Image2').click()
        driver.find_element(By.XPATH, "//select[@name='s1']/option[text()=' Eredeti cím  ']").click()
        driver.find_element(By.NAME, 'm1').send_keys('tétova esztendő')
        driver.find_element(By.XPATH, "//select[@name='s2']/option[text()=' Tárgyszó  ']").click()
        driver.find_element(By.NAME, 'm2').send_keys('világháború')
        driver.find_element(By.XPATH, "//select[@name='s3']/option[text()=' Időszak tárgyszó ']").click()
        driver.find_element(By.NAME, 'm3').send_keys('20 sz')
        driver.find_element(By.XPATH, "//select[@name='s4']/option[text()=' Nyelv  ']").click()
        driver.find_element(By.NAME, 'm4').send_keys('német')
        driver.find_element(By.XPATH, "//select[@name='s5']/option[text()=' Eredeti nyelv  ']").click()
        driver.find_element(By.NAME, 'm5').send_keys('magyar', Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[contains(text(), 'Das verlorene Jahr')]").click()
        check = self.expectedText in self.driver.page_source
        self.assertTrue(check, 'book not found')

    def tearDown(self):
        self.driver.close()


class Mek310SICAdv3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.expectedText = config['case_3xx']['expectedTextView']

    def xtest(self):
        """Case 310 - Search in Collection / Advanced - Additional title, series, original release, creative commons"""
        driver = self.driver        
        driver.get(targetURL)
        driver.find_element(By.NAME, 'Image2').click()
        driver.find_element(By.XPATH, "//select[@name='s1']/option[text()=' Alcím  ']").click()
        driver.find_element(By.NAME, 'm1').send_keys('tragédia')
        driver.find_element(By.XPATH, "//select[@name='s2']/option[text()=' Sorozat  ']").click()
        driver.find_element(By.NAME, 'm2').send_keys('olcsó könyvtár')
        driver.find_element(By.XPATH, "//select[@name='s3']/option[text()=' Eredeti kiadvány  ']").click()
        driver.find_element(By.NAME, 'm3').send_keys('cid')
        driver.find_element(By.XPATH, "//select[@name='s4']/option[text()=' Creative commons ']").click()
        driver.find_element(By.NAME, 'm4').send_keys('by-sa/3.0', Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[contains(text(), 'Cid')]").click()
        check = self.expectedText in self.driver.page_source
        self.assertTrue(check, 'book not found')

    def tearDown(self):
        self.driver.close()


class Mek311SICAdv4(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.expectedText = config['case_3xx']['expectedTextListen']

    def test(self):
        """Case 311 - Search in Collection / Advanced - Digital publisher, geographical subject, format, legal comment"""
        driver = self.driver
        driver.get(targetURL)
        driver.find_element(By.NAME, 'Image2').click()
        driver.find_element(By.XPATH, "//select[@name='s1']/option[text()=' Digitális kiadó  ']").click()
        driver.find_element(By.NAME, 'm1').send_keys('magánkiad')
        driver.find_element(By.XPATH, "//select[@name='s2']/option[text()=' Földrajzi tárgyszó  ']").click()
        driver.find_element(By.NAME, 'm2').send_keys('görögország')
        driver.find_element(By.XPATH, "//select[@name='s3']/option[text()=' Formátum  ']").click()
        driver.find_element(By.NAME, 'm3').send_keys('mp3')
        driver.find_element(By.XPATH, "//select[@name='s4']/option[text()=' Jogi megjegyzés ']").click()
        driver.find_element(By.NAME, 'm4').send_keys('jogvédett', Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[contains(text(), 'Epiktétos')]").click()
        check = self.expectedText in self.driver.page_source
        self.assertTrue(check, 'audiobook not found')

    def tearDown(self):
        self.driver.close()


class Mek312SICAdv5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.expectedText = config['case_3xx']['expectedTextView']

    def test(self):
        """Case 312 - Search in Collection / Advanced - Group title, contributor, contrib. quality, document type"""
        driver = self.driver
        driver.get(targetURL)
        driver.find_element(By.NAME, 'Image2').click()
        driver.find_element(By.XPATH, "//select[@name='s1']/option[text()=' Összefoglaló cím  ']").click()
        driver.find_element(By.NAME, 'm1').send_keys('isteni színjáték')
        driver.find_element(By.XPATH, "//select[@name='s2']/option[text()=' Közreműködő  ']").click()
        driver.find_element(By.NAME, 'm2').send_keys('szász károly')
        driver.find_element(By.XPATH, "//select[@name='s3']/option[text()=' Közreműködői minőség  ']").click()
        driver.find_element(By.NAME, 'm3').send_keys('fordító')
        driver.find_element(By.XPATH, "//select[@name='s4']/option[text()=' Dokumentumtípus ']").click()
        driver.find_element(By.NAME, 'm4').send_keys('elbeszélő költemény', Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[contains(text(), 'A paradicsom')]").click()
        check = self.expectedText in self.driver.page_source
        self.assertTrue(check, 'book not found')

    def tearDown(self):
        self.driver.close()


class Mek313SICAdv6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.expectedText = config['case_3xx']['expectedTextView']

    def test(self):
        """Case 313 - Search in Collection / Advanced - Subtitle"""
        driver = self.driver
        driver.get(targetURL)
        driver.find_element(By.NAME, 'Image2').click()
        driver.find_element(By.XPATH, "//select[@name='s1']/option[text()=' Részcím  ']").click()
        driver.find_element(By.NAME, 'm1').send_keys('1 2', Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[contains(text(), 'Digitális írástudás Linuxon')]").click()
        check = self.expectedText in self.driver.page_source
        self.assertTrue(check, 'book not found')

    def tearDown(self):
        self.driver.close()


class Mek314SICAdv7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.expectedText = config['case_3xx']['expectedTextView']

    def test(self):
        """Case 314 - Search in Collection / Advanced - author board"""
        driver = self.driver
        driver.get(targetURL)
        driver.find_element(By.NAME, 'Image2').click()
        driver.find_element(By.XPATH, "//select[@name='s1']/option[text()=' Testületi szerző ']").click()
        driver.find_element(By.NAME, 'm1').send_keys('hétfa kutatóintézet', Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[contains(text(), 'Érvek és ellenérvek a bankadóról')]").click()
        check = self.expectedText in self.driver.page_source
        self.assertTrue(check, 'book not found')

    def tearDown(self):
        self.driver.close()


class Mek315SICAdv8(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.expectedText = config['case_3xx']['expectedTextView']

    def test(self):
        """Case 315 - Search in Collection / Advanced - copyright owner"""
        driver = self.driver
        driver.get(targetURL)
        driver.find_element(By.NAME, 'Image2').click()
        driver.find_element(By.XPATH, "//select[@name='s1']/option[text()=' Copyright tulajdonos ']").click()
        driver.find_element(By.NAME, 'm1').send_keys('akadémiai kiadó 1990', Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[contains(text(), 'A magyar irodalom története 1945-1975')]").click()
        check = self.expectedText in self.driver.page_source
        self.assertTrue(check, 'book not found')

    def tearDown(self):
        self.driver.close()


class Mek400EnglishMode(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.caseURL = targetURL + config['mek']['englishContactUrl']
        self.expectedText = config['case_400']['expectedText']

    def test(self):
        """Case 400 - English version website"""
        driver = self.driver
        driver.get(self.caseURL)
        check1 = self.expectedText in driver.page_source
        self.assertTrue(check1, "text not found")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2, warnings='ignore')
