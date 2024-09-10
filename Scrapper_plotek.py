# pip install requests beautifulsoup4
import time, requests, bs4

def ScrapListyArtykulow(liczba_stron):

    for r in range(liczba_stron):
        url = 'https://www.pudelek.pl/article/?strona={}'.format(r+1)
        response = requests.get(url)
        time.sleep(2)
        soup=bs4.BeautifulSoup(response.content,'html.parser')
        print ('STRONA {}'.format(r+1))
        for row in soup.find_all(class_='sc-1mskw74-0 sc-1m1rbyx-1 dvfnVZ'):

            print('Tytuł artykułu: {}'.format(row.find(class_='sc-1mskw74-0 sc-7eqdwf-0 dvuFYB').get_text()))
            print('data: {}'.format(row.find(class_='sc-1mskw74-0 sc-7eqdwf-0 iElEid').get_text()))
            link = row.find('a').get('href')
            if link[0] == '/':
                print('link do artykulu: https://www.pudelek.pl{}'.format(link))
                odnosnik='https://www.pudelek.pl{}'.format(link)
            else:
                print('link do artykulu: {}'.format(link))
                odnosnik="ARTYKUL WIPOWSKI"
            ScrapArtykulu(odnosnik)


def ScrapArtykulu(adres):
    if adres=="ARTYKUL WIPOWSKI":
        print("ARTYKUL WIPOWSKI NIEDOSTEPNY")
        print('=' * 100)
    else:
        response2 = requests.get(adres)
        soup2=bs4.BeautifulSoup(response2.content,'html.parser')
        print("ZAWARTOSC ARTYKULU: ")
        for row in soup2.find(class_='sc-1mskw74-0 sc-1su7n3c-1 iwiEdl').find_all('p'):
            print(row.get_text())
            print("")
        print('=' * 50)
        time.sleep(2)


def scrapLinku():
    url = 'https://www.pudelek.pl/article/?strona=1'
    response = requests.get(url)
    soup=bs4.BeautifulSoup(response.content,'html.parser')
    for links in soup.find_all(class_='sc-1mskw74-0 sc-1m1rbyx-1 dvfnVZ'):
        link=links.find('a').get('href')
        if link[0] =='/':
            print('https://www.pudelek.pl{}'.format(link))
        else:
            print(link)

ScrapListyArtykulow(1)