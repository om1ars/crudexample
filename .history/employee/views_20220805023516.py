from django.shortcuts import render
from employee.forms import EmployeeForm
from employee.models import Employee


def emp(req):
    if req.method == "POST":
        form = EmployeeForm(req.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
        else:
            form = EmployeeForm()
        return render(request, 'index.html', {'form': form})

def show(req):
    