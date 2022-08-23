from follow_bot import spotify
import threading, os, time, colorama

lock = threading.Lock()
counter = 0
proxies = []
proxy_counter = 0
spotify_profile = str(input("\033[36mSpotify Link or Username:\033[31m "))
threads = int(input("\n\033[39mThreads: "))

def load_proxies():
    if not os.path.exists("proxies.txt"):
        print("\nFile proxies.txt not found")
        time.sleep(10)
        os._exit(0)
    with open("proxies.txt", "r", encoding = "UTF-8") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            proxies.append(line)
        if not len(proxies):
            print("\nNo proxies loaded in proxies.txt")
            time.sleep(10)
            os._exit(0)

print("\n[1] \033[32mProxies\n\033[39m[2] \033[31mProxyless\033[39m")
option = int(input("\n> "))
if option == 1:
    load_proxies()

def safe_print(arg):
    lock.acquire()
    print(arg)
    lock.release()

def thread_starter():
    global counter
    if option == 1:
        obj = spotify(spotify_profile, proxies[proxy_counter])
    else:
        obj = spotify(spotify_profile)
    result, error = obj.follow()
    if result == True:
        counter += 1
        safe_print("\033[32mFollowed\033[37m {}".format(counter))
    else:
        safe_print(f"\033[31mError {error}\033[37m")

while True:
    if threading.active_count() <= threads:
        try:
            threading.Thread(target = thread_starter).start()
            proxy_counter += 1
        except:
            pass
        if len(proxies) <= proxy_counter:
            proxy_counter = 0

#Developed by https://github.com/Ment1sek
