#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __future__
import sys
import os
import codecs
from ghost import Ghost
import json
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import fromstring
from bs4 import BeautifulSoup
import PySide

class ScrapeHackerRank(object):
    def __init__(
        self,
        url,
        match_text,
        debug=False,
        save=False,
    ):
        self.debug = debug

        hr_dir = os.environ.get("HR_DIR")
        if not hr_dir:
            raise Exception("Error, set HR_DIR to your hacker_rank directory as an environment variable")
        try:
            hr_name = url.split('/')[-2]
        except:
            hr_name = None
        if not hr_name:
            raise Exception("Error extracting section name from url: {}".format(url))
        if not os.path.isdir(hr_dir):
            raise Exception("Error, cannot find hackerRank directory: {}".format(hr_dir))

        self.dirname = "{}/python/{}".format(hr_dir,hr_name)
        self.match_text = match_text
        self.url = url
        self.save_file = "{}/debug.json".format(self.dirname)
        self.__makeDir()

        if self.debug:
            self.doc = json.load(open(self.save_file, 'r'))
        else:
            self.doc = self.__getDoc()

        if not self.doc:
            raise Exception("Error fetching HTML!")

        self.html = self.__getHtml()
        self.root = ET.fromstring(self.html)

        if save:
            fh = open(self.save_file, 'w').write(json.dumps(self.doc, indent=5))
            print("Save file initiated => {}, exiting".format(self.save_file))
            sys.exit()

    def __getDoc(self):
        ghost = Ghost()
        matches = []
        g = ghost.start()
        g.open(
            address=self.url,
            user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.121 Safari/535.2',
            wait=False,

        )
        page,resources = g.wait_for_text(self.match_text)
        if page:
            for r in resources:
                if str(r.content).find(self.match_text) >= 0:
                    print("Save file created: {}".format(self.save_file))
                    fh = open(self.save_file, 'w').write(r.content)
                    return json.loads(str(r.content))

        raise Exception("Error, could not find: {}".format(self.match_text))

    def __cleanString(self,string):
        string,n = codecs.utf_8_decode(string.encode('utf-8','ignore'))
        repl_with =  63 #ord '?'
        ord_arr = map(ord,list(string))
        new_arr = []
        for i in ord_arr:
            if i > 128:
                new_arr.append(repl_with)
            else:
                new_arr.append(i)
        return "".join(map(chr,new_arr))

    def __getHtml(self):
        body_html = self.doc.get('model',{}).get('body_html','')
        body_html = self.__cleanString(body_html)
        #html_save = "{}/debug.html".format(self.dirname)
        #print("Saving html: {}".format(html_save))
        #open(html_save, 'w', encoding='utf-8').write(body_html)
        #wfh.write(body_html)
        if not body_html:
            raise Exception("Error, fetching body_html")
        html = "{}{}{}".format('<html>',body_html,'</html>')
        soup = BeautifulSoup(html,'html.parser')
        return soup.prettify()

    def __makeDir(self):
        if not os.path.isdir(self.dirname):
            print("Making directory: {}".format(self.dirname))
            os.makedirs(self.dirname)

    def __getItext(self,node):
        return "".join([t for t in node.itertext()]).strip()

    def __getContent(self,which):
        next_match_skip_tags = ['div','style','svg','defs']
        if which not in ['input','output']:
            raise Exception("Error, invalid switch: {}".format(which))

        p_iter = self.root.iter()
        for i in p_iter:
            t = self.__getItext(i).lower()
            fw = t.find(which)
            if self.debug:
                print("======================")
                print(fw,i,i.tag)
                print(t)
            if fw > 0 and i.tag == 'strong':
                while True:
                    dtag = p_iter.next()
                    if dtag.tag in next_match_skip_tags: continue
                    if self.debug: print("Returning: {}".format(dtag))
                    return self.__getItext(dtag)
        return ''

    def makeFiles(self):
        chead = self.doc.get('model',{}).get('python_template_head','')
        ctemplate = self.doc.get('model',{}).get('python_template','')
        ctail = self.doc.get('model',{}).get('python_template_tail','')

        matches = {
            'challenge_sample_output' : self.__getContent('output'),
            'challenge_sample_input' : self.__getContent('input'),
        }

        for fn,content in matches.items():
            fp = "{}/{}".format(self.dirname,fn)
            print("Writing: {}".format(fp))
            if self.debug:
                print(fp,content)
            else:
                open(fp, 'w').write(content)

        fp = "{}/{}".format(self.dirname,"main.py")
        template_doc="""#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
print("===" * 30)
print("SAMPLE INPUT:")
print("===" * 30)
print(open("./challenge_sample_input", 'r').read())
sys.stdin = open("./challenge_sample_input", 'r')
print("===" * 30)
print("SAMPLE OUTPUT:")
print("===" * 30)
print(open("./challenge_sample_output", 'r').read())
print("===" * 30)
print("START")
print("===" * 30)

{}

{}

{}
""".format(chead,ctemplate,ctail).strip()
        open(fp, 'w').write(template_doc)

"""===================================================
MAIN
==================================================="""
"""
turl = "https://www.hackerrank.com/challenges/alphabet-rangoli/problem"
turl = "https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem"
turl = "https://www.hackerrank.com/challenges/merge-the-tools/problem"
turl="https://www.hackerrank.com/challenges/py-the-captains-room/problem"
"""

"""
"""
if len(sys.argv) > 1:
    turl = sys.argv[1]
else:
    turl = raw_input().strip()

if not turl: raise Exception("Error, url is not defined!")
s = ScrapeHackerRank(
    url=turl,
    match_text='Sample Output',
#    debug=True,
)
s.makeFiles()
