from rest_framework import serializers 
from tutorials.models import Tutorial
from rest_framework.fields import ListField
from ast import literal_eval


# class StringArrayField(ListField):
#     def to_representation(self, obj):
#         # str -> list
#         return literal_eval(obj)
#
#     def to_internal_value(self, data):
#         # list -> str
#         data = str(data)
#         return data
#

class TutorialSerializer(serializers.ModelSerializer):
    # attendancelist = StringArrayField()

    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published',
                  'liveDate',
                  'attendancelist')


class AttendanceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('attendancelist',)
