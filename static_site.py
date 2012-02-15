import os

from django.conf import settings
from django.template import Template, Context
from django.template.loader import get_template

# Configure the template loaders as per:
#
# https://docs.djangoproject.com/en/1.3/ref/templates/api/#configuring-the-template-system-in-standalone-mode
#
# NOTE: Add pwd (as this is what we get from os.walk)
#   - Templates will include|extend|ssi 'layout/...'
settings.configure(
    TEMPLATE_DIRS=(os.path.dirname(__file__),)
)

# Now lets walk the templates dir and write to www.
root = './templates'

for dirpath, subdirs, filenames in os.walk(root):
    for name in filenames:
        # get template and render
        template_path = os.path.join(dirpath, name)
        t = get_template(template_path)
        html = t.render(Context({})) # Empty context is required.

        # and write
        write_dir = dirpath.replace("templates", "www", 1)
        if not os.path.exists(write_dir):
            os.makedirs(write_dir)
        write_path = os.path.join(write_dir, name)

        write_file = open(write_path, 'w')
        write_file.write(html)
        write_file.close()

        print "Wrote: %s" % write_path



