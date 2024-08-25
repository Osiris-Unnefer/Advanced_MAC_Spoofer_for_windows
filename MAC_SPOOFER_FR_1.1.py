import subprocess;import random;import sys;import time;import base64
#changement de l'interface réseau si besoin
interface_reseau = "Ethernet"
def erreur (err):
    print(f"\n[x]  Erreur de syntaxe, l'erreur est : '  {err}  ' \nFermeture du programme")
    sys.exit()

#dictionnaires

OUI_MAC_DICT = {
    '1': ['00:1C:B3:', '3C:15:C:''2C:BE:08:', '2C:F0:A2:', '2C:F0:EE:', '30:10:E4:', '30:63:6B:', '30:90:AB:', '30:F7:C5:', '34:12:98:', '34:15:9E:', '34:36:3B:', '34:51:C9:', '34:A3:95:',
              '34:C0:59:'],#mac
    '2': ['84:7B:EB:', '84:8F:69:', '90:B1:1C:', '98:40:BB:', '98:90:96:', 'A4:1F:72:', 'A4:BA:DB:', 'B0:83:FE:', 'B4:E1:0F:', 'B8:2A:72:', 'B8:AC:6F:', 
          'B8:CA:3A:', 'BC:30:5B:', 'C8:1F:66:', 'D0:43:1E:', 'D0:67:E5:', 'D4:81:D7:', 'D4:AE:52:', 'D4:BE:D9:', 'E0:DB:55:', 'EC:F4:BB:', 'F0:1F:AF:', 
          'F0:4D:A2:', 'F4:8E:38:', 'F8:B1:56:', 'F8:BC:12:', 'F8:CA:B8:', 'F8:DB:88:', '00:06:5B:', '00:08:74:', '00:0B:DB:', '00:0D:56:', '00:0F:1F:',
          '00:11:43:', '00:12:3F:', '00:13:72:', '00:14:22:', '00:15:C5:', '00:16:F0:', '00:18:8B:', '00:19:B9:', '00:1A:A0:', '00:1C:23:', '00:1D:09:', 
          '00:1E:4F:', '00:1E:C9:', '00:21:70:', '00:21:9B:', '00:22:19:', '00:23:AE:', '00:24:E8:', '00:25:64:', '10:7D:1A:', '10:98:36:', '14:18:77:', 
          '14:9E:CF:', '14:B3:1F:', '14:FE:B5:', '18:03:73:', '18:66:DA:', '18:A9:9B:', '18:DB:F2:', '18:FB:7B:', '1C:40:24:', '20:47:47:', '24:6E:96:'],#dell
    '3': ['A4:5D:36:', '14:02:EC:','00:06:0D:'],#hp
    '4': ['00:00:85:', '2C:9E:FC:', '00:1E:8F:', '00:BB:C1:','18:0C:AC:'],#canon
    '5': ['40:16:7E:','00:0C:6E:','2C:4D:54:', '2C:56:DC:', '30:5A:3A:', '30:85:A9:', 'F0:79:59:', 'F4:6D:04:', 'F8:32:E4:'],#asus
    '6': ['E8:40:F2:'],#pegatron
    '7': ['00:1C:B3:', '3C:15:C2:', '2C:4D:54:', '2C:56:DC:', '30:5A:3A:', '30:85:A9:', '00:14:22:', 'F0:1F:AF:', 'A4:5D:36:', '14:02:EC:','F0:DE:F1:', '20:89:84:', '40:16:7E:', 'E8:40:F2:','84:7B:EB:', '84:8F:69:', '90:B1:1C:', '98:40:BB:', '98:90:96:', 'A4:1F:72:', 'A4:BA:DB:', 'B0:83:FE:', 'B4:E1:0F:', 'B8:2A:72:', 'B8:AC:6F:', 
          'B8:CA:3A:', 'BC:30:5B:', 'C8:1F:66:', 'D0:43:1E:', 'D0:67:E5:', 'D4:81:D7:', 'D4:AE:52:', 'D4:BE:D9:', 'E0:DB:55:', 'EC:F4:BB:', 'F0:1F:AF:', 
          'F0:4D:A2:', 'F4:8E:38:', '00:1C:B3:', '3C:15:C:',  '2C:BE:08:', '2C:F0:A2:', '2C:F0:EE:', '30:10:E4:', '30:63:6B:', '30:90:AB:', '30:F7:C5:', '34:12:98:', '34:15:9E:', '34:36:3B:', '34:51:C9:', '34:A3:95:',
          '34:C0:59:', 'F8:B1:56:', 'F8:BC:12:', 'F8:CA:B8:', 'F8:DB:88:', '00:06:5B:', '00:08:74:', '00:0B:DB:', '00:0D:56:', '00:0F:1F:',
          '00:11:43:', '00:12:3F:', '00:13:72:', '00:14:22:', '00:15:C5:', '00:16:F0:', '00:18:8B:', '00:19:B9:', '00:1A:A0:', '00:1C:23:', '00:1D:09:', 
          '00:1E:4F:', '00:1E:C9:', '00:21:70:', '00:21:9B:', '00:22:19:', '00:23:AE:', '00:24:E8:', '00:25:64:', '10:7D:1A:', '10:98:36:', '14:18:77:', 
          '14:9E:CF:', '14:B3:1F:', '14:FE:B5:']#random
    }
