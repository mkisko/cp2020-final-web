from django.shortcuts import render

from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.http import JsonResponse

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
