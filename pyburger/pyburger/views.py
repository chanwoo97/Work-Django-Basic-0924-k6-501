from django.http import HttpResponse
from django.shortcuts import render

from burgers.models import Burger


def main(request):
    # return HttpResponse("Hello, world. 파이버거~~")
    return render(request, 'main.html')

def burger_list(request):
    # return HttpResponse("파이버거의 햄버거 목록입니다.~~~")
    burgers = Burger.objects.all()
    print("전체 햄버거 목록 : ", burgers)
    context = {'burgers': burgers}
    return render(request, 'burger_list.html', context)

def burger_search(request):
    # 1. 화면에서 검색어 받아와서
    # 2. DB에서 검색하고
    # 3. 검색 결과를 화면에 전달
    # search/?keyword=더블

    keyword = request.GET.get("keyword")
    # 유효성 체크
    if keyword is not None:
        burgers = Burger.objects.filter(name__icontains=keyword)
        # DB에서 조회
        print("keyword", keyword)
    else:
        burgers = Burger.objects.none()

    # 조회된 결과 데이터를 화면에 전달하기.
    context = {'burgers': burgers}
    return render(request, "burger_search.html", context)