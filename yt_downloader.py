import yt_dlp as youtube_dl
import random


def present_terms_of_service():
    tos = """
    Downloading videos from YouTube to keep permanently or share without permission is generally against their Terms of Service. 
    YouTube states that their content is owned by the creators and protected by copyright.

    However, YouTube does allow downloading videos for personal, non-commercial use in some cases. This includes being able to download videos when using YouTube Premium or using tools like YouTube Studio for content creators.
    
    Downloading audio only from YouTube videos to make into music playlists or offline listening may fall into a gray area. YouTube offers an official YouTube Music app that allows this, suggesting it is tolerated to some degree. But systematic downloading of audio at scale could still violate Terms.

    There are some third party sites and tools that allow downloading YouTube videos. However, YouTube actively works to disable and block these when discovered. So use of third party downloaders comes with some risk of YouTube actions against the account.

    Factors that matter are whether the downloading is systematic in large volumes vs a few videos, if you own the channel or have permission from creators, whether you share or profit from the downloads, and whether you circumvent ads or other limits.

    So in summary - downloading for personal offline use in moderation may be okay, but violating Terms by sharing, re-uploading, or systematically extracting a lot of audio/video without permission is risky and could prompt enforcement actions.

    Additional Resources:
    - YouTube's full Terms of Service: https://www.youtube.com/static?template=terms
      Specifically section 5 outlines restrictions around downloading content. Key points are that you can't download significant portions of content, circumvent technical restrictions, or provide tools for others to download.
    
    - YouTube's policies on copyright: https://www.youtube.com/howyoutubeworks/policies/copyright/
      This reiterates that all videos are protected by copyright, and downloading full videos requires the owner's permission. It also discusses fair use exceptions.
    
    - YouTube Premium download terms: https://support.google.com/youtube/answer/132596?hl=en
      This clarifies what downloading is allowed for paid Premium subscribers. It's for personal offline use only.
    
    - YouTube Studio download feature: https://support.google.com/youtube/answer/94316?hl=en
      Content creators can download their own videos using YouTube Studio tools. Downloads are watermarked and limited.

    Let me know if you need any clarification on YouTube's policies!
    """
    print(tos)

    acknowledgment_code = ''.join(
        [str(random.randint(0, 9)) for _ in range(5)])
    print(
        f"\nPlease enter the following code to acknowledge the Terms of Service: {acknowledgment_code}")

    user_input = input("Enter the 5-number sequence: ")
    if user_input != acknowledgment_code:
        print("Incorrect code or acknowledgment refused. Exiting.")
        exit()


def download_from_youtube():
    # URL Source Selection
    url = input("Enter the YouTube or YouTube Music URL: ")
    if "music.youtube.com" in url:
        print("Detected YouTube Music URL.")
    else:
        print("Detected standard YouTube URL.")

    # Format Selection using Numerical Choices
    print("Choose desired format:\n1. Video\n2. Audio")
    format_choice = input("Enter your choice (1/2): ")

    # youtube_dl Configuration
    if format_choice == "2":
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': './%(title)s.%(ext)s',
        }
    elif format_choice == "1":
        ydl_opts = {
            'format': 'bestvideo+bestaudio',
            'outtmpl': './%(title)s.%(ext)s',
        }
    else:
        print("Invalid format choice. Exiting.")
        return

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    present_terms_of_service()
    download_from_youtube()
