An add-on for mdown, allowing editors to mix rich text and markdown code.
It follows the same conventions as the mdown module.

To install:

Open <mezzanine home>/settings.py

Add or edit:

To enable markdown rendering,

    RICHTEXT_FILTER = 'mdown-keyword.filters.codehilite'

or if you do not need code hilighting

    RICHTEXT_FILTER = 'mdown-keyword.filters.plain'

Add to INSTALLED_APPS

    "mdown-keyword",

Optional:

You can install mdown or pagedown and use

    python manage.py pygments_styles <style name> >
        <your theme>/static/css/pygments.css

    python manage.py collectstatic

To use:

In a blog post or page, entering the markdown interpreter
is done using [markdown] and exiting it using [/markdown]
