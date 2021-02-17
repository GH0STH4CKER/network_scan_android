import os , subprocess , threading , time , sys


import concurrent , requests


from concurrent import futures


from colorama import Fore , init


init()


G = Fore.LIGHTGREEN_EX  # Defining colors


R = Fore.LIGHTRED_EX


Cyn = Fore.LIGHTCYAN_EX


Ylw = Fore.LIGHTYELLOW_EX





banner = """

     __     _                      _      __                 
  /\ \ \___| |___      _____  _ __| | __ / _\ ___ __ _ _ __  
 /  \/ / _ \ __\ \ /\ / / _ \| '__| |/ / \ \ / __/ _` | '_ \ 
/ /\  /  __/ |_ \ V  V / (_) | |  |   <  _\ \ (_| (_| | | | |
\_\ \/ \___|\__| \_/\_/ \___/|_|  |_|\_\ \__/\___\__,_|_| |_|
----------------------- [+] GHOSTH4CK3R -------------------


 """


def print_banner():


    print(Cyn + banner)





print_banner()





input("Press \'Enter\' To Scan > ")





def anim() :                # Scanning animation

   
    itms = [" Scanning /"," Scanning -"," Scanning \\"," Scanning |"]

    def spinning_cursor():
        while True:
            for cursor in itms:
   
                yield cursor

    spinner = spinning_cursor()
    for _ in range(50):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b')
    


def anim2() :

    os.system('clear')
    print_banner()


def ping_range(start,count) :








    prefix = "192.168.1."


    condition = "Unreachable" 


    condition2 = "timed out"


    list1 = []


    #list2 = []





    for xxx in range(start,start+count) :


        


        ip = prefix + str(xxx)


        code = "ping -c1 -s1 " + ip     


        code2 = "arp -a " + ip


        ping = os.popen(code).read()           


       


        if condition not in ping and condition2 not in ping and "100%" not in ping :  # Checking if IP's are alive


            #print(G + ip)               


            #list1.append(ip)


            try:


                arp = os.popen(code2).read().split('\n')  # Getting MAC Address


                arpS = str(arp)


                


                if "no match" not in arpS :
                	mac_loc = arpS.find(':')
                	mac = arpS[(mac_loc-2):(mac_loc+15)]
                else: 
                	#mac = "[ Not Found ]"
                	cmd3 = "ip address show wlan0"
                	macz = os.popen(cmd3).read()
                	maczl = macz.find("link/ether")
                	mac2 = macz[(maczl+11):(maczl+28)]
                	mac = mac2


                macsite_url = "https://macvendors.com/query/" + mac


                vendor_res = requests.get(macsite_url)   # Getting MAC Vendor





                if vendor_res.status_code == 200 :


                    vendor = vendor_res.text


                else:


                    vendor = "[Not Found]"





                IPnMACnVendor = ip + "  " + mac + "  " + vendor


                list1.append(IPnMACnVendor)


            


            except ModuleNotFoundError as e :             # If error occurs


                IPnNon = ip + str(e)


                list1.append(IPnNon)





    return list1 








tasks = []





with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor :  # Multi Threading


    for start in [1,11]:


        tasks.append(executor.submit(ping_range,start,10))


        


    for start in [21,31]:


        tasks.append(executor.submit(ping_range,start,10))


        


    for start in [41,51]:


        tasks.append(executor.submit(ping_range,start,10))


        


    for start in [61,71]:


        tasks.append(executor.submit(ping_range,start,10))


        


    for start in [81,91]:


        tasks.append(executor.submit(ping_range,start,10))


        


    for start in [101,111]:


        tasks.append(executor.submit(ping_range,start,10))


        


    for start in [121,131]:


        tasks.append(executor.submit(ping_range,start,10))


        #GH0STH4CK3R


    for start in [141,151]:


        tasks.append(executor.submit(ping_range,start,10))


        


    for start in [161,171]:


        tasks.append(executor.submit(ping_range,start,10))


        


    for start in [181,191]:


        tasks.append(executor.submit(ping_range,start,10))





    for start in [201,211]:


        tasks.append(executor.submit(ping_range,start,10))





    for start in [221,231]:


        tasks.append(executor.submit(ping_range,start,10))





    for start in [241,248]:


        tasks.append(executor.submit(ping_range,start,7))

        os.system('clear')
        print_banner()
        for v in range(2):


            anim()


        


anim2()    





print(Cyn + "\nResults :")


print(G + "")





empty_tsk = 0





for task in tasks:  # Outputting Returned Values From each thread


    if len(task.result()) == 1 :  


        print(task.result()[0])


    elif len(task.result()) > 1 :


        for elmnt in range(len(task.result())) :


            print(task.result()[elmnt])


    elif len(task.result()) == 0 :


        empty_tsk += 1





if empty_tsk >= 254 :


    print(R + "No IP's Found !")


    


print(Cyn + "")    


input("Exit >>")


