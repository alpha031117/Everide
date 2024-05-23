from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MyRideSerializer
from .models import Ride
from user.models import MyUser, Driver
from carbonFootprint.models import CarbonFootprint

# API for getting all rides
@api_view(['GET'])
def get_ride(request):
    ride = Ride.objects.all()
    serializer = MyRideSerializer(ride, many=True)
    return Response(serializer.data)

# API for getting rides of a specific user
@api_view(['GET'])
def get_user_ride(request, pk):
    try:
        user_obj = MyUser.objects.get(id=pk)
        print(user_obj)
        rides = Ride.objects.filter(user=user_obj)
        serializer = MyRideSerializer(rides, many=True)
        return Response(serializer.data)
    except MyUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

# API for creating a ride
@api_view(['POST'])
def createRide(request):
    data = request.data
    user = get_object_or_404(MyUser, id=data['user'])
    driver = get_object_or_404(Driver, id=data['driver'])
    shared_with_friends_ids = data.get('shared_with_friends', [])

    ride = Ride.objects.create(
        user=user,
        driver=driver,
        pickup_location=data['pickup_location'],
        destination_location=data['destination_location'],  # Corrected field name
        distance=data['distance'],
        type_of_ride=data['type_of_ride'],
        # Note: total_received will be automatically calculated in the model's save method
    )
    ride.shared_with_friends.set(shared_with_friends_ids)

    # Call the function to update the carbon footprint
    update_carbon_footprint(user, ride.distance)

    serializer = MyRideSerializer(ride, many=False)
    return Response(serializer.data)

# API for updating a ride
@api_view(['PUT', 'PATCH'])
def updateRide(request, pk):
    try:
        ride = Ride.objects.get(pk=pk)
    except Ride.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = MyRideSerializer(ride, data=request.data, partial=True)  # Pass request data to serializer, allowing partial updates
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API for marking a ride as complete
@api_view(['PUT', 'PATCH'])
def completeRide(request, pk):
    ride = get_object_or_404(Ride, id=pk)
    
    if request.method == 'PUT':
        # For PUT requests, mark the ride as completed
        ride.completed = True
        ride.save()

    elif request.method == 'PATCH':
        # For PATCH requests, update only the 'completed' field
        ride.completed = True

    user = get_object_or_404(MyUser, id=ride.user.id)
    cfp = get_object_or_404(CarbonFootprint, user=user)
    distance = ride.distance

    # Apply tier-based multiplier to footprint
    if cfp.tier == 'Silver':
        carbonfootprint_earned = distance * 170 * 1.2   # Multiply by 1.2 for Silver tier
    elif cfp.tier == 'Gold':
        carbonfootprint_earned = distance * 170 * 1.4   # Multiply by 1.4 for Gold tier
    elif cfp.tier == 'Bronze':
        carbonfootprint_earned = distance * 170 * 1.1   # Multiply by 1.1 for Bronze tier
    else:
        carbonfootprint_earned = distance * 170 

    ride.carbonfootprint_earned = carbonfootprint_earned
    ride.save()

    serializer = MyRideSerializer(ride, many=False)
    
    # Return a success response with appropriate status code
    return Response(serializer.data, status=status.HTTP_200_OK)

# API for cancelling a ride
@api_view(['DELETE'])
def cancelRide(request, pk):
    ride = Ride.objects.get(id=pk)
    ride.delete()

    return Response('Ride is cancelled.')

# API for getting booking history of a user
@api_view(['GET'])
def get_booking_history(request, user_id):
    # Filter BookingHistory objects for the given user ID
    user = get_object_or_404(MyUser, id=user_id)
    history = Ride.objects.filter(user=user)
    serializer = MyRideSerializer(history, many=True)
    return Response(serializer.data)

def update_carbon_footprint(user, distance):
    cfp, created = CarbonFootprint.objects.get_or_create(user=user)

    cfp.total_distance += distance
    # Apply tier-based multiplier to footprint
    if cfp.tier == 'Silver':
        cfp.footprint += distance * 170 * 1.2   # Multiply by 1.2 for Silver tier
    elif cfp.tier == 'Gold':
        cfp.footprint += distance * 170 * 1.4   # Multiply by 1.4 for Gold tier
    elif cfp.tier == 'Bronze':
        cfp.footprint += distance * 170 * 1.1   # Multiply by 1.1 for Bronze tier
    else:
        cfp.footprint += distance * 170 
    
    cfp.save()
