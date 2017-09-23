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

__match_main__ = '>Dashboard<'
__match_text__ = ',"body_html":"'
__lang_switches__ = {
    'python': {
        'head' : 'python_template_head',
        'main' : 'python_template',
        'tail' : 'python_template_tail',
        'fn'   : 'main.py'
    }
}

class ScrapeHackerRank(object):
    def __init__(
        self,
        url,
        debug=False,
    ):
        self.debug = debug
        self.url = url
        hr_dir = os.environ.get("HR_DIR")
        if not hr_dir:
            raise Exception("Error, set HR_DIR to your hacker_rank directory as an environment variable")
        if not os.path.isdir(hr_dir):
            raise Exception("Error, cannot find hackerRank directory: {}".format(hr_dir))

        self.save_file = "{}/debug.json".format(hr_dir)

        if self.debug:
            if not os.path.isfile(self.save_file):
                raise Exception("Error, debug enabled but save file is not populated")
            self.doc = json.load(open(self.save_file, 'r'))
        else:
            self.doc = self.__getDoc()

        if not self.doc:
            raise Exception("Error fetching HTML!")

        self.html = self.__getHtml()
        self.root = ET.fromstring(self.html)

        model = self.doc.get('model')
        if not model: 
            raise Exception("Error getting model from json! see {} for details".format(self.save_file))

        slug = model.get('slug')
        self.lang = model.get('track',{}).get('track_slug')
        if not slug:
            raise Exception("Error detecting model['slug'] see {} for details".format(self.save_file))
        if not self.lang:
            raise Exception("Error detecting model['track']['track_slug'] see {} for details".format(self.save_file))

        hr_name = slug
        template_fn = '{}/templates/{}'.format(hr_dir,self.lang)
        if not os.path.isfile(template_fn):
            raise Exception("Error, template for language: {} does not exist".format(template_fn))
        self.template_doc = open(template_fn,'r').read()

        self.dirname = "{}/{}/{}".format(hr_dir,self.lang,hr_name)
        self.__makeDir()
        print("Save file created: {}".format(self.save_file))
        open(self.save_file, 'w').write(json.dumps(self.doc, indent=5))

    def __getDoc(self):
        ghost = Ghost()
        matches = []
        g = ghost.start()
        g.open(
            address=self.url,
            user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.121 Safari/535.2',
            wait=False,

        )
        page,resources = g.wait_for_text(__match_main__)
        if page:
            for r in resources:
                if str(r.content).find(__match_text__) >= 0:
                    return json.loads(str(r.content))
        raise Exception("Error, could not find: {}".format(__match_text__))

    def __cleanString(self,string):
        #This was a nightmare... I'm probably still not doing it well but whatever
        #wondering if hackerrank is going to throw some unicode at me at some point lol
        string,n = codecs.utf_8_decode(string.encode('utf-8','ignore'))
        return "".join(map(chr,[63 if i > 128 else i for i in map(ord,list(string))]))

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

    def getLangSwitches(self):
        retarr = []
        for i in ['head','main','tail','fn']:
            retarr.append(__lang_switches__.get(self.lang,{}).get(i))
        return retarr

    def makeFiles(self):
        t_head, t, t_tail, main_fn = self.getLangSwitches()
        chead = self.doc.get('model',{}).get(t_head,'')
        ctemplate = self.doc.get('model',{}).get(t,'')
        ctail = self.doc.get('model',{}).get(t_tail,'')

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

        fp = "{}/{}".format(self.dirname,main_fn)
        data = self.template_doc.format(chead,ctemplate,ctail).strip()
        open(fp, 'w').write(data)

"""===================================================
MAIN
==================================================="""
"""
turl = "https://www.hackerrank.com/challenges/alphabet-rangoli/problem"
turl = "https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem"
turl = "https://www.hackerrank.com/challenges/merge-the-tools/problem"
turl = "https://www.hackerrank.com/challenges/py-the-captains-room/problem"
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
#    debug=True,
)
s.makeFiles()
