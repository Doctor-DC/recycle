import coreapi
import coreschema
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from rest_framework.schemas import AutoSchema
from rest_framework.utils import json
from rest_framework.views import APIView
# from json_schema_generator import SchemaGenerator
# from asyn.tasks import task_response
from resouces.connect.conn_server import conn_server
from resouces.connect.decorators import token_certify_decorator

conn = None

class instances(APIView):
    """
    get:
        获取回收站instances列表
    """
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field(name='Authorization',required='True',location='header',description='Authentication header',type='string'),
            coreapi.Field(name='DcCode',required='True',location='header',description='dccode header')
        ]

    )
    @method_decorator(token_certify_decorator)
    def get(self,request,conn):
        ins = conn_server(request,conn)
        # ins = conn.describe_instances(status=["terminated"],owner="usr-zHHGDyko")
        return JsonResponse(ins,safe=False)

class ceaseinstances(APIView):
    """
    put:
    彻底删除instances
    """
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field (name='Authorization', required='True', location='header',description='Authentication header', type='string'),
            coreapi.Field (name='DcCode', required='True', location='header', description='dccode header'),
            coreapi.Field (name='instance', required=True, location="query", description='主机id')
        ]

    )
    @method_decorator(token_certify_decorator)
    def put(self,request,conn):
        instances = request.GET.get('instances')
        # print(type(instances))
        instances = instances.split()  #str 分割成列表 如hello world -》  ["hello","world"]
        # print(type(instances))
        res = conn.cease_instances(instances)
        return JsonResponse(res)

class imageslist(APIView):
    """
    get:
        获取回收站镜像
    """
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field (name='Authorization', required='True', location='header',
                           description='Authentication header', type='string'),
            coreapi.Field (name='DcCode', required='True', location='header', description='dccode header'),

        ]
    )
    @method_decorator(token_certify_decorator)
    def get(self,request,conn):
        images = conn.describe_images(status='deleted'),
        return JsonResponse(images,safe=False)

class imagescease(APIView):
    """
    put:
        彻底删除镜像
    """
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field (name='Authorization', required='True', location='header',
                           description='Authentication header', type='string'),
            coreapi.Field (name='DcCode', required='True', location='header', description='dccode header'),
            coreapi.Field(name='images',required=True,location='query',description='镜像id',)
        ]
    )

    @method_decorator(token_certify_decorator)
    def delete(self,request,conn):
        imagesid = request.GET.get('images')
        imagesid = imagesid.split()
        res = conn.cease_images(imagesid)
        return JsonResponse(res)



class volumeslist(APIView):
    """
    get:
        获取回收站硬盘
    """
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field (name='Authorization', required='True', location='header',
                           description='Authentication header', type='string'),
            coreapi.Field (name='DcCode', required='True', location='header', description='dccode header'),

        ]
    )
    @method_decorator(token_certify_decorator)
    def get(self,request,conn):
        volumes = conn.describe_volumes(status=["deleted"]),
        return JsonResponse(volumes,safe=False)

class volumescease(APIView):
    """
    put:
        彻底删除硬盘
    """
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field (name='Authorization', required='True', location='header',
                           description='Authentication header', type='string'),
            coreapi.Field (name='DcCode', required='True', location='header', description='dccode header'),
            coreapi.Field(name='volumes',required=True,location='query',description='硬盘id',)
        ]
    )

    @method_decorator(token_certify_decorator)
    def delete(self,request,conn):
        volumes = request.GET.get('volumes')
        volumes = volumes.split()
        res = conn.cease_volumes(volumes)
        return JsonResponse(res)