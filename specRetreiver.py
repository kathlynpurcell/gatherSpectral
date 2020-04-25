# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:16:26 2019

@author: kpurc
"""

#program to fetch the spectral type of any star


from bs4 import BeautifulSoup

from urllib.request import urlopen

stardat = open("Stars.txt", 'r+')
star_line = stardat.readline()
new = open("Stars+SpecType.txt", 'w+')
print("Running")
while star_line:
    use_line = star_line.strip()
    link_line = use_line.replace(" ","+")
    url_link = "http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=" + link_line + "&submit=SIMBAD+search"
    html = urlopen(url_link)
    soup = BeautifulSoup(html, 'html.parser')
    html_text = soup.get_text()
    spec_line = html_text.find('Spectral type:') +27
    spectral_type = html_text[spec_line:spec_line+6]
    new.write(use_line + "," + spectral_type.strip() + "\n")
    ###If you are reading to LaTex/Excel/ another program then use only ',' or '\t' and set that
        ### to the delimeter in the other program to convert the output .txt file
    star_line = stardat.readline()
    print(".")

stardat.close()
new.close()
print("Done!")
