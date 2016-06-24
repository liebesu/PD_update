# Copyright (C) 2010-2013 Claudio Guarnieri.
# Copyright (C) 2014-2016 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import os

_current_dir = os.path.abspath(os.path.dirname(__file__))
PD_UPDATE_ROOT = os.path.normpath(os.path.join(_current_dir, "..", ".."))
DATA_ROOT=os.path.normpath(os.path.join(PD_UPDATE_ROOT,"data"))
TMP_ROOT=os.path.normpath(os.path.join(PD_UPDATE_ROOT,"tmp"))
PACKED_ROOT=os.path.normpath(os.path.join(PD_UPDATE_ROOT,"packed"))
CUCKOO_VERSION = "0.1-dev"
CUCKOO_GUEST_PORT = 8000
CUCKOO_GUEST_INIT = 0x001
CUCKOO_GUEST_RUNNING = 0x002
CUCKOO_GUEST_COMPLETED = 0x003
CUCKOO_GUEST_FAILED = 0x004
GITHUB_URL = "https://github.com/liebesu/PD_update"
ISSUES_PAGE_URL = "https://github.com/liebesu/PD_update/issues"

LATEST_HTTPREPLAY = "0.1.11"
