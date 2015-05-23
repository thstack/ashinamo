from django.http import HttpResponse
from class_data import CpuClassData, NetClassData, IoClassData, MemClassData
import simplejson as json

# Create your views here.
def getcpu(request):
    cpudata = CpuClassData.CpuData()
    result = json.dumps(cpudata.compute_data()) 
    return HttpResponse(result)

def getmem(request):
    memdata = MemClassData.MemData() 
    result = json.dumps(memdata.get_data())
    return HttpResponse(result)

def getnet(request):
    netdata = NetClassData.NetData(['eth0'])
    result = json.dumps(netdata.compute_data())
    return HttpResponse(result)

def getio(request):
    iodata = IoClassData.IoData(['sda'])
    result = json.dumps(iodata.compute_data())
    return HttpResponse(result)
