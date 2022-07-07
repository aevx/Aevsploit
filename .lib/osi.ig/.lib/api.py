import requests
import random
import json
import sys
from local import *

resp_js = None
is_private = False
total_uploads = 12

def proxy_session():
	session = requests.session()
	session.proxies = {
		'http':  'socks5://127.0.0.1:9050',
		'https': 'socks5://127.0.0.1:9050'
	}
	return session

def get_page(usrname):
	global resp_js
	session = requests.session()
	session.headers = {'User-Agent': random.choice(useragent)}
	resp_js = session.get('https://www.instagram.com/'+usrname+'/?__a=1').text
	return resp_js

def exinfo():

	def xprint(xdict, text):
		if xdict != {}:
			print(f"{su}{re} hastag kullanımı")
			i = 0
			for key, val in xdict.items():
				if len(mail) == 1:
					if key in mail[0]:
						continue
				print(f"  {gr}%s : {wh}%s" % (key, val))
				i += 1
				if i > 4:
					break
			print()
		else:
			pass
	
	raw = find(resp_js)

	mail = raw['email']
	tags = sort_list(raw['tags'])
	ment = sort_list(raw['mention'])

	if mail != []:
		if len(mail) == 1:
			print(f"{su} {re}email bulundu : \n{gr}  %s" % mail[0])
			print()
		else:
			print(f"{su} {re}email bulundu : \n{gr}  ")
			for x in range(len(mail)):
				print(mail[x])
			print()

	xprint(tags, "tags")
	xprint(ment, "mentions")
	
def user_info(usrname):

	global total_uploads, is_private
	
	resp_js = get_page(usrname)
	js = json.loads(resp_js)
	js = js['graphql']['user']
	
	if js['is_private'] != False:
		is_private = True
	
	if js['edge_owner_to_timeline_media']['count'] > 12:
		pass
	else:
		total_uploads = js['edge_owner_to_timeline_media']['count']

	usrinfo = {
		'Kullanıcı Adı': js['username'],
		'Kullanıcı İd': js['id'],
		'Ad': js['full_name'],
		'Takipçi': js['edge_followed_by']['count'],
		'Takip': js['edge_follow']['count'],
		'Toplam Gönderi': js['edge_owner_to_timeline_media']['count'],
		'Posts video': js['edge_felix_video_timeline']['count'],
		'Reels': js['highlight_reel_count'],
		'Biografi': js['biography'].replace('\n', ', '),
		'Biosundaki url': js['external_url'],
		'Gizlilik': js['is_private'],
		'Mavi Tik': js['is_verified'],
		'Profil fotoğrafı': urlshortner(js['profile_pic_url_hd']),
		'İşletme hesabı': js['is_business_account'],
		'Yeni Hesap mı?': js['is_joined_recently'],
		'İşletme kategorisi': js['business_category_name'],
		'Kategori': js['category_enum'],
		'Kılavuzlar': js['has_guides'],
        }


	banner()

	print(f"{su}{re} kullanıcı bilgileri")
	for key, val in usrinfo.items():
		print(f"  {gr}%s : {wh}%s" % (key, val))

	print("")

	exinfo()
