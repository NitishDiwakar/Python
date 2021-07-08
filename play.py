import webbrowser

# create a list with song name and link

# Dictionary
song_list = {
	"tere naam" : "OMoU0Pfibc4",
	"odhni odh ke" : "_rHAedNAOfk",
	"ram pam pam" : "_wE3hDN06Qg",
	"dil huwa deewana" : "SjGiu3HRCkI",
	"aakhir tumhe aana hai" : "YvT6T5hMt-w",
	"tu dharti pe chahe" : "wuKIZxaRnG8",
	"dekha tujhe to" : "cUVUs7M9TS0"
	# "" : ""
	}
# End dictionary

song_name_input = input("Enter song name: ")
song_name = song_name_input
# print("You entered: " + song_name);


# print(song_list)
# print(type(song_list))

if song_name in song_list:
	# print("Found")
	# print(song_list[song_name])
	video_link = (song_list[song_name])

	# new = 2 opens in new tab, new = 1 open in new window, default = newtab
	webbrowser.open(f"www.youtube.com/watch?v={video_link}", new=2) 

else:
	print("Not found")
# print(song_list)

	



