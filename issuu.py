
# coding: utf-8

# In[61]:


from requests import get
import requests
import wget
import os
from bs4 import BeautifulSoup

def create_pdf():
    from fpdf import FPDF
    #pdf = FPDF()
    pdf = FPDF('P','mm','A4') # create an A4-size pdf document 
    # imagelist is the list with all image filenames
    for image in document:
        x,y,w,h = 0,0,200,250
        pdf.add_page()
        pdf.image(image,x,y,w,h)
    pdf.output(pdfoutput, "F")


# In[62]:


#SETTINGS

deleteimages="y"
down='D:\Dropbox\WGET' # target directory
format='jpg'


# In[63]:


def mk_folder():
    if not os.path.exists(dd):
                   os.makedirs(dd)
def download_images():
    for link in linkslist:
          wget.download(link,dd)


# In[64]:


url = input('Issuu Pub Url: ')


# In[65]:


#cooking

response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
#id=html_soup.find('meta',{property:'og:image:secure_url'})
id=html_soup.find("meta",  property="og:image")['content']
id=id.replace('_1.jpg','')
title=html_soup.find("meta",  property="og:title")['content']
title=title.replace(' ','-')
print(title)


# In[66]:


dd=down+'\\'+title
pdfoutput=dd+'\\'+title+'.pdf'
print(dd)
mk_folder()
document=[]
for number in range(1,600):
    url=id+'_'+str(number)+'.'+format
    localfile=dd+'\\'+'page_'+str(number)+'.'+format
    file=requests.get(url)
    x,y,w,h = 0,0,200,250
    if file.status_code == 200:
        wget.download(url,dd)
        document.append(localfile)
    else:
        break

create_pdf()
if deleteimages=='y':
    for file in document:
        os.remove(file)
print("FINISHED")

