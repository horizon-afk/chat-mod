cmdWords = ["leave","play","help","pause", "skip", "queue", "clear", "resume","stop"]


channel = ""
message = ""

def deleteMsg():
    global channel
    purge = False
    
    # the data type of channel is originally "discord.channel.TextChannel"
    channel = str(channel)
  
    if bool(message) is True:
        # for messages in music channel
        if channel == "music":
      
            if (message.split()[0][0] != "!"):
                
                purge = True

                           
        
            elif message.split()[0][1:] not in cmdWords:
                    purge = True
            
                
                
        # for messages outside music channel
        else:
    
            if message.startswith("!"):
           
                purge = True
              
                                
    return purge
        
# TODO: function to interact with bot without refering to the code to allow new words        
def botInteract():
    pass
