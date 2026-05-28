from datetime import date

from data import datas
from data import extra
from auth import yt_auth

url = "https://www.billboard.com/charts/india-songs-hotw/"

def main():
    try:
        ytmusic = yt_auth.authenticate()
        print("Authenticated successfully!")

        song_list = datas.get_top_songs(url)
        print("Top songs retrieved successfully!")

        playlist_id = ytmusic.create_playlist(f'Indian top 25 songs weekly{date.today()}', description='Top 25 songs in India this week', privacy_status='PRIVATE')
        print("Playlist created successfully!")

        for song in song_list:
            searched = ytmusic.search(song, filter='songs', limit=1)
            
            ytmusic.add_playlist_items(playlist_id, [searched[0]['videoId']])
            print(f"Added '{song}' to the playlist.")

    except Exception as e:
        print(f"Error occurred: {e}")
        return


if __name__ == "__main__":
    main()
    