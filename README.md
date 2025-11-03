# Ex.05 Design a Website for Server Side Processing
## Date: 02.11.2025

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :

math.html
```

<html>
    <head>
        <title>BMI_Calculator</title>
        <style>
            body {
                font-family: Arial;
                display: flex;
                justify-content: center;
                align-content: center;
                height: 100vh;
            }
            .powerbox {
                background-color: powderblue;
                border: 2px inset black;
                padding: 30px;
                text-align: center;
                height: 330px;
                width: 450px;
                display: block;
            }
            input[type="text"] {
                width: 80%;
                padding: 8px;
                margin: 10pypx;
                border: 2px solid black;
                background-color: teal;
            }
        </style>
    </head>

    <body>
        
        <br>
        <div class="powerbox">
            <h2 align="center">Power of a lamp filament in an Incandescent bulb<br>Bharath K (212224230036)</h2>
            <form method="POST">
            {%csrf_token %}
            <div class="formelt">
            Intensity: <input type="text" name="intensity" value="{{intensity}}" placeholder="Enter intensity">
            <br>
            <br>
            </div>
            <div class="formelt">
            Resistance: <input type="text" name="resistance" value="{{resistance}}" placeholder="Enter resistance">
            <br>
            <br>
            </div>
            <div class="formelt">
            <input  type="submit" value="Calculate">
            <br>
            <br>
            </div>
            <div class="formelt">
            Power: <input type="text" name="power" value="{{power}}">
            <br>
            </div>
            </form>
        </div>
    </body>
</html>

```
views.py
```
from django.shortcuts import render
def calculate_POWER(request):
  context = {}
  context['power'] = "0"
  context['intensity'] = "0"
  context['resistance'] = "0"
  if (request.method=="POST"):
    print("POST method is used")
    intensity = request.POST.get("intensity","0")
    resistance = request.POST.get("resistance","0")
    print("Request=", request)
    print("intensity=", intensity)
    print("resistance=", resistance)
    power = float(intensity)*(float(resistance)*float(resistance))
    context['power'] = power
    context['intensity'] = intensity
    context['resistance'] = resistance
    print("power=", power)
  return render (request,'lenovoapp/math.html',context)
```
urls.py
```
from django.contrib import admin
from django.urls import path
from lenovoapp import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('calculate_POWER/', views.calculate_POWER, name = "power"),
    path('', views.calculate_POWER, name="powerroot")
]
```

## SERVER SIDE PROCESSING:
![alt text](<Screenshot 2025-11-03 090642.png>)

## HOMEPAGE:
![alt text](<Screenshot 2025-11-03 090936.png>)

## RESULT:
The program for performing server side processing is completed successfully.
