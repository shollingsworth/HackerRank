#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __future__
import sys
import os
from ghost import Ghost
import json
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import fromstring
from bs4 import BeautifulSoup

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

        if self.debug:
            self.doc = json.load(open(self.save_file, 'r'))
        else:
            self.doc = self.__getDoc()

        if not self.doc:
            raise Exception("Error fetching HTML!")

        if not self.debug:
            self.__makeDir()
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
                    return json.loads(r.content)
        raise Exception("Error, could not find: {}".format(self.match_text))

    def __getHtml(self):
        body_html = self.doc.get('model',{}).get('body_html')
        if not body_html:
            raise Exception("Error, fetching body_html")
        return "{}{}{}".format('<html>',body_html,'</html>')

    def __makeDir(self):
        if not os.path.isdir(self.dirname):
            print("Making directory: {}".format(self.dirname))
            os.makedirs(self.dirname)

    def makeFiles(self):
        chead = self.doc.get('model',{}).get('python_template_head')
        ctemplate = self.doc.get('model',{}).get('python_template')
        ctail = self.doc.get('model',{}).get('python_template_tail')

        html = self.__getHtml()
        soup = BeautifulSoup(html,'html.parser')
        root = ET.fromstring(soup.prettify())

        hackdowns = []
        for i in root.findall(".//*[@class='hackdown-content']/*/pre"):
            hackdowns.append("".join([t for t in i.itertext()]))
            #hackdowns.append(i.text.strip())
        #grab the last two elements, throw away the first
        matches = {
            'challenge_sample_output' : hackdowns.pop(),
            'challenge_sample_input' : hackdowns.pop()
        }
        for fn,content in matches.items():
            fp = "{}/{}".format(self.dirname,fn)
            print("Writing: {}".format(fp))
            if self.debug:
                print(fp,content)
            else:
                open(fp, 'w').write(content)

        fp = "{}/{}".format(self.dirname,"main2.py")
        template_doc="""#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
#-- HEAD
{}
sys.stdin = open("./challenge_sample_input", 'r')

#-- TEMPLATE
{}

#--- TAIL
{}

#-------- CUSTOM
if __name__ == '__main__':
    s = raw_input()
    i = int(raw_input())
    arr = map(int, raw_input().split())
        if self.debug:
            print(fp,template_doc)
        else:
            open(fp, 'w').write(template_doc)
""".format(chead,ctemplate,ctail)
        open(fp, 'w').write(template_doc)

"""===================================================
MAIN
==================================================="""
if len(sys.argv) > 1:
    turl = sys.argv[1]
else:
    turl = raw_input().strip()

#turl = "https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem"
if not turl: raise Exception("Error, url is not defined!")
s = ScrapeHackerRank(
    url=turl,
    match_text='Sample Input',
)
try:
    s.makeFiles()
except:
    #save output to test against
    print("ERROR! --- something went wrong. Saving output")
    s = ScrapeHackerRank(
        url=turl,
        match_text='Sample Input',
        save=True,
        #save=True,
        #debug=True,
    )
