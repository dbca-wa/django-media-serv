from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.conf import settings
import mimetypes
import os

def getMediaFile(request):
    file_path = request.path.replace("../","")
    extension = request.path[-3:]
    file_name_path = settings.BASE_DIR+file_path
    if os.path.isfile(file_name_path) is True:
              the_file = open(file_name_path, 'rb')
              the_data = the_file.read()
              the_file.close()
              if extension == 'msg':
                  return HttpResponse(the_data, content_type="application/vnd.ms-outlook")
              if extension == 'eml':
                  return HttpResponse(the_data, content_type="application/vnd.ms-outlook")
              if extension == 'shp':
                  return HttpResponse(the_data, content_type="x-gis/x-shapefile")
              if extension == 'shx':
                  return HttpResponse(the_data, content_type="x-gis/x-shapefile")
              if extension == 'dbf':
                  return HttpResponse(the_data, content_type="text/plain")
              if extension == 'prj':
                  return HttpResponse(the_data, content_type="application/octet-stream")

              return HttpResponse(the_data, content_type=mimetypes.types_map['.'+str(extension)])
    else:
              return
#
