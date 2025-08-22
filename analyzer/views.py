from django.shortcuts import render
from .forms import ProfileForm
from . import nlp_utils
from django.conf import settings

def analyze_view(request):
    result = {}
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            for section in ['headline', 'skills', 'about']:
                text = form.cleaned_data[section]
                corrected, grammar_issues = nlp_utils.analyze_grammar(text)
                sentiment, vader = nlp_utils.analyze_sentiment(text)
                try:
                    
                    suggestion = nlp_utils.get_openai_suggestion(text, settings.OPENAI_API_KEY)
                except Exception as e:
                    suggestion = f"GPT suggestion disabled ({str(e)})"
                result[section] = {
                    "original": text,
                    "corrected": corrected,
                    "grammar_issues": grammar_issues,
                    "sentiment": sentiment,
                    "vader": vader,
                    "suggestion": suggestion
                }
    else:
        form = ProfileForm()
    return render(request, "analyzer/home.html", {"form": form, "result": result})
