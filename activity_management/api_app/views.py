from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from activity_app.models import Task,ActivityLog,Remainder
from api_app.serializer import TaskSerializer,ActivitylogSerializer,RemainderSerializer
# Create your views here.

class TaskApiView(APIView):
    def get(self,request,*args, **kwargs):
        
        try:
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks,many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self,request,*args, **kwargs):

        try:
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

                message={
                    'status': 'success',
                    'status_code': status.HTTP_201_CREATED,
                }
                return Response(data=message,status=status.HTTP_201_CREATED)
            
            else:
                return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response(data={'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
    def put(self,request,id,*args, **kwargs):
        try:
            task = Task.objects.get(id=id)
            serailizer = TaskSerializer(instance=task,data=request.data,partial=True)

            if serailizer.is_valid():
                serailizer.save()
                message = {
                    'status': 'success',
                    'status_code': status.HTTP_200_OK
                }
                return Response(data=message,status=status.HTTP_200_OK)
            else:
                return Response(data=serailizer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data={'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self,request,id,*args, **kwargs):
        try:
            task = Task.objects.get(id=id)
            task.delete()
            message = {
                'status': 'success',
                'status_code': status.HTTP_200_OK
            }
            return Response(data=message,status=status.HTTP_200_OK)
    
        except Exception as e:
            return Response(data={'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class ActivitylogApiView(APIView):
    def get(self,*args, **kwargs):
        try:
            activity = ActivityLog.objects.all()
            serializer = ActivitylogSerializer(activity,many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self,request,*args, **kwargs):
        try:
            serializer = ActivitylogSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = {
                    'status': 'success',
                    'status_code': status.HTTP_201_CREATED
                }
                return Response(data=message,status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data={'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self,request,id,*args, **kwargs):
        try:
            activity = ActivityLog.objects.get(id=id)
            serializer = ActivitylogSerializer(instance=activity,data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = {
                    'status': 'success',
                    'status_code': status.HTTP_200_OK
                }
                return Response(data=message,status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data={'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self,request,id,*args, **kwargs):
        try:
            task = ActivityLog.objects.get(id=id)
            task.delete()
            message = {
                'status': 'success',
                'status_code': status.HTTP_200_OK
            }
            return Response(data=message,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        

class RemainderApiView(APIView):
    def get(self,request,*args, **kwargs):
        try:
            remainders = Remainder.objects.all()
            serializer = RemainderSerializer(remainders,many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self,request,*args, **kwargs):
        try:
            serializer = RemainderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

                message = {
                    'status': 'success',
                    'status_code': status.HTTP_201_CREATED,
                }

                return Response(data=message,status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data={'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
    def put(self,request,id,*args, **kwargs):
        try:
            remainder = Remainder.objects.get(id=id)
            serializer = RemainderSerializer(instance=remainder,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                message = {
                    'status': 'success',
                    'status_code': status.HTTP_200_OK
                }
                return Response(data=message,status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data={'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self,request,id,*args, **kwargs):
        try:
            remainder = Remainder.objects.get(id=id)
            remainder.delete()
            message = {
                'status': 'success',
                'status_code': status.HTTP_200_OK
            }
            return Response(data=message,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)