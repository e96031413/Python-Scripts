import webbrowser

with open ('study.txt')as f:
	for url in f:
		webbrowser.open_new_tab(url)
