from flask import Flask, url_for, redirect, Response, request, render_template,session
from .. import mongo
from..models.services import service

def landing():
    return render_template("landingpage.html")


# #Display Service
def services():
        return render_template("service.html")

# Display AdminService

def AdminServices(): 
    return render_template("AdminService.html", service = services)


# Display Service
def services(): 
    return render_template("service.html",)



def Concept_Design():
        return render_template("Concept Design.html")


def Material_Finish():
        return render_template("Material and Finish.html")


def Styling_Decoration():
        return render_template("Styling and Decoration.html")


def Renovation_Remodeling():
        return render_template("Renovation and Remodeling.html")

