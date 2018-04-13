from libvirt import libvirtError

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from servers.models import Compute
from instance.models import Instance
from vrtManager.instance import wvmInstances, wvmInstance
from decorators.decorator import ( patch_view_decorator, token_required )


@patch_view_decorator(token_required)
class ChangeStatus(generics.CreateAPIView):
    
    def post(self, request, host_id):
        data=request.DATA
        if "status" in data and data.get("status",""):
            vm_status = data.get("status","")
        else:
            return Response({"data":{}, "message": "Missing required parameter: status"}, status=status.HTTP_404_NOT_FOUND)

        if "name" in data and data.get("name",""):
            name = data.get("name","")
        else:
            return Response({"data":{}, "message": "Missing required parameter: name"}, status=status.HTTP_404_NOT_FOUND)

        try:
            compute = Compute.objects.get(id=host_id)
        except Compute.DoesNotExist as err:
            return Response({"data":{}, "message": err.message}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            conn = wvmInstances(compute.hostname, compute.login, compute.password, compute.type)
            get_instances = conn.get_instances()
        except libvirtError as err:
            return Response({"data":{}, "message": err.message}, status=status.HTTP_404_NOT_FOUND)

        try:
            Instance.objects.get(compute_id=host_id, name__in=get_instances)
        except Instance.DoesNotExist as err:
            return Response({"data":{}, "message": err.message}, status=status.HTTP_404_NOT_FOUND)

        if conn:
            try:
                if 'suspend' == vm_status:
                    conn.suspend(name)
                    return Response({"data":data, "message": "Instance suspend successfully!"}, status=status.HTTP_200_OK)
                elif 'resume' == vm_status:
                    conn.resume(name)
                    return Response({"data":data, "message": "Instance resume successfully!"}, status=status.HTTP_200_OK)

                conn.close()
            except libvirtError as err:
                return Response({"data":{}, "message": err.message}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"data":{}, "message": "Something went wrong with connection!"}, status=status.HTTP_404_NOT_FOUND)


@patch_view_decorator(token_required)
class VMSnapshots(generics.CreateAPIView):
    
    def post(self, request, host_id):
        data = request.DATA
        if "vm_name" in data and data.get("vm_name",""):
            vm_name = data.get("vm_name","")
        else:
            return Response({"data":{}, "message": "Missing required parameter: vm_name"}, status=status.HTTP_404_NOT_FOUND)

        if "snapshot_name" in data and data.get("snapshot_name",""):
            snapshot_name = data.get("snapshot_name","")
        else:
            return Response({"data":{}, "message": "Missing required parameter: snapshot_name"}, status=status.HTTP_404_NOT_FOUND)

        try:
            compute = Compute.objects.get(id=host_id)
        except Compute.DoesNotExist as err:
            return Response({"data":{}, "message": err.message}, status=status.HTTP_404_NOT_FOUND)

        try:
            instance = Instance.objects.get(compute_id=host_id, name=vm_name)
        except Instance.DoesNotExist as err:
            return Response({"data":{}, "message": err.message}, status=status.HTTP_404_NOT_FOUND)

        try:
            conn = wvmInstance(compute.hostname, compute.login, compute.password, compute.type, vm_name)
            conn.create_snapshot(snapshot_name)
            conn.close()
            return Response({"data":data, "message": "Snapshot created successfully!"}, status=status.HTTP_200_OK)
        except libvirtError as err:
           return Response({"data":{}, "message": "Something went wrong with connection!"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, host_id):
        data = request.DATA
        if "vm_name" in data and data.get("vm_name",""):
            vm_name = data.get("vm_name","")
        else:
            return Response({"data":{}, "message": "Missing required parameter: vm_name"}, status=status.HTTP_404_NOT_FOUND)

        if "snapshot_name" in data and data.get("snapshot_name",""):
            snapshot_name = data.get("snapshot_name","")
        else:
            return Response({"data":{}, "message": "Missing required parameter: snapshot_name"}, status=status.HTTP_404_NOT_FOUND)

        try:
            compute = Compute.objects.get(id=host_id)
        except Compute.DoesNotExist as err:
            return Response({"data":{}, "message": err.message}, status=status.HTTP_404_NOT_FOUND)

        try:
            instance = Instance.objects.get(compute_id=host_id, name=vm_name)
        except Instance.DoesNotExist as err:
            return Response({"data":{}, "message": err.message}, status=status.HTTP_404_NOT_FOUND)

        try:
            conn = wvmInstance(compute.hostname, compute.login, compute.password, compute.type, vm_name)
            conn.snapshot_delete(snapshot_name)
            conn.close()
            return Response({"data":data, "message": "Snapshot deleted successfully!"}, status=status.HTTP_200_OK)
        except libvirtError as err:
           return Response({"data":{}, "message": "Something went wrong with connection!"}, status=status.HTTP_404_NOT_FOUND)
