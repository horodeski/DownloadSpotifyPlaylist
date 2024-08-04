import subprocess
import os

""" pip install spotdl """

def download_spotify_playlist(playlist_url, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    command = f"spotdl --output {output_folder} {playlist_url}"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    playlist_url = input("Insira a URL da playlist do Spotify: ")
    output_folder = input("Insira o diretório de saída: ")
    download_spotify_playlist(playlist_url, output_folder)
    print(f'Playlist baixada e convertida para MP3 em: {output_folder}')
