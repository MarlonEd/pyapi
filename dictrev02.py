#!/usr/bin/python3

def main():
  


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]
print(f"My {nightmare[0]['user']['name']['first']}! The {nightmare[0]['kumquat']} do {nightmare[0]['d']}!!")



    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

print(f"My {[1][1]}! The {[1][0]} do {[3]}!")

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
print(f"My {[1][0]}! The {[1][1]} do {[3]}!")

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]
    
print(f"My {[1][0]}! The {[1][1]} do {[3]}!")    
    
    #  firewalldict = {'sip':'5060', 'ssh':'22', 'http':'80'}

    ## display the current state of our dictionary
   #  print(firewalldict)

    ## add another entry to the dict
    ## notice that https maps to an INT, not a STRING
    # firewalldict['https'] = 443

    ## display the dict with the new entry for host4
   #  print(firewalldict)

    ## display some dictionary data
    #print('The print statement can be passed multiple items, provided they are separated by commas')
    #print("The port in use for HTTP Secure is:", firewalldict['https'])

    ## this SHOULD fail but it will not because we are using the .get method
    #print("A safer way to recall that data is to use the .get method:", \
     # firewalldict.get('razzledazzlerootbeer'))
    
    ## use the .keys method to return a list of keys
    #print(firewalldict.keys())
    
    ## use the .values method to return a list of values
    #print(firewalldict.values())
    
    ## remove a single key from the dict
    #del firewalldict["sip"]
    #print(firewalldict)

if __name__ == "__main__":
    main()
