# Flask Blueprint Static Example

This example shows the working way to:

- use flask blueprints
- ensure that static files (css, js and images etcetera) work as expected while using blueprints


## What are blueprints in flask?
Blueprints are a way to build an app using flask such that the app is very scalabe, by ensuring that the app is split into different modules with each module having all its resources independent of other modules. This means that several developers can split the task by working on one module each, independent of the other developer, and once everything is put together it becomes a full unit. Modules can be added/removed without affecting the overall functionality of the app, as they work independently of each other.


## So why then is this example really necessary?
While using Flask to build a simple app without blueprints, it usually causes no issues to get the static files (css, js, images etcetera) to display. However, when using blueprints a lot of users run into problems because flask tries to locate the static directory from the root path of the project (where the entry file, run.py, is). This example shows just what to do to ensure that flask uses the blueprint to locate the static files in the corresponding module (app/static in this case).


## So what are the most critical points to make of the example?
- create the blueprint, WITH the name of the static folder specified in the format as shown:
	> views_bp = Blueprint("views", \_\_name\_\_, template_folder="templates", static_folder="static")

- in the html template, ".static" is used, NOT "static" -- so that it references the static file for the blueprint, and NOT from the root of the web app.
	> <link rel="stylesheet" href="{{url_for('.static', filename='css/style.css')}}">

- in the main app instance, DISABLE static folder by setting it to None -- so as to allow the blueprint's static folder to be used.
	> app = Flask(\_\_name\_\_, static_folder=None)

> The drawback to this method is that you can only use static files in blueprints, and not from anywhere else (such as the root directory), since the static_folder has been set to None. This removes the possibility of combining an overall css styling from a parent directory together with a blueprint's unique css styling.



# Another Method (with url_prefix)
- simply ensure that all blueprints have been registered with a url_prefix. A good convention for a suitable url_prefix is to use the view name
>	e.g "/home"
- ".static" (not "static") is also used in the html templates. The full syntax is actually blueprintname.static 
> 	e.g href="{{url_for('home.static', filename='css/style.css'}}"


> This method makes it possible to use an overall styling (non-blueprint) together with a blueprint styling. The only trade-off is that url_prefixes must be used.
