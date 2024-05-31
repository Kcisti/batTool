Re, Gr, Wh, Ye= '\033[1;31m', '\033[1;32m', '\033[1;37m', '\033[1;33m'
import requests

def userSSModeF():
    try:
        username = input(f"\n {Wh}Enter Username : {Gr}")
        results = {}
        social_media = [
            {"url": "https://www.facebook.com/{}", "name": "Facebook", "category" : "social"},
            {"url": "https://www.twitter.com/{}", "name": "Twitter", "category" : "social"},
            {"url": "https://www.instagram.com/{}", "name": "Instagram", "category" : "social"},
            {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn", "category" : "other"},
            {"url": "https://www.github.com/{}", "name": "GitHub", "category" : "hobby"},
            {"url": "https://www.pinterest.com/{}", "name": "Pinterest", "category" : "social"},
            {"url": "https://www.tumblr.com/{}", "name": "Tumblr", "category" : "social"},
            {"url": "https://www.youtube.com/{}", "name": "Youtube", "category" : "other"},
            {"url": "https://soundcloud.com/{}", "name": "SoundCloud", "category" : "hobby"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat", "category" : "social"},
            {"url": "https://www.tiktok.com/@{}", "name": "TikTok", "category" : "social"},
            {"url": "https://www.behance.net/{}", "name": "Behance", "category" : "other"},
            {"url": "https://www.medium.com/@{}", "name": "Medium", "category" : "forum"},
            {"url": "https://www.quora.com/profile/{}", "name": "Quora", "category" : "forum"},
            {"url": "https://www.flickr.com/people/{}", "name": "Flickr", "category" : "other"},
            {"url": "https://www.periscope.tv/{}", "name": "Periscope", "category" : "other"},
            {"url": "https://www.twitch.tv/{}", "name": "Twitch", "category" : "hobby"},
            {"url": "https://www.dribbble.com/{}", "name": "Dribbble", "category" : "other"},
            {"url": "https://www.stumbleupon.com/stumbler/{}", "name": "StumbleUpon", "category" : "other"},
            {"url": "https://www.ello.co/{}", "name": "Ello", "category" : "other"},
            {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt", "category" : "other"},
            {"url": "https://www.telegram.me/{}", "name": "Telegram", "category" : "social"},
            {"url": "https://www.weheartit.com/{}", "name": "We Heart It", "category" : "other"},
            {"url": "https://bere.al/{}", "name":"Bereal", "category" : "social"},
            {"url": "https://www.chess.com/topic/{}?search=1", "name":"Chess", "category" : "hobby"},
            {"url": "https://open.spotify.com/user/{}", "name":"Spotify", "category" : "hobby"},
            {"url": "https://www.wattpad.com/{}", "name":"Wattpad", "category" : "hobby"},
            {"url": "https://lichess.org/@/{}", "name":"Lichess", "category" : "hobby"},
        ]
        social,hobby,forum,other=0,0,0,0
        for site in social_media:
            url = site['url'].format(username)
            response = requests.get(url)
            if response.status_code == 200:
                results[site['name']] = url
                if site['category'] == 'social':
                    social=social+1
                elif site['category'] == 'hobby':
                    hobby=hobby+1
                elif site['category'] == 'forum':
                    forum=forum+1
                elif site['category'] == 'other':
                    other=other+1
            else:
                results[site['name']] = (f"{Re}! Username not found !")
    except Exception as e:
        print(f"{Re}Error : {e}")
        return

    print(f"\n{Gr} SHOW INFORMATION USERNAME\n")
    for site, url in results.items():
        print(f"{Wh} {Gr}+ {Wh} {site} : {Gr}{url}")
    print(f"\n FOUND: {hobby} hobbies, {social} social, {forum} forums and {other} others")