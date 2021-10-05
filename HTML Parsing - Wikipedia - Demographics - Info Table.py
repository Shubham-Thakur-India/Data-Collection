#!/usr/bin/env python
# coding: utf-8

# In[3]:


##importing libraries

import pandas as pd
import requests
import re
from bs4 import BeautifulSoup

#url to parse
url = "https://en.wikipedia.org/wiki/Demographics_of_India"

#requesting url
req_url = requests.get(url)

#loading html content
soup = BeautifulSoup(req_url.text)

# Page title
title=soup.title.string.replace(' - Wikipedia','')

# Defining info table
summary_box_table=pd.DataFrame(columns=[title,'Info'])

var_01,var_02,col_2= ([], ) * 3

# Loading data into info table
table_segments=str(soup.findAll('table',class_="infobox")[0].findAll('th')).split('<th class="infobox-above navbox-abovebelow" colspan="2">')[1].split('<th class="infobox-header navbox-abovebelow" colspan="2">')
sub_segments_table_part_1=table_segments[0].split('</th>, <th class="infobox-label" scope="row">')[1:]
for i in sub_segments_table_part_1:
    var_01.append(str(i.replace('</th>, ','')).replace('\xa0•\xa0','  • '))
for i in table_segments[1:]:
    to_be_mapped=i.split('</th>, <th class="infobox-label" scope="row">')
    for j in to_be_mapped[1:]:
        var_02.append(to_be_mapped[0]+" > "+j.replace('</th>, ','').replace('</th>]',''))
col_1=var_01+var_02
summary_data=soup.findAll('table',class_="infobox")[0].findAll(class_='infobox-data')
for i in summary_data:
    col_2.append(re.sub("\[.*?\]","",i.text.replace("\n"," ")))
summary_box_table=summary_box_table.append(pd.DataFrame({title:col_1,'Info':col_2}))


# In[4]:


summary_box_table


# In[ ]:




