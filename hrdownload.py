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
import html2text
import PySide

__default_lang__ = 'python'
__match_main__ = '>Dashboard<'
__match_text__ = ',"body_html":"'
__lang_switches__ = {
    'python': {
        'head' : 'python_template_head',
        'main' : 'python_template',
        'tail' : 'python_template_tail',
        'fn'   : 'main.py',
        'matches': {
            'challenge_sample_output' : ['sample output','strong'],
            'challenge_sample_input' : ['sample input','strong'],
        }
    },
    'ruby': {
        'head' : 'ruby_template_head',
        'main' : 'ruby_template',
        'tail' : 'ruby_template_tail',
        'fn'   : 'main.rb',
        'matches': {
            'hint' : ['hint','strong'],
        },
    },
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

        sys.stderr.write("Save file created: {}\n".format(self.save_file))
        open(self.save_file, 'w').write(json.dumps(self.doc, indent=5))

        model = self.doc.get('model')
        if not model: 
            raise Exception("Error getting model from json! see {} for details".format(self.save_file))

        slug = model.get('slug')
        self.lang = model.get('track',{}).get('track_slug')
        if self.lang not in __lang_switches__.keys():
            sys.stderr.write("hrm... seems track/slug_name '{}'' isn't in our languages. Defaulting to: '{}'".format(self.lang,__default_lang__))
            self.lang = __default_lang__
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
        if not body_html:
            raise Exception("Error, fetching body_html")
        html = "{}{}{}".format('<html>',body_html,'</html>')
        soup = BeautifulSoup(html,'html.parser')
        return soup.prettify()

    def __makeDir(self):
        if not os.path.isdir(self.dirname):
            sys.stderr.write("Making directory: {}\n".format(self.dirname))
            os.makedirs(self.dirname)

    def __getItext(self,node):
        return "".join([t for t in node.itertext()]).strip()

    def __getContent(self,which,mytag):
        next_match_skip_tags = ['div','style','svg','defs']
        p_iter = self.root.iter()
        for i in p_iter:
            t = self.__getItext(i).lower()
            fw = t.find(which)
            if fw >= 0 and i.tag == mytag:
                if self.debug:
                    sys.stderr.write("{}\n".format("-*-" * 20))
                    try: sys.stderr.write("{}/{}/{}\n".format(fw,i,i.tag))
                    except: pass
                    sys.stderr.write("{}\n".format(t))
                while True:
                    dtag = p_iter.next()
                    if dtag.tag in next_match_skip_tags: continue
                    text = self.__getItext(dtag)
                    if self.debug:
                        sys.stderr.write("Returning: {}\n".format(text))
                    return text
        return ''

    def getLangSwitches(self):
        retarr = []
        for i in ['head','main','tail','fn']:
            retarr.append(__lang_switches__.get(self.lang,{}).get(i))
        #sys.stderr.write("{}\n".format(retarr))
        return retarr

    def makeFiles(self):
        t_head, t, t_tail, main_fn = self.getLangSwitches()
        chead = self.doc.get('model',{}).get(t_head,'')
        ctemplate = self.doc.get('model',{}).get(t,'')
        ctail = self.doc.get('model',{}).get(t_tail,'')



        matches = __lang_switches__.get(self.lang,{}).get('matches')
        if not matches:
            raise Exception("Error, could not find matches in {}".format(__lang_switches__))


        for fn,content in matches.items():
            which, tag = content
            data = "\n".join(l.strip() for l in self.__getContent(which,tag).split("\n"))
            if not data:
                sys.stderr.write("content: {} / {} was not a match, skipping write\n".format(which,tag))
                continue
            fp = "{}/{}".format(self.dirname,fn)
            sys.stderr.write("Writing: {}\n".format(fp))
            if self.debug:
                sys.stderr.write("{} / {}\n".format(fp,data))
            else:
                open(fp, 'w').write(data)

        fp = "{}/{}".format(self.dirname,main_fn)
        data = self.template_doc.format(chead,ctemplate,ctail).strip()
        open(fp, 'w').write(data)

        gen_fp = "{}/{}".format(self.dirname,'content')
        sys.stderr.write("Writing: {}\n".format(gen_fp))
        open(gen_fp, 'w').write(html2text.html2text(self.html))
        #finally for cd in "hr" alias in bash
        sys.stdout.write("{}\n".format(self.dirname))

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
