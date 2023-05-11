from rest_framework import serializers
from branch.models import Branch


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['name', 'geo']

    def validate_geo(self, value):
        if 'москва' not in value.lower():
            raise  serializers.ValidationError('Расположение филиала не в г. Москва')
        return value


    def validate_name(self, value):
        if 'fitness' not in value.lower():
            raise serializers.ValidationError('В названии не указано слово fitness')
        return value
