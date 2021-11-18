from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse('This is about page')


def home(request):
    return render(request, 'home.html')


def reverse(request):
    s = ''
    # "".join(s.split())
    user_text = request.GET['usertext']
    # можно также использовать принт для вывода результатов в терминал
    # print(user_text)
    # будем запрашивать эту информацию из страницы реверс.хтмл {{ usertext }}
    reversed_text = ''
    reversed_text = user_text[::-1]
    words_count = len(user_text.split())
    # print(words_count)
    return render(request,
                  'reverse.html', {
                      'usertext': user_text,
                      'reversed_text': reversed_text,
                      'words_count': words_count,

                  }
                  )
