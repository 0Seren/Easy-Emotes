# -*- coding: utf-8 -*-
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
from Emote import Emote
from Gui import Application

def importxmlemotes(filename):
    retemotes = []
    emotes = ET.parse(filename).getroot() #TODO: Handle parse errors
    for emote in emotes:
        text = ""
        tags = []
        for data in emote:
            if data.tag == "text":
                text = data.text.encode('utf-8')
            elif data.tag == "tags":
                for tag in data:
                    tags.append(tag.text.encode('utf-8'))
        retemotes.append(Emote(text, tags))
    return retemotes

def main():
    emotes = importxmlemotes("emotes.xml")
    tagstoemotes = []
    for emote in emotes:
        for tag in emote.tags:
            tagstoemotes.append((tag, emote))
    app = Application(searchtable = tagstoemotes)
    app.master.title('Easy Emotes')
    app.mainloop()



main()
