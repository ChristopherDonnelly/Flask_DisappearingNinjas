'''
Build a flask application with the below functionality.

This exercise will help you practice URL routing, using views, and rendering static content.

These are the routes that you need to set up:

On the default page ('localhost:5000'), it should display a view that says "No ninjas here"
When user visits /ninja, it should display all four Ninja Turtles (Leonardo, Michelangelo, Raphael, and Donatello)

/ninja/[ninja_color], should display the corresponding Ninja Turtle (grab the color parameter out of the requested URL)

If user visits /ninja/blue, it should only display the Ninja Turtle Leonardo.
/ninja/orange - Ninja Turtle Michelangelo.
/ninja/red - Ninja Turtle Raphael
/ninja/purple - Ninja Turtle Donatello

If a user tries to hack into your web app by specifying a color or string combination other than the colors (Blue, Orange, Red, and Purple), example: /ninja/black or /ninja/123, then display the image notapril.jpg

You'll need to remember how to use static files for this assignment. Take a minute to refresh your memory back to the static files section if you need to :)
Click here to download the image files.
'''


# Import Flask to allow us to create our app, and import
# render_template to allow us to render HTML Files.
from flask import Flask, render_template, request, redirect

app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
                                          # are running the file directly or importing it as a module.

@app.route('/')                           # The "@" symbol designates a "decorator" which attaches the
                                          # following function to the '/' route. This means that
                                          # whenever we send a request to localhost:5000/ we will run
                                          # the following "hello_world" function.

def display_index():
    return render_template('index.html')    # Render the template and return it!

@app.route('/ninja')         

def display_ninja_home():
    return render_template('ninja.html')    # Render the template and return it!

@app.route('/ninja/<ninja_color>')         

def display_ninja(ninja_color = "home"):
    print ninja_color
    return render_template('ninja.html', color = ninja_color)    # Render the template and return it!

app.run(debug=True)                       # Run the app in debug mode.