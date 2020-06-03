from bs4 import BeautifulSoup
import requests as req


class getInformation:
    def search(self, inn):
        link = f'https://www.rusprofile.ru/search?query={inn}&search_inactive=0'
        resp = req.get(link)
        information = Information()
        """
                Что ту происходит? Мы делаем get запрос по ссылке подставляя нужный нам ИНН, у запроса есть статус ответа, есл это 200, значит все ок, ссылка сработала
                Далее мы проверяем на ошибки все возвмодные И возвращаем СТРОКУ, можно конечно написать свои ошибки, но это муторно, вообще эта штука работает и довольно хорошо(наверное)
                
        
        """
        if resp.status_code != 200:
            return 'Page unavailable'
        elif resp.status_code == 404:
            return 'Not Found.'
        try:
            """
            Тут мы уже используем библиотеку и по html тегам производим поиск нужной нам информации 
            """
            soup = BeautifulSoup(resp.text, 'html.parser')
            information.companyName=soup.find("div", class_="company-name").text
            information.ogrn = (str(soup.find(id="clip_ogrn").text))# + " " + str(soup.find("dd", class_="company-info__text has-copy").find("dd",
                                                                                                                       #class_='company-info__text').text))  # add date
            information.inn = soup.find(id="clip_inn").text
            information.kpp = soup.find(id="clip_kpp").text
            information.date = soup.find_all("div", class_="company-row")[1].find("dd", class_="company-info__text").text
            information.money = soup.find_all("div", class_="company-row")[1].find("span", class_="copy_target").text
            information.address = soup.find("span", itemprop="postalCode").text +","+ soup.find("span",
                                                                                             itemprop="addressRegion").text +","+ soup.find(
                "span", itemprop="streetAddress").text
            information.typeOfActivity = soup.find_all("div", class_="rightcol")[1].find("span", class_="company-info__text").text
        except Exception as e:
            print(e)
            return 'Error in get date.'
        return information

class Information:
    def __init__(self):
        pass

    def setvalues(self, companyName, ogrn, inn, kpp, date, money, address, typeOfActivity):
        self.companyName = companyName
        self.ogrn = ogrn
        self.inn = inn
        self.kpp = kpp
        self.date = date
        self.money = money
        self.address = address
        self.typeOfActivity = typeOfActivity
