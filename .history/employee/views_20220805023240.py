from django.shortcuts import render

def emp(req):
    if req.method == "POST":
        form = EmployeeForm()