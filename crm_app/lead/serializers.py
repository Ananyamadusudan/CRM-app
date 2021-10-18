from rest_framework import serializers
from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        read_only_fields = (
            'created_by',
            'created_at',
            'updated_at'
        )
        fields = (
            'id',
            'company',
            'contact_person',
            'email',
            'phone_number',
            'website',
            'confidence',
            'estimated_value',
            'status',
            'priority'

        )

