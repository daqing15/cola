#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Copyright (c) 2013 Qin Xuye <qin@qinxuye.me>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Created on 2013-6-7

@author: Chine
'''

import os

from cola.core.opener import MechanizeOpener
from cola.core.urls import Url, UrlPatterns

from login import WeiboLogin
from parsers import MicroBlogParser, UserInfoParser

def login_hook(opener, **kw):
    username = kw['username']
    passwd = kw['password']
    
    loginer = WeiboLogin(opener, username, passwd)
    return loginer.login()

url_patterns = UrlPatterns(
    Url(r'http://weibo.com/aj/mblog/mbloglist.*', 'micro_blog', MicroBlogParser),
    Url(r'http://weibo.com/\d+/info', 'user_info', UserInfoParser),
)