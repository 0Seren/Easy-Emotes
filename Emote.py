# -*- coding: utf-8 -*-
class Emote():
    def __init__(self, text, tags):
        self.text = text
        self.tags = tags

    def __str__(self):
        ret = "Emote(\"" + self.text + "\", ["
        for tag in self.tags:
            ret += "\"" + tag + "\", "
        if ret.endswith(", "):
            ret = ret[:-2]
        ret += "])"
        return ret
#<?xml version="1.0" encoding="UTF-8"?>
#<emotes>
#    <emote>
#        <text>¯\_(ツ)_/¯</text>
#        <tags>
#            <tag>shrug</tag>
#            <tag>umadbro?</tag>
#        </tags>
#    </emote>
#</emotes>
    def toXMLstring(self):
        xml = "<emote>\n\t<text>" + self.text + "</text>\n\t<tags>\n"
        for tag in self.tags:
            xml += "\t\t<tag>" + tag + "</tag>\n"
        xml += "\t</tags>\n</emote>"
        return xml

#{
#    "text": "¯\_(ツ)_/¯",
#    "tags": [
#        "shrug",
#        "umadbro?"
#    ]
#}
    def toJSONstring(self):
        JSON = "{\n\t\"text\": \"" + self.text + "\",\n\t\"tags\": [\n"
        for tag in self.tags:
            JSON += "\t\t\"" + tag + "\",\n"
        if JSON.endswith(",\n"): #remove extra comma
            JSON = JSON[:-2] + "\n"
        JSON += "\t]\n}"
        return JSON
