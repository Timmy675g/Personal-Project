import requests

def check_username(username):
    sites = {
        "GitHub": f"https://github.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Pinterest": f"https://www.pinterest.com/{username}/",
        "Twitter (X)": f"https://x.com/{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Roblox": f"https://www.roblox.com/users/profile?username={username}",
        "Minecraft (NameMC)": f"https://namemc.com/profile/{username}"
    }


    print(f"\n🔍 Checking username: {username}\n")

    for site, url in sites.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 404:
                print(f"✅ {site}: Available")
            else:
                print(f"❌ {site}: Taken")
        except requests.exceptions.RequestException:
            print(f"⚠️ {site}: Could not connect (maybe blocked)")

if __name__ == "__main__":
    user_input = input("Enter a username to check: ")
    check_username(user_input)

# In order to run this code, you need to wrrite "python check_username.py" in your terminal.