from django.shortcuts import render
from django.views import View


class EditSponsorInfoView(View):
    def get(self, request):
        return render(request, "edit_sponsor_info.html")

    def put(self, request):
        pass
