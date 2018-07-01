import requests
import sys
import wget
program_name = sys.argv[0]
link = sys.argv[1:]

class mp3_collection:
    def __init__ (self):
        self.depth = 2
        self.search_list = ['mp3_name']
        self.total_entry = {"URL":0, "MP3":0, "JPG":0, "ZIP":0}
        self.total_url = 0
        self.link_list = {} 

    def set_search_depth(self, depth):
        self.depth = depth

    def is_url_already_exist(self, new_url):
        '''
        for i in self.link_list:
            if str(i) is str(new_url):
                print ("***********")
                return True
        return False
        '''         
        try:
            self.link_list[new_url]
            return True
        except:
            return False
    
    def get_dir_name_frm_url(self, url):
        token = "-songs.html"
        str = url[url.rfind('/')+1:url.find(token)]
        return str

    def add_url(self, parent_url, new_url):
        if self.is_url_already_exist(new_url) is True:
            return False
        if new_url.find(".mp3") is not -1:
            url_type = "MP3"
            self.total_entry["MP3"] += 1
        elif new_url.find(".zip") is not -1:
            url_type = "ZIP"
            self.total_entry["ZIP"] += 1
        elif new_url.find(".jpg") is not -1:
            url_type = "JPG"
            self.total_entry["JPG"] += 1
        else:
            url_type = "URL"
            self.total_entry["URL"] += 1
        
        directory_name = self.get_dir_name_frm_url(parent_url)
        self.link_list.update({new_url:{"TYPE":url_type, "PARENT_URL":parent_url, \
                    "SCANNED":False, "DOWNLOADED":False, "DIR_NAME":directory_name}})
    
    def print_links(self, file_type="ALL"):
        for i in self.link_list:
            if  ((file_type == "ALL" or file_type == "MP3") and \
                    (self.link_list[i]["TYPE"] == "MP3")):
                print("MP3: ",  self.link_list[i]["DIR_NAME"])
            
            if  ((file_type == "ALL" or file_type == "ZIP") and \
                    (self.link_list[i]["TYPE"] == "ZIP")):
                print("ZIP: ",  self.link_list[i]["DIR_NAME"])
            
            if  ((file_type == "ALL" or file_type == "JPG") and \
                    (self.link_list[i]["TYPE"] == "JPG")):
                print("JPG: ",  self.link_list[i]["DIR_NAME"])
            
            if  ((file_type == "ALL" or file_type == "URL") and \
                    (self.link_list[i]["TYPE"] == "URL")):
                print("URL: ",  self.link_list[i]["DIR_NAME"])

    def print_entries(self):
        print("Total url:", self.total_entry["URL"])
        print("Total mp3:", self.total_entry["MP3"])
        print("Total zip:", self.total_entry["ZIP"])
        print("Total jpg:", self.total_entry["JPG"])

    def get_sub_links(self, url):
        start_token="http"
        stop_token="\""
        http_r = requests.get(url)
        if (http_r.ok == False):
            print("URL Incorrect")
            return False
        str = http_r.text
        links = []
        while str.find(start_token) is not -1:
            str=str[str.find(start_token):]    
            link = str[:str.find(stop_token)]
            str = str[str.find(stop_token)+len(stop_token):]
            links.append(link)
        return links
        
    def get_new_url_list(self):
        links = []
        for link in self.link_list:
            if self.link_list[link]["SCANNED"] is True:
                continue
            if self.link_list[link]["TYPE"] != "URL":
                continue
            self.link_list[link]["SCANNED"] = True
            links.append(link)
        return links
        
    def start(self, url):
        self.add_url("null", url)
        while self.depth:
            for parent_link in self.get_new_url_list():
                print ("links", parent_link)
                sub_links = self.get_sub_links(parent_link)
                for link in sub_links:
                    if self.is_url_already_exist(link) is True:
                        continue
                    self.add_url(parent_link, link)
            
            self.depth -= 1
            
   

obj = mp3_collection()
#obj.add_url("NULL", "https://songspk3.in/firangi-songs.html")
obj.start("https://songspk3.in/firangi-songs.html")
obj.print_links(file_type="JPG")
obj.print_entries()
 
                    
''' 
print link
#r = requests.get("https://songspk3.in/firangi-songs.html")
r = requests.get(link[0])
#print r.status_code
#print r.headers
#print r.content
if (r.ok == False):
    print("URL Incorrect")
    exit

start_token="http"
stop_token="\""
str = r.text
links = []
mp3_links = []
while str.find(start_token) is not -1:
    str=str[str.find(start_token):]    
    link = str[:str.find(stop_token)]
    str = str[str.find(stop_token)+len(stop_token):]
    links.append(link)
    #print (link)
    
for link in links:
   # print (link)
    if link.find(".mp3") is not -1:
        print(link)
        mp3_links.append(link)
    
   
print("mp3 link", mp3_links[0])
mp3_link = '\"'+mp3_links[0]+'\"'
print("mp3 link", mp3_link)
mp3_data = wget.download(mp3_link)

print(mp3_data)
'''
