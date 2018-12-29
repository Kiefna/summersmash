#!/usr/bin/env python
try:
    from gevent import monkey
    monkey.patch_all()
except ImportError:
    pass

try:
    import psycogreen.gevent
    psycogreen.gevent.patch_psycopg()
except ImportError:
    pass

# these two lines are a workaround the 'data cutoff issue' issue described by jamadden @
# https://github.com/gevent/gevent/issues/778#issuecomment-205048050
# Note: unfortunately, runserver_plus isn't compatible with this fix
import django.core.servers.basehttp  # noqa: E402
django.core.servers.basehttp.WSGIRequestHandler.wbufsize = -1

import os  # noqa: E402
import sys  # noqa: E402

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "summersmash.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
