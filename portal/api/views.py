from django.shortcuts import render

from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.http import JsonResponse

from main.models import Regulations, Role

@method_decorator(csrf_exempt, name='dispatch')
class VioceParser(View):
    def get(self, request):
        return render(request, 'api/voice.html')

    def post(self, request):
        import speech_recognition as sr

        # get voice from file
        try:
            sample_audio = sr.AudioFile(request.FILES.get('voice'))
            recognizer = sr.Recognizer()

            # opem voice file
            with sample_audio as audio_file:
                recognizer.adjust_for_ambient_noise(audio_file)
                audio_content = recognizer.record(audio_file)

            return JsonResponse({
                'error': False,
                'text': recognizer.recognize_google(audio_content, language='ru-RU')
            })
        except:
            return JsonResponse({
                'error': True
            }) 

@method_decorator(csrf_exempt, name='dispatch')
class GetRegulation(View):
    def post(self, request):
        title = request.POST.get('title')

        if not title:
            return JsonResponse({'success': False})

        regulation = Regulations.objects.filter(title__icontains=title).first()
        if not regulation:
            return JsonResponse({'success': False})
        
        persons = []
        roles = regulation.roles.all()

        for role in roles:
            for person in role.profiles.all():
                persons.append(person.id)

        return JsonResponse({
            'success': True, 
            'regulation': {
                'title': regulation.title,
                'hours': regulation.hours,
                'persons': persons
            }
        })