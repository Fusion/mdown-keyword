import re
from markdown import markdown


# This module lets you mix markdown and rich text
# It follows the same conventions as the mdown module.
#
# You can install mdown or pagedown and use
# python manage.py pygments_styles <style name> >
#         <your theme>/static/css/pygments.css
#
# python manage.py collectstatic
#
# To enable markdown rendering, add to settings.py:
# RICHTEXT_FILTER = 'mdown-keyword.filters.codehilite'
# or if you do not need code hilighting:
# RICHTEXT_FILTER = 'mdown-keyword.filters.plain'
#
# In a blog post or page, entering the markdown interpreter
# is done using [markdown] and exiting it using [/markdown]
#
def _render(content, args=[]):
    cl_pattern = re.compile(r'<[^>]*?>')
    md_pattern = re.compile(r'\[markdown\](.*?)\[/markdown\]',
                            re.DOTALL | re.M)

    return re.sub(md_pattern,
                  lambda _: markdown(re.sub(
                                     cl_pattern, '',
                                     _.group(1).
                                     replace('<br />', '\n').
                                     replace('</div>', '\n').
                                     replace('&nbsp;', ' ')),
                                     args),
                  content)


def codehilite(content):
    return _render(content, ['codehilite', ])


def plain(content):
    return _render(content)
