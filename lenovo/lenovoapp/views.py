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