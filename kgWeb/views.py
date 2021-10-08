from django.http import HttpResponse
from django.shortcuts import render
import json
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb as sql 


db = sql.connect(host = "hongkong.chn.ryan1202.wang",
                     user = "node",
                     passwd = "password",
                     db = "node" )
cursor = db.cursor()




def index(request):
    context = {}
    return render(request, 'head.html', context)

# def nodes(request):
#     context = {}
#     return render(request, "nodes.html", context)


def ajax_info(request):
    return HttpResponse("This is ajax info")


def get_node_info(node_ip):
    command = "select * from node where node_ip = " + "\"" + node_ip +"\""
    cursor.execute(command)
    results = cursor.fetchall()
    for item in results:
        return item[4]

def get_emoji(status):
    ret = ""
    if status == "pending":
        ret = "🟠"
    elif status == "OK":
        ret = "🔵"
    elif status == "FAILED":
        ret = "🔴"
    return ret + status

def status_info(request):
    nodesStatus = {
        "node1": get_emoji(get_node_info("10.2.25.5")),
        "node2": get_emoji(get_node_info("10.2.25.41"))
    }
    
    return HttpResponse(json.dumps(nodesStatus))


# def get_diag_info():
#     diaginfo = {}
#     data_legends = []
#     return diaginfo

# def result(request):
#     if 'inputstr' in request.GET:
#         context = {}

#         diaginfo = get_diag_info()
#         context['diaginfo'] = str(json.dumps(diaginfo))
#         return render(request, 'result.html', context)
#         # return HttpResponse()
#         # return HttpResponse(request.GET['inputstr'])
#     else:
#         return HttpResponse("404")
#     # context = {}

#     # diaginfo = get_diag_info()
#     # context['diaginfo'] = str(json.dumps(diaginfo))
#     # return render(request, 'result.html', context)
#     # return HttpResponse()

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
