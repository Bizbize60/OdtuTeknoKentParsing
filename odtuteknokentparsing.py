import requests
from bs4 import BeautifulSoup
import re

def get_html(url):
    try:
        response = requests.get(url)
        return response.text
    except:
        print("",end="")
def find_emails(html):
    try:
        emails = set()
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        soup = BeautifulSoup(html, 'html.parser')
        if 'contact' in soup.get_text().lower() or 'iletisim' in soup.get_text().lower():
            for a in soup.find_all('a', href=True):
                if "contact" in a["href"] or "iletisim" in a["href"]:
                    if "html" in a["href"]:
                        if ".tr" in html:
                            ind=html.find(".tr")
                            contact_page_link=html[0:ind]+"/"+a["href"]
                            contact_page_html = get_html(contact_page_link)
                            contact_page_soup = BeautifulSoup(contact_page_html, 'html.parser')
                            emails.update(re.findall(email_pattern, contact_page_soup.get_text()))
                    
                        elif ".com" in html:
                            ind=html.find(".com")
                            contact_page_link=html[0:ind]+"/"+a["href"]
                            contact_page_html = get_html(contact_page_link)
                            contact_page_soup = BeautifulSoup(contact_page_html, 'html.parser')
                            emails.update(re.findall(email_pattern, contact_page_soup.get_text()))
                    
                    else:
                        contact_page_link=a["href"]
                        contact_page_html = get_html(contact_page_link)
                        contact_page_soup = BeautifulSoup(contact_page_html, 'html.parser')
                        emails.update(re.findall(email_pattern, contact_page_soup.get_text()))

        else:
            emails.update(re.findall(email_pattern, soup.get_text()))
        return emails
    except:
        print("",end="")

site = requests.get("https://odtuteknokent.com.tr/tr/firmalar/tum-firmalar.php")
soup = BeautifulSoup(site.content, 'html.parser')
for a in soup.find_all('a', href=True):
    if "teknokent" in a["href"]:
        continue
    elif "http" not in a["href"]:
        continue
    else:
        if ".com" not in a["href"]:
            continue
        else:
            html = get_html(a["href"])
            emails = find_emails(html)
            if emails:
                
                for email in emails:
                    print(email)
            else:
                continue