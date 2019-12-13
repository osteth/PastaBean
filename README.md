
# PastaBean
Python Script to Scrape Pastebin with Regex. This is by far  NOT a 'finished project' and plan to improve this over time.
My goal is to make PastaBean as flexible as I can and simple to run with minimal requirements to capture data.

## Background
Created script to learn Python and capture data on the popular site https://Pastebin.com.

## Features
- Scrape Pastebin, 100 queries per 60 seconds.
- Write matches to text file in same directory.
- Logging  - `pasta.log`

## Requirements
- Pastebin PRO account to use the API to scrape and whitelist your Internet IP (https://pastebin.com/doc_scraping_api).
- `sudo apt-get install python python-pip`
- `pip install requests`

## Recommendations/Usage
- Run on VPS
- Login via SSH
- Run script as background process(Python2.7): `python PastaBean.py &`
- Run script as background process(Python3.5.2): `python3 PastaBean.py &` : Tested and works.
- To release background process to`init` use `exit` to logout of ssh session
- Log back into VPS via SSH verify `Pastabean.py` is still running 
- Happy Hunting :)

## Future Improvements 
- Improve current RegeX
- Add more Regex!!!
- Enable to allow script to write to custom file path.
- ~~Decreased status output to one line.~~
- ~~Generate log file for each alarm to replace e-mail alerts~~
- Expand to other similar sites like pastebin.



## Contact
- Twitter @Tu5k4rr
- E-mail: Tu5k4rr@protonmail.com


