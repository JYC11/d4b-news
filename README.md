# Django For Beginners Chapter 6~: News

I set up a WSL2 environment in windows in anticipation for Django For Professionals where I have to use actual databases, docker and other stuff. I'm getting used to the new environment but I can't wait to get a M1X macbook pro because windows is still quite clunky in terms of development imo.

The news app is the final project this book offers and it nicely wraps up all the topics covered so far and expands upon some previous topic.

## New topic: Custom User Models
I skipped over elaborating on the basic user models in the blog section of the book because I knew that in actual applications, the user auth may not be as simple as the basic stuff Django provides. The Custom User Model that allows django devs to customise auth is far more interesting.

It starts off by creating a custom model by importing an AbstractUser model. From studying Java I know that Abstract Classes act as somewhat templates for other classes to follow when they inherit them so I guess this does the same.

Then with the custom model, a custom form is created in forms.py and then the rest(views.py, urls.py) act the same way by importing forms and creating views and urls.

## Misc topics: Bootstrap, HTML and Emails.
Not really into frontend stuff and not gonna spend time on it since I'm focused on learning Django.

The email stuff was deceptively easy to set up by just putting a few things in the settings file and signing up to a email service. Things may end up getting more complicated but stuff seems just so easy?

## Revising old topics: CRUD
The CRUD function from the previous chapters got touched on again but with much brevity since it was a topic that was already covered. The steps are(very simplified) going from route level to model level:

1. Add routes to urls
2. Make views
3. Make html pages to render with the views using models

## New topic: Authorization
To summarise: not letting not-logged in users edit or update or see posts.
Done easily by importing and using LoginRequiredMixins and UserPassesTestMixin

## New topic: Relations
Relationships between data aren't new topics for me per se but how Django does it was new for me. Instead of making a Comments app, I just created a model and linked it to the frontend and admin with a few edits. The book doesn't cover adding comments in the article detail page itself but I can't be bothered with the HTML for now. Someday I'll have to learn frontend.

## New topic: Deployment
The book now covers stuff to get ready for deployment.
1. Setting env variables and hiding secret keys(forgot about those and just pushed them to github woops)
2. Generating static files with whitenoise
3. Using Gunicorn for something? Will need to google
4. Updating database so that is uses a Postgres db instead of a sqlite3 db
5. Setting allowed hosts
6. Setting Debug to False

## Tests
Almost forgot about tests but I'm glad I didn't. Wrote all the tests for user creation and CRUD so far.

Wrote tests for mixins after some googling. The book didn't really elaborate on it.