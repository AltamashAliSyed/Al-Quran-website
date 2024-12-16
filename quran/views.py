from django.shortcuts import render

# Create your views here.
import requests
from django.http import JsonResponse
from .models import wadu
def surah(request):
    response = requests.get("http://api.alquran.cloud/v1/surah")
    surah = response.json().get('data',[])

    return render(request, 'surah.html', {'surah': surah})


def surah_detail(request, surah_number):
    
    arabic_response = requests.get(f"http://api.alquran.cloud/v1/surah/{surah_number}")
    arabic_data= arabic_response.json()

    english_response=requests.get(f"http://api.alquran.cloud/v1/surah/{surah_number}/en.sahih")
    english_data = english_response.json()

    if arabic_data['status'] =='OK' and english_data['status'] =='OK':
        ayahs=[]
        for arabic_ayah,english_ayah in zip(arabic_data['data']['ayahs'] , english_data['data']['ayahs']):
            ayah_number = arabic_ayah['number']
            audio_url = f"https://cdn.islamic.network/quran/audio/128/ar.alafasy/{ayah_number}.mp3"

            ayahs.append({
                'number':arabic_ayah['numberInSurah'],
                'arabic_text':arabic_ayah['text'],
                'english_text':english_ayah['text'],
                'audio_url': audio_url,


            })
    

    return render(request , 'surah_detail.html',{'ayahs':ayahs, 'surah_name':arabic_data['data']['englishName']})




def juz(request):
    response = requests.get("http://api.alquran.cloud/v1/juz/30/en.asad")
    data = response.json().get('data', {})
    ayahs = data.get('ayahs', [])

    context = {
        'ayahs': ayahs,  
        'juz_numbers':range(1,31),
        
    }

    return render(request, 'juz.html', context)


def juz_detail(request, juz_number):
    english_response = requests.get(f"http://api.alquran.cloud/v1/juz/{juz_number}/en.asad")
    english_data = english_response.json().get('data', {})

    arabic_response = requests.get(f"http://api.alquran.cloud/v1/juz/{juz_number}")
    arabic_data = arabic_response.json().get('data', {})

    
    ayahs=[]
    surahs ={}
    for arabic_ayah,english_ayah in zip(arabic_data.get('ayahs',[]), english_data.get('ayahs',[])):
        ayah_number = arabic_ayah['number']  
        audio_url = f"https://cdn.islamic.network/quran/audio/128/ar.alafasy/{ayah_number}.mp3"
        ayahs.append({
            'number':arabic_ayah['numberInSurah'],
            'arabic_text': arabic_ayah['text'],
            'english_text':english_ayah['text'],
            'audio_url': audio_url,

        })

    context = {
        'juz_number': juz_number,
        'ayahs': ayahs,
        'surahs':surahs
    }

    return render(request, 'juz_detail.html', context)



                                   
def wadu_view(request):
    wadu_list = wadu.objects.all()
    return render(request, 'wadu.html',{'wadu_list':wadu_list})

def Home(request):
    return render(request, 'home.html')