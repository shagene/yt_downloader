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
    - YouTube's policies on copyright: https://www.youtube.com/howyoutubeworks/policies/copyright/
    - YouTube Premium download terms: https://support.google.com/youtube/answer/132596?hl=en
    - YouTube Studio download feature: https://support.google.com/youtube/answer/94316?hl=en
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


def prompt_url():
    while True:
        url = input("Enter the YouTube or YouTube Music URL: ")
        if url.startswith("https://www.youtube.com") or url.startswith("https://music.youtube.com"):
            return url
        else:
            print(f"\nInvalid URL provided: {url}")
            print("The URL must be a valid YouTube or YouTube Music link starting with 'https://www.youtube.com' or 'https://music.youtube.com'.")
            choice = input(
                "Would you like to:\n1. Provide a new URL\n2. Exit the application\nEnter your choice (1/2): ")
            if choice == '2':
                exit()


def download_from_youtube():
    url = prompt_url()

    # (Insert your code here for detecting URL type, choosing format, and defining ydl_opts)

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except youtube_dl.utils.UnsupportedError:
            print("Unsupported URL or an error occurred. Please ensure the provided URL is a valid YouTube or YouTube Music link.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    present_terms_of_service()
    download_from_youtube()
