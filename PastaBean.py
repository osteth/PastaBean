#!/usr/bin/python

import re, requests, json, time
while True:
	### Read in last N posts and get the key and put in array
	print 'starting loop'
	post_limit = '100'
	last_n_posts = requests.get('http://pastebin.com/api_scraping.php?limit=' + post_limit).text
	json_posts = json.loads(last_n_posts)

	for post in json_posts:
			raw_post_text = requests.get('http://pastebin.com/api_scrape_item.php?i='+ post['key'])
		
			if re.match('[_=/\\\\]{3,20}', raw_post_text.text) is not None :
				h = open('{0}-{1}.txt'.format(post['key'], 'pwrshll'), 'w')
				h.write(raw_post_text.text.encode('utf-8').strip())
				h.close()
			elif re.match('TV(oA|pB|pQ|qA|qQ|ro)', raw_post_text.text) is not None :
				f = open('{0}-{1}.txt'.format(post['key'], 'PE64'), 'w')
				f.write(raw_post_text.text.encode('utf-8').strip())
				f.close()
			elif re.match('sdcard', raw_post_text.text) is not None :
				y = open('{0}-{1}.txt'.format(post['key'], 'sdcard'), 'w')
				y.write(raw_post_text.text.encode('utf-8').strip())
				y.close()			
			elif re.match('.*.\.onion', raw_post_text.text) is not None :
				z = open('{0}-{1}.txt'.format(post['key'], 'onion'), 'w')
				z.write(raw_post_text.text.encode('utf-8').strip())
				z.close()			
			elif re.match('(STRING|ENTER|DELAY)', raw_post_text.text) is not None :
				x = open('{0}-{1}.txt'.format(post['key'], 'Ducky'), 'w')
				x.write(raw_post_text.text.encode('utf-8').strip())
				x.close()			
	time.sleep(60)
		
		





