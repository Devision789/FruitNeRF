#!/home/se86kimy/anaconda3/envs/nerfstudio/bin/python
# -*- coding: utf-8 -*-
import re
import sys
from fruit_nerf.scripts.process_data import entrypoint

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(entrypoint())