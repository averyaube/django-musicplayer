from django.http import HttpResponse

def playlists(request):
	return HttpResponse("playlists")

def playlist(request, playlist_id):
	return HttpResponse("playlist")

def playlist_json(request, playlist_id):
	return HttpResponse("playlist json")