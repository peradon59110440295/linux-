import click
import requests

from PIL import Image
from StringIO import StringIO
from bs4 import BeautifulSoup

@click.command()
@click.argument('src', nargs=-1)
@click.argument('dst', nargs=1)
def main(src, dst):
    	""" Poster"""    
	name=""	
	for fn in src:
        	name+='%s' % (fn)+" "
	name+='%s'%(dst)
	url='www.seriesyou.com/{}'.format(name.replace(" ", "-"))
	html=requests.get(url)
	beau=BeautifulSoup(html.content,'html.parser')
	poster=beau.find_all('p',{'class':'className'})
	beau=BeautifulSoup(str(poster),'html.parser')
	poster=beau.find_all('img')[0]['src']
	req=requests.get(str(poster))
	img=Image.open(StringIO(req.content))
	img.show()
