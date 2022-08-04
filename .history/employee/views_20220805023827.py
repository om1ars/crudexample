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
    employees = Employeee.objects.all()
    return render(request,"show.html",{'employees':employees})  

def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  

def update(req, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(req.POST, instance = employee)

    if form.is_valid():
        form.save()

        return redirect("/show")
    return render(req, "edit.html", {'employee': employee)