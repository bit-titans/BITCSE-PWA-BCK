from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.models import TT,Faculty,Slot,Subject
# Create your views here.
class getTT(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        result = {}
        pid = request.user.profile.pid
        if(len(pid)==10):
            semsec = self.request.query_params.get('semsec')
            days = ['MON','TUE','WED','THU','FRI','SAT']
            for day in days:
                subs = TT.objects.filter(semsec=semsec,day=day)
                subl = []
                for sub in subs:
                    subr = {
                        "subcode":sub.subject.subcode,
                        "subname":sub.subject.subname,
                        "faculty":sub.faculty.name,
                        "slot":sub.slot.time,
                        "room":sub.room
                    }
                    subl.append(subr)
                result[day]=subl
            return Response(result)
        else:
            fid = self.request.user.profile.pid
            days = ['MON','TUE','WED','THU','FRI','SAT']
            for day in days:
                subs = TT.objects.filter(faculty__fid=fid,day=day)
                subl = []
                for sub in subs:
                    subr = {
                        "subcode":sub.subject.subcode,
                        "subname":sub.subject.subname,
                        "faculty":sub.faculty.name,
                        "slot":sub.slot.time,
                        "room":sub.room
                    }
                    subl.append(subr)
                result[day]=subl
            return Response(result)
