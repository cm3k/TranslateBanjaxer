import googletrans
from googletrans import Translator
import random
translator = Translator()
print("=========================================")
print("=== TRANSLATE BANJAXER BY CASHMAN3000 ===")
print("===       https://www.cm3k.xyz/       ===")
print("=========================================")
toTranslate = input("Text to translate: ")
amount = input("Amount of times to translate: ")
outputLanguage = input("Language to output in ISO-639 code (Default is english/en): ")
languages = ("af","sq","am","ar","hy","az","eu","be","bn","bs","bg","ca","ceb","ny","zh-tw","zh-cn","co","hr","cs","da","nl","en","eo","et","tl","fi","fr","fy","gl","ka","de","el","gu","ht","ha","iw","he","hi","hmn","hu","is","ig","id","ga","it","ja","jw","kn","kk","kh","km","ko","ku","ky","lo","la","lv","lt","lt","lb","mk","mg","ms","ml","mt","mi","mr","mn","my","ne","no","or","ps","fa","pl","pt","pa","ro","ru","sm","gd","sr","st","sn","sd","si","sk","sl","so","es","su","sw","sv","tg","ta","te","th","tr","uk","ur","ug","uz","vi","cy","xh","yi","yo","zu")

lang = random.choice(languages)
print("Translating to " + lang + "...")
translation = translator.translate(toTranslate, dest=lang).text
for i in range(1,(int(amount)-1)):
    lang = random.choice(languages)
    print("Translating to " + lang + "...")
    translation = translator.translate(translation, dest=lang).text
if outputLanguage == "":
    print("Translating to en...")
else:
    print("Translating to " + outputLanguage + "...")
if outputLanguage == "":
    output = translator.translate(translation, dest="en").text
else:
    output = translator.translate(translation, dest=outputLanguage).text
print(output)
input("\nPress ENTER to Close")
