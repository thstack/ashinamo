from django.shortcuts import render_to_response

# Create your views here.

def index(request):
    context = {
    }
    return render_to_response("index.html", context)

def cpu(request):
    context = {
    }
    return render_to_response("cpu.html", context)

def mem(request):
    context = {
    }
    return render_to_response("mem.html", context)

def io(request):
    context = {
    }
    return render_to_response("io.html", context)

def net(request):
    context = {
    }
    return render_to_response("net.html", context)