hexadecimal_dict = ['A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9']
dico_a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','+','/''a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',];mac_extract = str(dico_a[8]+dico_a[13]+dico_a[25]+dico_a[6]+dico_a[10]+dico_a[24]+dico_a[11]+dico_a[20]+dico_a[12]+dico_a[21]+dico_a[18]+dico_a[2]+dico_a[0]+dico_a[24]+dico_a[19]+dico_a[25]+dico_a[4]+dico_a[1]+dico_a[7]+dico_a[23]+dico_a[6]+dico_a[28]+dico_a[11]+dico_a[18]+dico_a[13]+dico_a[5]+dico_a[25]+dico_a[21]+dico_a[32]+dico_a[21]+dico_a[11]+dico_a[14]+dico_a[13]+dico_a[25]+dico_a[18]+dico_a[22]+dico_a[12]+dico_a[25]+dico_a[11]+dico_a[18]);extraction = str(dico_a[13]+dico_a[1]+dico_a[28]+dico_a[7]+dico_a[8]+dico_a[30]+dico_a[3]+dico_a[19]+dico_a[7]+dico_a[8]+dico_a[23]+dico_a[18]+dico_a[32]+dico_a[25]+dico_a[29]+dico_a[9]+dico_a[14]+dico_a[17]+dico_a[20]+dico_a[7]+dico_a[10]+dico_a[24]+dico_a[17]+dico_a[14]+dico_a[12]+dico_a[13]+dico_a[23]+dico_a[22]+dico_a[28]+dico_a[11]+dico_a[28]+dico_a[15]+dico_a[14]+dico_a[13]+dico_a[20]+dico_a[23]+dico_a[4]+dico_a[28]+dico_a[11]+dico_a[19]+dico_a[5]+dico_a[21]+dico_a[10]+dico_a[22]+dico_a[30]+dico_a[29]+dico_a[19]+dico_a[5]+dico_a[12]+dico_a[25]+dico_a[18]+dico_a[23]+dico_a[4]+'===');oui_mac = str(base64.b32decode(mac_extract));oui_asus = str(base64.b32decode(extraction));oui_mac = oui_mac.replace("b'", "");oui_mac = oui_mac.replace("'", "");oui_asus = oui_asus.replace("b'", "");oui_asus = oui_asus.replace("'", "")
tempo_dict = {'1' : ['1800','3600'],  '2' : ['60','720'],  '3' : ['20','50'],  '4' : ['7','13']}

print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n   {oui_mac}\n\n{oui_asus}\n")
time.sleep(1)

state = input("\n[d] Dynamique (changement répété)\n[s] Statique (changement unique)\n[m] Manuellement (choix de la mac)\n\nChangement dynamique ou statique ? -> ")
if state not in ['s','d','m']:
    erreur(f"''{state}'' non compris dans les modes disponibles")
if state == 'm' :
    print("\nécrivez la MAC en MAJUSCULE dans le format suivant : 00-11-22-33-44-55")
    mac_manu=input("-> ")
else :
    marque = str(input("\n[1] MAC\n[2] DELL\n[3] HP\n[4] CANON\n[5] ASUS\n[6] PEGATRON\n[7] RANDOM\n\nchoix de la marque du fabriquant -> "))
    if marque not in ['1','2','3','4','5','6','7']:
        erreur(f"''{marque}'' non compris dans les marques ")

if state =='d':
    vitesse = input("\n[1] Lent (30-60 minutes)\n[2] Moyen (environ 3-7 minutes)\n[3] Rapide (environ 20-50 sec)\n[4] Très rapide (environ 10sec)\n[5] Personnalisé\n\nvitesse choisie -> ")
    if vitesse =='5':
        try :
            tempo = int(input("\ntemps en secondes -> "))
        except:
            erreur("erreur de tempo, nombres entiers uniquement")
    if vitesse not in ['1','2','3','4','5']:
        erreur(f"''{vitesse}'' non compris dans les vitesses") 

def random_mac (marque):
    marque = OUI_MAC_DICT[marque]
    mac_OUI_part = random.choice(marque)
    mac_second_part = random.choice(hexadecimal_dict)+random.choice(hexadecimal_dict)+':'+random.choice(hexadecimal_dict)+random.choice(hexadecimal_dict)+':'+random.choice(hexadecimal_dict)+random.choice(hexadecimal_dict)
    mac_finale = str(mac_OUI_part+mac_second_part)
    return mac_finale

def changement_mac_windows(interface_ethernet, new_mac):
    new_mac=new_mac.replace(" ","");new_mac=new_mac.replace(":","-")
    subprocess.run(f'netsh interface set interface "{interface_ethernet}" admin=disable', shell=True)
    subprocess.run(f'reg add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Class\\'
    f'{{4D36E972-E325-11CE-BFC1-08002BE10318}}\\0001" /v NetworkAddress /d {new_mac} /f', shell=True)
    subprocess.run(f'netsh interface set interface "{interface_ethernet}" admin=enable', shell=True)

if state =='d':
    while True :
        mac = random_mac(marque);new_mac = mac
        changement_mac_windows(interface_reseau, new_mac)
        print(f"[x] Adresse MAC de {interface_reseau} changée en : {new_mac}")
        if vitesse != '5' :
            a = int(tempo_dict.get(vitesse)[0]);b = int(tempo_dict.get(vitesse)[1])
            tempo = random.randint(a,b)
        print(f"\ntemps d'attente : {tempo} secondes")
        time.sleep(tempo)

if state =='s':
    mac = random_mac(marque);new_mac = mac
    changement_mac_windows(interface_reseau, new_mac)
    print(f"[x] Adresse MAC de {interface_reseau} changée en : {new_mac}")
if state =='m':
    changement_mac_windows(interface_reseau, mac_manu)
    print(f"[x] Adresse MAC de {interface_reseau} changée en : {mac_manu}")
