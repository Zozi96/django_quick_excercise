from datetime import date

from rest_framework import serializers

from pets.models import Pet


class PetSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = "__all__"

    def age(self):
        """ Return the current age of the pet in years. """
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age
