import json
import spotipy
import webbrowser


username = 'SpotifyAudioPython'
clientID = '17c8b957f3454a57bc7a20f988a1630e'
clientSecret = '6b627f706f4545259929db1121d1617c'
redirect_uri = 'http://google.com/callback/'
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()

# To get the  JSON response
print(json.dumps(user_name, sort_keys=True, indent=4))

while True:
	print("Welcome, " + user_name['display_name']+"\n")
	search_song = input("Song name: ")
	print("Playing... ".format(search_song))
	results = spotifyObject.search(search_song, 1, 0, "track")
	songs_dict = results['tracks']
	song_items = songs_dict['items']
	song = song_items[0]['external_urls']['spotify']
	webbrowser.open(song)

