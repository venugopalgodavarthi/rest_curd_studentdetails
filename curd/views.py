
from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from curd.models import student
from curd.serializers import studentserializers
from rest_framework.decorators import api_view
    

@api_view(['GET', 'POST','PUT', 'DELETE'])
def student_list(request):
    stu=None
    if request.method == 'GET':
        stu = student.objects.all()
        name = request.query_params.get('first_name', None)
        if name is not None:
            stu = stu.filter(first_name__icontains=name)
        
        curd_serializer = studentserializers(stu, many=True)
        return JsonResponse(curd_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        curd_data = JSONParser().parse(request)
        curd_serializer = studentserializers(data=curd_data)
        if curd_serializer.is_valid():
            curd_serializer.save()
            return JsonResponse(curd_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(curd_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = student.objects.all().delete()
        return JsonResponse({'message': '{} curd were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET','PUT', 'DELETE'])
def student_detail(request,pk):
    try: 
        stu = student.objects.get(pk=pk) 
    except student.DoesNotExist: 
        return JsonResponse({'message': 'The record does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        curd_serializer = studentserializers(stu) 
        return JsonResponse(curd_serializer.data) 
    
    if request.method == 'PUT': 
        curd_data = JSONParser().parse(request) 
        curd_serializer = studentserializers(stu, data=curd_data) 
        if curd_serializer.is_valid(): 
            curd_serializer.save() 
            return JsonResponse(curd_serializer.data) 
        return JsonResponse(curd_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        studentd.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
             
@api_view(['GET'])
def studentd(request,pk):
    stu = student.objects.filter(name=pk)
    if request.method == 'GET': 
        curd_serializer = studentserializers(stu, many=True)
        return JsonResponse(curd_serializer.data, safe=False)
