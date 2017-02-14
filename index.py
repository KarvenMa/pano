#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-08 13:45:07
# @Author  : Chen Kai (just_be_fine@163.com)

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'root.settings'

from django.core.wsgi import get_wsgi_application
from bae.core.wsgi import WSGIApplication
application = WSGIApplication(get_wsgi_application())