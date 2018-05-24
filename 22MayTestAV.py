# -*- coding: utf-8 -*-
"""
Created on Tue May 22 14:31:39 2018

@author: john3
"""

import subprocess
import sys
version = 2.0
package = 'alpha_vantage'

subprocess.call([sys.executable, '-m', 'pip', 'install', '{}=={}'.format(package, version)])
print("harvey")