import webbrowser 
firefoxPath = r'C:\Program Files\Mozilla Firefox\firefox.exe'            
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefoxPath))
with open("urls.txt") as f:
    for url in f:
    	webbrowser.get('firefox').open(url,new=1,autoraise=True)
        
