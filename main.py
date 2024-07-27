import imageio_ffmpeg as ffmpeg
import yt_dlp
import os

def download_youtube_video(url, output_path='.', audio_only=False):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'ffmpeg_location': ffmpeg.get_ffmpeg_exe()
    }

    if audio_only:
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"Download sucess and saved in: {output_path}")
    except Exception as e:
        print(f"Error during download: {e}")


def main():
    # enter YT video URL to get mp3
    video_url = 'https://www.youtube.com/watch?v=XXXXXXXXXXXXXXXXXX'  
    
    # set path to directory
    output_path = r'C:\X\X'

    file_directory = os.path.join(output_path)
    download_youtube_video(video_url, file_directory, True)


if __name__ == '__main__':
    main()
