## Having gotten it to work, here are the steps taken to create the database:

- In the terminal, at the project root directory, do:
>from my_app.models import * - - - (this includes the database object (db), as well as the User model and any other model)

>from my_app import create_app

>db.create_all(app=create_app()) - - - BOOM! The database file is created instantly.
	
- OR more conveniently, in the create_app function, just after the initialization of the database with the app, the database could be created with the app passed in as argument, as depicted in the create_app function:
>db.init(app=app)
>
>db.create_all(app=app)

The database is created only if none exists but to be on the safe side, it would be wise to check and ensure the database doesn't exist before creating it.
	

A thing of note is that because we're using the app factory pattern, we can't straightforwardly add anything (say a User instance called user) to the database via terminal using db.session.add(user) -- even though it is possible by creating an app context via some advanced "push" technique. Instead, we have to place such database functionality in a view function (as shown in the create_user function of the user view) and it works perfectly.
