from lxml import etree
import os
import json

def main():
    lpts = []
    for subdir, dirs, files in os.walk(os.getcwd()):
        for filename in files:
            filepath = subdir + os.sep + filename
            if filepath.endswith(".xml"):
                data = open(filepath)
                tree = etree.parse(data)
                for sentence in tree.xpath("//sentence"):
                    for word in sentence.xpath("token"):
                        lpf = ""
                        if "lemma" in word.attrib:
                            lemma = word.attrib["lemma"]
                            parse = word.attrib["morphology"]
                            form = word.attrib["form"]
                            lpt = lemma + " " + parse + " " + form
                            lpts.append(lpt)
                data.close()
    new_data = json.dumps(lpts, indent=4, ensure_ascii=False)
    g = open("lemParForm.json", 'w')
    g.write(new_data)
    g.close()

                    
main()
