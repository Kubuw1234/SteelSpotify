from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
from spotify_integration import get_spotify_access_token, get_current_track_info, create_json_track_info
from steelseries_integration import initialize_sdk, update_keyboard_display

def main():
    # Uzyskaj token dostępu do Spotify API
    spotify_access_token = get_spotify_access_token(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)

    # Inicjalizuj SDK SteelSeries GG
    initialize_sdk()

    while True:
        # Pobierz informacje o utworze z Spotify
        current_track_info = get_current_track_info(spotify_access_token)

        # Stwórz JSON z informacjami o utworze
        json_data = create_json_track_info(current_track_info)

        # Aktualizuj wyświetlanie na klawiaturze SteelSeries GG
        update_keyboard_display(json_data)

if __name__ == "__main__":
    main()
