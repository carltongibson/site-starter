# Site Starter

Port of HTML5 Boilerplate to Django templates, plus static site generator.

## Features ##

* HTML5 Bolierplate (+ build script)
* Twitter Bootstrap
* Compass (SASS)
* Django Template based HTML generation

(I'll eventually get round to writing some pointers to the above but at this
stage I'm basically assuming you know what these are, and how to install/use
them -- or at least have someone who'll get you started. -- If that doesn't
apply ping me on Twitter [@carltongibson](https://twitter.com/#!/carltongibson)
and I'll try and bump it up the list.)

## Installation ##

1. **Clone or download files**. If cloning it's probably worth renaming master
branch and origin remote so you can track changes to site-starter but push to
your own remote. (February 20, 2012: I have notes on this. Ping me on Twitter
[@carltongibson](https://twitter.com/#!/carltongibson) if I've not posted them
and you want help with this.)
2. **Create a new Python virtualenv for your project.**
3. **$ pip install -r requirements.txt**
4. **GO!**

## Usage ##

### Watch for template changes

From root folder:

    $ watchmedo shell-command -c 'python static_site.py' layout/ templates/

This will build your HTML files into `www/`

### Compile your SASS files

From `www/`

    $ compass watch

### Serve the files during development

From `www/`

    $ python -m SimpleHTTPServer 8000

Site will be available at <http://localhost:8000/>

### Run the h5bp build script

From `www/build/`

    $ ant build

Now upload the `publish` folder.


## Feedback/Issues ##

* Ping me on Twitter: [@carltongibson](https://twitter.com/#!/carltongibson)
* Open an [Issue on
GitHub](https://github.com/carltongibson/site-starter/issues)

