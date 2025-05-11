import platform, socket, psutil, sys, time, requests, os, uuid
from datetime import datetime

# ANSI escape codes for colors
RED = "\033[91m"
RESET = "\033[0m"

def print_slow(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def roast_user():
    pc_name = platform.node()
    user_ip = socket.gethostbyname(socket.gethostname())
    os_version = platform.system() + " " + platform.release()
    cpu_count = psutil.cpu_count(logical=True)
    total_memory = round(psutil.virtual_memory().total / (1024 ** 3), 2)
    used_memory = round(psutil.virtual_memory().used / (1024 ** 3), 2)
    free_disk = round(psutil.disk_usage('/').free / (1024 ** 3), 2)
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0, 8 * 6, 8)][::-1])

    print_slow(f"PC Name: {pc_name}... sounds like a default name, huh? 🐕")
    print_slow(f"IP Address: {user_ip}... probably assigned by your microwave 🍳")
    print_slow(f"OS: {os_version}... using this relic, are we? 💻")
    print_slow(f"CPU Cores: {cpu_count}... more cores than you have friends 💀")
    print_slow(f"Memory: {used_memory}/{total_memory} GB used... stop hoarding memes! 🧠")
    print_slow(f"Free Disk: {free_disk} GB... emptier than your social calendar 📅")
    print_slow(f"Current Time: {time_now}... shouldn’t you be doing something else? 🕒")
    print_slow(f"MAC Address: {mac_address}... we even know your network adapter too 🕵️‍♂️")

def simulate_attacks():
    print_slow("Initiating some serious *cyber attacks* on your system... but don’t worry, it’s all in good fun 😈")
    time.sleep(1)
    
    print_slow("Running DDoS... 🤖 Sending packets... lots of packets...")
    time.sleep(2)
    
    print_slow("Executing a SQL Injection... 🔍 Oops, your login table is gone... just kidding! 🧙")
    time.sleep(2)
    
    print_slow("Deploying Ransomware... Encrypting your files... Oh wait, no, it's just your vacation photos 🏖️")
    time.sleep(2)
    
    print_slow("Performing Man-in-the-Middle attack... Intercepting your messages... Don’t worry, nobody cares 🕶️")
    time.sleep(2)
    
    print_slow("Bypassing firewall... Or maybe you forgot to set one up in the first place? 🚧")
    time.sleep(2)
    
    print_slow("Rootkit installed! Just kidding. Or am I? 🤖")
    time.sleep(2)

def download_image():
    image_url = "https://i.ibb.co/dLPVjTv/Findme.jpg"
    image_name = "Findme.jpg"
    
    try:
        print_slow("Downloading secret image from the remote server... 📡")
        response = requests.get(image_url)
        
        # Save the image
        with open(image_name, 'wb') as file:
            file.write(response.content)
        
        # Get the absolute path of the downloaded image
        img_path = os.path.abspath(image_name)
        print_slow(f"Secret image saved at: {RED}{img_path}{RESET} 🖼️")
        return img_path

    except Exception as e:
        print_slow(f"Error downloading image: {e}")
        return None

def challenge_intro(image_path):
    print_slow("Great! You were able to get my profile. 🐊 But, but, but... it's not so easy to get the flag. 😎")
    time.sleep(1)
    print_slow("You think you're clever, huh? Well, here's the real challenge.")
    time.sleep(1)
    print_slow(f"I secretly downloaded an image to your system: {RED}{image_path}{RESET} 🖼️")
    print_slow("Use your *skills* to analyze the image carefully. 🖼️")
    print_slow("Once you find the *place* where it was taken, find the *nearest metro station* to it. 🚇")
    print_slow("The flag format will be:")
    print_slow(f'{RED}CSAY{{"Place"_"Name"+"station"_"Name"}}{RESET} 🏆')
    print_slow("Good luck! 🕵️‍♂️")

def main():
    print_slow("Hacking your System... 🕵️‍♂️")
    roast_user()
    
    print_slow("\nSimulating attacks... 💻")
    simulate_attacks()

    image_path = download_image()
    
    if image_path:
        challenge_intro(image_path)
    else:
        print_slow("Couldn't download the image. Try again later.")

    print_slow("... It is also famous as electronics market in Delhi")
    print_slow("... now the real game begins! 🔍")

if __name__ == "__main__":
    main()
