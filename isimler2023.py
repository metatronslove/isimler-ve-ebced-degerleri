import urllib.request
import time
import codecs
import sys
import traceback
sys.stdin.reconfigure(encoding="ISO-8859-9")
sys.stdout.reconfigure(encoding="ISO-8859-9")

# thank you kahramankostas ! This my 2023 revision of his 2019s code
#------------------------Only function here-------------------------
def link_bul(sayfa):
    baglanti = sayfa.find("a href")
    if baglanti == -1:
        return None, 0
    baglanti_basi = sayfa.find("'h", baglanti)
    baglanti_sonu = sayfa.find("l'", baglanti_basi)
    url = sayfa[baglanti_basi + 1:baglanti_sonu] + "l"
    print(url)
    return url, baglanti_sonu
#--------------------------------------------------------------------
dosya=codecs.open("isimler2023.csv", "w", "ISO-8859-9")
dosya.write("Arabic,Turkce\n")
for i in range (1,83):
	site = "https://isimler.ihya.org/index.html?s=" + str(i)
	temp = urllib.request.urlopen(site)
	print(site)
	sayfa = temp.read().decode('ISO-8859-9')
	limit = sayfa.find("<p align=center><small>")
	sayfa = sayfa[:limit]
	while True:
		url, n = link_bul(sayfa)
		sayfa = sayfa[n:]
		if url:
			if "-isminin-anlami.html" in url:
				temptr=urllib.request.urlopen(url)
				subpage = subpagetr = temptr.read().decode('ISO-8859-9')
				tekst=subpage.find("<font size='6'")
				if tekst != -1:
					bas=subpage.find(">", tekst)
					son=subpage.find("<", bas)
					subpage=subpage[bas+1:son]
					kekst=subpagetr.find("<font color=#006699><b")
					if kekst != -1:
						bastr=subpagetr.find("<b>", kekst)
						sontr=subpagetr.find("</b>", bastr)
						subpagetr=subpagetr[bastr+3:sontr]
						subpage = subpage+','+subpagetr+'\n'
						dosya.write(subpage)
						print(subpage)
		else:
			break
dosya.close()