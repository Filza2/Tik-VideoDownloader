from requests import get
from time import sleep
#YOU MUST READ "README" FILE BEFORE RUN THE TOOL
print("""
████████╗██╗██╗  ██╗     ██╗   ██╗██████╗ ██╗     
╚══██╔══╝██║██║ ██╔╝     ██║   ██║██╔══██╗██║     
   ██║   ██║█████╔╝█████╗██║   ██║██║  ██║██║     
   ██║   ██║██╔═██╗╚════╝╚██╗ ██╔╝██║  ██║██║     
   ██║   ██║██║  ██╗      ╚████╔╝ ██████╔╝███████╗
   ╚═╝   ╚═╝╚═╝  ╚═╝       ╚═══╝  ╚═════╝ ╚══════╝
                
          By @TweakPY - @vv1ck
""")
user_vedid=input('[?] Enter The Video url : ')#https://vm.tiktok.com/ZMLYJPWBp/ or https://www.tiktok.com/@xawado/video/7123617989328456961?is_from_webapp=1&sender_device=pc supported !
vaild_v=user_vedid.split('https://')[1].split('.tiktok')[0]
if vaild_v=='vt':user_vedid=user_vedid.replace('vt','vm')
elif 'https://www.tiktok.com/@' in user_vedid:
    try:
        ved_id_skip=user_vedid.split('/video/')[1].split('?is_from_webapp')[0]
        r2=get(f"https://tiktok.livecounts.io/videoDownload/{ved_id_skip}",headers={'Host': 'tiktok.livecounts.io','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': '*/*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Referer': 'https://tokcounter.com/',
'X-Midas': '6d39063decda45d796d043e3c5570884b83a64072df6c66ae97bc6471be38554',
'X-Aurora': '4976244355026',
'X-Maven': '76f088c63041b7b049b3172220ef741c4a258f069295e62d30d29da585a92900',
'X-Joey': '1658748118342',
'X-Mayhem': '553246736447566b58312f697330687930634247756675374f51726c724c426d7a4e51785051484c7176596357674346474c6e6d39667957344547554e785753','Origin': 'https://tokcounter.com','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'cross-site','Te': 'trailers'})
        print('[+] Done ..')
        sleep(1.4)
        ved_title=r2.json()['video']['title'];ved_downloadurl=r2.json()['video']['downloadUrl']
        mp3_title=r2.json()['sound']['title'];mp3_downloadurl=r2.json()['sound']['downloadUrl']
        author_name=r2.json()['author']['name'];author_id_user=r2.json()['author']['id'];author_userid=r2.json()['author']['userId']
        if ved_title=='':ved_title='Null'
        if ved_downloadurl=='':ved_downloadurl='NULL'
        if mp3_title=='':mp3_title='Null'
        if mp3_downloadurl=='':mp3_downloadurl='NULL'
        if author_name=='':author_name='Null'
        if author_id_user=='':author_id_user='Null'
        if author_userid=='':author_userid='Null'
        exit(f"""
{'-'*40}
[#] video :\n
[+] Video Title : {ved_title}
[+] Video Downlaod Url : {ved_downloadurl}\n
[#] sound :\n
[+] Sound Title : {mp3_title}
[+] Sound Download Url : {mp3_downloadurl}\n
[#] author :\n
[+] Author Name : {author_name}
[+] Author username : {author_id_user}
[+] Author id : {author_userid}
{'-'*40}
""")
    except Exception as i:exit(f'[!] Failed to fetch download link : {i}')
elif vaild_v=='vm':pass
else:print('[!] Sorry This Type of urls not supported now but the tool will try to run anyway')
r1=get(f'https://api.tokcount.com/?type=videoId&username={user_vedid})',headers={'Host': 'api.tokcount.com','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': '*/*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Referer': 'https://tokcounter.com/',
'X-Midas': '6d39063decda45d796d043e3c5570884b83a64072df6c66ae97bc6471be38554',
'X-Aurora': '4976244355026',
'X-Maven': '76f088c63041b7b049b3172220ef741c4a258f069295e62d30d29da585a92900',
'X-Joey': '1658748118342',
'X-Mayhem': '553246736447566b58312f697330687930634247756675374f51726c724c426d7a4e51785051484c7176596357674346474c6e6d39667957344547554e785753','Origin': 'https://tokcounter.com','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'cross-site','Te': 'trailers'})
if r1.status_code==500:exit("[!] Video url is invalid or Video Not Found !")
elif r1.json()["success"]==False:exit("[!] Video url is invalid or Video Not Found !")
try:
    ved_id=r1.json()['id']
    print("[-] video id Found ..")
    sleep(1.5)
    r2=get(f"https://tiktok.livecounts.io/videoDownload/{ved_id}",headers={'Host': 'tiktok.livecounts.io','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': '*/*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Referer': 'https://tokcounter.com/',
'X-Midas': '6d39063decda45d796d043e3c5570884b83a64072df6c66ae97bc6471be38554',
'X-Aurora': '4976244355026',
'X-Maven': '76f088c63041b7b049b3172220ef741c4a258f069295e62d30d29da585a92900',
'X-Joey': '1658748118342',
'X-Mayhem': '553246736447566b58312f697330687930634247756675374f51726c724c426d7a4e51785051484c7176596357674346474c6e6d39667957344547554e785753','Origin': 'https://tokcounter.com','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'cross-site','Te': 'trailers'})
    print('[+] Done ..')
    sleep(1.4)
    ved_title=r2.json()['video']['title'];ved_downloadurl=r2.json()['video']['downloadUrl']
    mp3_title=r2.json()['sound']['title'];mp3_downloadurl=r2.json()['sound']['downloadUrl']
    author_name=r2.json()['author']['name'];author_id_user=r2.json()['author']['id'];author_userid=r2.json()['author']['userId']
    if ved_title=='':ved_title='Null'
    if ved_downloadurl=='':ved_downloadurl='NULL'
    if mp3_title=='':mp3_title='Null'
    if mp3_downloadurl=='':mp3_downloadurl='NULL'
    if author_name=='':author_name='Null'
    if author_id_user=='':author_id_user='Null'
    if author_userid=='':author_userid='Null'
    print(f"""
{'-'*40}
[#] video :\n
[+] Video Title : {ved_title}
[+] Video Downlaod Url : {ved_downloadurl}\n
[#] sound :\n
[+] Sound Title : {mp3_title}
[+] Sound Download Url : {mp3_downloadurl}\n
[#] author :\n
[+] Author Name : {author_name}
[+] Author username : {author_id_user}
[+] Author id : {author_userid}
{'-'*40}
""")
except KeyboardInterrupt:exit()
except:exit('[!] Fetal Error !')
