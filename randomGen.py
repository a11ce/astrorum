from genlang import language

def shipName(lang = None):
    if not lang:
        lang = language.Language()
        return lang.newMorpheme().capitalize(), lang
        
    return lang.newMorpheme().capitalize()

def personName(lang = None):
    return shipName(lang)