import json
class get:
    def logmessage(id):
        with open('./db/logs/message.json', 'r') as f:
            prefixes = json.load(f)
        return int(prefixes[str(id)])

    def logrole(id):
        with open('./db/logs/role.json', 'r') as f:
            prefixes = json.load(f)
        return int(prefixes[str(id)])

    def logserveur(id):
        with open('./db/logs/serveur.json', 'r') as f:
            prefixes = json.load(f)
        return int(prefixes[str(id)])
    def wl(id):
        with open('./db/wl/wl.json', 'r') as f:
            prefixes = json.load(f)
        lenwl = len(prefixes['wl'])
        wllen = -1
        for i in range(0,lenwl):
            wllen + 1
            if prefixes['wl'][wllen]  == str(id):
                return True

    def owner(id):
        with open('./db/wl/owner.json', 'r') as f:
            prefixes = json.load(f)
        lenowner = len(prefixes['owner'])
        ownerlen = -1
        for i in range(0,lenowner):
            ownerlen + 1
            if prefixes['owner'][ownerlen]  == str(id):
                return True   
    def isowner(idowner):
        if idowner == 1067781397231697950:
            return True    
    def sanction(id) :
        with open('./db/antiraid/sanction.json', 'r') as f:
            prefixes = json.load(f)
        if prefixes[str(id)] == "derank":
            return "derank" 
class anti:
    def link(id):
        with open('./db/antiraid/antilink.json', 'r') as f:
            prefixes = json.load(f)
        if prefixes[f"{id}"] == "on":
            return  True
        else:
            return False
    def everyone(id):
        with open('./db/antiraid/antieveryone.json', 'r') as f:
            prefixes = json.load(f)
        if prefixes[f"{id}"] == "on":
            return  True
        else:
            return False   
    def channel(id):
        with open('./db/antiraid/channel.json', 'r') as f:
            prefixes = json.load(f)
        if prefixes[f"{id}"] == "on":
            return  True
        else:
            return False
    def role(id):
        with open('./db/antiraid/antirole.json', 'r') as f:
            prefixes = json.load(f)
        if prefixes[f"{id}"] == "on":
            return  True
        else:
            return False
    def webhook(id):
        with open('./db/antiraid/antiwebhook.json', 'r') as f:
            prefixes = json.load(f)
        if prefixes[f"{id}"] == "on":
            return  True
        else:
            return False
    def ban(id):
        with open('./db/antiraid/antiban.json', 'r') as f:
            prefixes = json.load(f)
        if prefixes[f"{id}"] == "on":
            return  True
        else:
            return False    
    def spam(id):
        with open('./db/antiraid/antispam.json', 'r') as f:
            prefixes = json.load(f)
        if prefixes[f"{id}"] == "on":
            return  True
        else:
            return False
  