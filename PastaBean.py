#!/usr/bin/python

import re, requests, json, time, datetime, smtplib


while True:
	### Read in last N posts and get the key and put in array
	now = datetime.datetime.now()
	print 'Loop Check  = ' + str(now.strftime("%H:%M:%S%p"))
	post_limit = '100'
	last_n_posts = requests.get('http://pastebin.com/api_scraping.php?limit=' + post_limit).text
	json_posts = json.loads(last_n_posts)

	for post in json_posts:
			raw_post_text = requests.get('http://pastebin.com/api_scrape_item.php?i='+ post['key'])
		
			if re.match('(password|leak|dump)', raw_post_text.text) is not None :
				w = open('{0}-{1}.txt'.format(post['key'], 'Common'), 'w')
				w.write(raw_post_text.text.encode('utf-8').strip())
				w.close()
				gmail_alert('Common',post['full_url'])
			elif re.match('TV(oA|pB|pQ|qA|qQ|ro)', raw_post_text.text) is not None :
				f = open('{0}-{1}.txt'.format(post['key'], 'PE64'), 'w')
				f.write(raw_post_text.text.encode('utf-8').strip())
				f.close()
				gmail_alert('Base64 Encoded Exe',post['full_url'])
			elif re.match('sdcard', raw_post_text.text) is not None :
				y = open('{0}-{1}.txt'.format(post['key'], 'sdcard'), 'w')
				y.write(raw_post_text.text.encode('utf-8').strip())
				y.close()
				gmail_alert('sdcard',post['full_url'])			
			elif re.match('.*.\.onion', raw_post_text.text) is not None :
				z = open('{0}-{1}.txt'.format(post['key'], 'onion'), 'w')
				z.write(raw_post_text.text.encode('utf-8').strip())
				z.close()
				gmail_alert('Onion URL',post['full_url'])			
			elif re.match('(STRING|ENTER|DELAY)', raw_post_text.text) is not None :
				x = open('{0}-{1}.txt'.format(post['key'], 'Ducky'), 'w')
				x.write(raw_post_text.text.encode('utf-8').strip())
				x.close()
				gmail_alert('Ducky',post['full_url'])
			elif re.match('aHR0cDovLw', raw_post_text.text) is not None :
				q = open('{0}-{1}.txt'.format(post['key'], 'httpB64'), 'w')
				q.write(raw_post_text.text.encode('utf-8').strip())
				q.close()
				gmail_alert('http64',post['full_url'])
			elif re.match('QUACK.*.|(powershell|bash)|(LED.*.)|(ATTACKMODE.*.)', raw_post_text.text) is not None :
				e = open('{0}-{1}.txt'.format(post['key'], 'BASH-BUNNY'), 'w')
				e.write(raw_post_text.text.encode('utf-8').strip())
				e.close()
				gmail_alert('Bash Bunny',post['full_url'])		
			
			
			
			 
	time.sleep(60)
def gmail_alert(subject,body):
    gmail_user = "gmail sender account"
    gmail_password = "Sender Password"
    gmail_sender = gmail_user  
    to = ['Gmail receiver account']  
     
 
    email_text = """\  
    From: %s  
    To: %s  
    Subject: %s
    %s
    """ % (gmail_sender, ", ".join(to), subject, body)
 
    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_sender, to, email_text)
        server.close()
 
        print 'Email sent!'
    except:  
        print 'Something went wrong...'
 
 





