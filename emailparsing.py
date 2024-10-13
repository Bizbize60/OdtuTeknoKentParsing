import requests
from bs4 import BeautifulSoup
import re

def requestOfUrl(url):

    try:
        content=requests.get(url)
        getemail(content.text,url)
    except:
        print("", end="")
def getemail(content,anawebsayfasi):
    emailcounter=0
    pure_emails=[]
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    x=re.split("\s",content)
    y="  ".join(x)

    emails=re.findall(email_pattern,y)
    y=" ".join(emails)
    cleaned_email = re.sub(r'[a-zA-Z]+\d+([a-zA-Z]*)', r'\1', y)
    y="".join(cleaned_email)
    emails_array=y.split()
    for email in emails_array:
        cleaned_email = re.sub(r'^[A-Z]', '', email)
        pure_emails.append((cleaned_email))
    for i in pure_emails:
        if "info" or "bilgi" or "iletisim" in i:
            emailcounter+=1

    if emailcounter >= 10 :
        for i in pure_emails:
            print(i)
    else:
        soup = BeautifulSoup(content, 'html.parser')
        for link in soup.find_all('a'):

                urls=str(link.get('href'))

                index = urls.find(".com")
                if index >0:
                    newurls=urls[:index+4]
                    if newurls not in anawebsayfasi:

                        try:
                            context=requests.get(urls)
                            emails = re.findall(email_pattern, context.text)
                            for i in emails:
                                print(i)

                        except:
                            print("", end="")



                else:
                    pass




requestOfUrl("https://odtuteknokent.com.tr/tr/firmalar/tum-firmalar.php")
requestOfUrl("https://asoteknopark.com.tr/?page_id=1606")
requestOfUrl("https://ankarateknokent.com/firmalar-portfolio/")
requestOfUrl("https://www.gaziteknopark.com.tr/allcompany")
requestOfUrl("https://www.teknoparkankara.com.tr/Firmalar.html")
requestOfUrl("https://ostimteknopark.com.tr/tr/firmalar-119")
requestOfUrl("https://www.hacettepeteknokent.com.tr/tr/firma_rehberi/bilgisayar_ve_iletisim_teknolojileri-16")
requestOfUrl("https://www.hacettepeteknokent.com.tr/tr/firma_rehberi/elektronik-17")
requestOfUrl("https://www.cyberpark.com.tr/firma-arsiv")