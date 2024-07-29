# Python Standard Library Dependencies


# External Dependency Imports
from flask import render_template, Blueprint, current_app

# Internal Dependency Imports
from App.Data.db_utils import add_document

#######################################################################################
#                                        Notes:                                       #
#                                                                                     #
# Things done in this file:                                                           #
# 1. Define the main blueprint for the application                                    #
# 2. Define the index route for the application                                       #
#                                                                                     #
#######################################################################################

# Define the main blueprint for the application
main_blueprint = Blueprint("main", __name__)

# Define the application routes
@main_blueprint.route("/")
def index():
    add_document(current_app, "Hello", "world")
    return render_template("index.jinja")

