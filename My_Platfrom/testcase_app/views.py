from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
# Create your views here.


def testcase_manage(request):
    return render(request, "testcase.html", {"type": "debug"})


def debug(request):
    if request.method == "POST":
        url = request.POST.get("url")
        method = request.POST.get("method")
        headers = request.POST.get("headers")
        type = request.POST.get("type")
        parameter = request.POST.get("parameter")
        print("url", url, "")
        print("method", method, "")
        print("headers", headers, "")
        print("type", type, "")
        print("parameter", parameter, "")

        json_headers = headers.replace("\'", "\"")
        try:
            headers = json.loads(json_headers)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"result": "headers类型错误"})

        json_par = parameter.replace("\'", "\"")
        try:
            payload = json.loads(json_par)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"result": "参数类型错误"})


        if method == "get":
            if headers == "":
                r = requests.get(url, params=payload)
                print("结果:", r.json())
            else:
                r = requests.get(url, params=payload, headers=headers)
                print("结果:", r.json())

        if method == "post":
            if type == "form":
                if headers == "":
                    r = requests.post(url, data=payload)
                    print("结果:", r.json())
                else:
                    r = requests.post(url, data=payload, headers=headers)
                    print("结果:", r.json())
            if type == "json":
                if headers == "":
                    r = requests.post(url, json=payload)
                    print("结果:", r.json())
                else:
                    r = requests.post(url, json=payload, headers=headers)
                    print("结果:", r.json())

        return JsonResponse({"result": r.text})
    else:
        return JsonResponse({"result": "请求方法错误！"})
