from django.contrib.auth.models import User
from rest_framework import serializers
from .models import  Booking, MenuItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ "id", "url", "username", "email", "password"]
        extra_kwargs = {
            "password": {"write_only": True, "required": True},
        }

    def create(self, validated_data):
        # Use create_user so password is hashed
        return User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            password=validated_data["password"],
        )

    # In Django REST Framework (DRF), this line is the "magic" that allows you to extend the default 
    # update behavior without having to manually rewrite the logic for saving every single field.
    # Think of it as saying: "Go ahead and do the standard update work, and then give me the 
    # finished object back so I can do something extra with it."
    # Breaking Down the Components
    #     super(): This refers to the parent class (usually serializers.ModelSerializer). It tells 
    #           Python to look for the update() method already built into DRF.
    #     .update(instance, validated_data): This calls that built-in method.
    #         instance: The existing object currently in the database (the one you want to change).
    #         validated_data: The new data that has already passed through your validation rules 
    #           (the "clean" data from the user's request).
    #     instance = : We capture the result of the update. The built-in method saves the changes to 
    #                   the database and returns the updated object.
    # Summary:
    # validated_data is a dictionary of "clean" input from the user.
    # .pop("password")	pulls the password out and deletes it from the dictionary.
    # None	prevents an error if the password field is missing.
    # The Result is validated_data is now safe to save to the database.
    def update(self, instance, validated_data):
        # Allow updating password safely
        # validated_data only has things like 'username' and 'email'
        # Pull password out of the pile of data aka object
        password = validated_data.pop("password", None)

        #What .pop() does
        # The .pop(key, default) method does two things at once:
        #     Extracts: It finds the value for "password" and assigns it to the password variable.
        #     Removes: It deletes the "password" key from the validated_data dictionary entirely.
        # validated_data is the new info sent by the user (JSON).
        # instance is the old info sitting in your Database.
        instance = super().update(instance, validated_data)

        if password:
            # hash and save the password
            instance.set_password(password)
            instance.save(update_fields=["password"])

        return instance


# class MenuSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Menu
#         # The 'id' is included because it's the primary key created by Django
#         fields = ['id', 'title', 'price', 'inventory']
        
class MenuItemSerializer(serializers.ModelSerializer):
    # price cannot be less than $2
    # This validation technique only works in DRF, not Admin Panel
    # Best to do validation in Models.py to apply to both
    # price = serializers.DecimalField(
    #         max_digits=6,
    #         decimal_places=2,
    #         min_value=2.00,
    #         max_value=50.00)
    # # Inventory must be greater than 0
    # inventory = serializers.IntegerField(min_value=1)
    class Meta:
        model  = MenuItem
        fields = ['id', 'title', 'price', 'inventory']
        
class BookingSerializer(serializers.ModelSerializer):
    # Guests must be between 1 and 9
    # number_of_guests = serializers.IntegerField(
    #     min_value=1,
    #     max_value=9
    #)
    class Meta:
        model = Booking
        # The 'id' is included because it's the primary key created by Django
        fields = '__all__'
        

# class BookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Booking
#         fields = '__all__'
#         extra_kwargs = {
#             'booking_date': {'format': '%Y-%m-%dT%H:%M:%S'} # ISO format with time
#         }