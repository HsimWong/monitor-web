from django.http import HttpResponse
from django.shortcuts import render
import json 

def index(request):
    return render(request, 'head.html')
def get_diag_info():
    diaginfo = {}
    data_legends = []
    return diaginfo

def result(request):
    if 'inputstr' in request.GET:
        context = {}
    
        diaginfo = get_diag_info()
        context['diaginfo'] = str(json.dumps(diaginfo)) 
        return render(request, 'result.html', context)
        # return HttpResponse()
        # return HttpResponse(request.GET['inputstr'])
    else:
        return HttpResponse("404")
    # context = {}
    
    # diaginfo = get_diag_info()
    # context['diaginfo'] = str(json.dumps(diaginfo)) 
    # return render(request, 'result.html', context)
    # return HttpResponse()

''' A typical diagram info should be like this
diaginfo = {"type": "force",

    "categories": [
        {
            "name": "甲公司",
            "keyword": {},
            "base": "网格关系"
        }
    ],
    "nodes":  [

        {
            "name": "甲公司A股东",
            "value": 8,
            "symbolSize": 25,
            "category": 0,
            "itemStyle": {
                "color": '#3398db'
            }
        }
    ],
    "links": [ 
               {
                   "source": 10,
                   "target": 13
                   }
              ]
}
'''
