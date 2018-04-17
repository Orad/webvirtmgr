from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from servers.models import Compute


class Connections(generics.ListAPIView):
    
    def get(self, request):
        computes = Compute.objects.all()
        data = []
        for compute in computes:
            if compute.type == 1 :
                url = 'qemu+tcp://%s/system' % compute.hostname
            if compute.type == 2 :
                url = 'qemu+ssh://%s@%s/system' % (compute.login, compute.hostname)
            if compute.type == 3 :
                url = 'qemu+tls://%s@%s/system' % (compute.login, compute.hostname)
            if compute.type == 4 :
                url = 'qemu:///system'
            append = True
            for element in data:
                if element['url'] == url:
                    element['count'] += 1
                    append = False
            if append:
                data.append({ "url": url, "type": compute.type,"count":1})
                
        return Response(data)