from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, GroupSerializer, SocialWorkerSerializer, EnrollmentSerializer, \
    NonCashBenefitsSerializer, IncomeSerializer, HomelessSerializer, AppointmentSerializer
from .models import SocialWorker, Homeless, Enrollment, NonCashBenefits, IncomeAndSources, Appointments


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class SocialWorkerRegistration(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HomelessDetails(viewsets.ModelViewSet):
    queryset = Homeless.objects.all()
    serializer_class = HomelessSerializer


class SocialWorkerDetails(viewsets.ModelViewSet):
    queryset = SocialWorker.objects.all()
    serializer_class = SocialWorkerSerializer


class IncomeDetails(viewsets.ModelViewSet):
    queryset = IncomeAndSources.objects.all()
    serializer_class = IncomeSerializer


class NonCashDetails(viewsets.ModelViewSet):
    queryset = NonCashBenefits.objects.all()
    serializer_class = NonCashBenefitsSerializer


class HomelessViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Homeless.objects.filter()
        serializer = HomelessSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Homeless.objects.filter(pk=pk)
        enroll = get_object_or_404(queryset, pk=pk)
        serializer = HomelessSerializer(enroll)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        homeless = request.data
        serializer = HomelessSerializer(data=homeless)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class EnrollmentViewSet(viewsets.ViewSet):

    def list(self, request, homeless_pk=None):
        queryset = Enrollment.objects.filter(PersonalId_id=homeless_pk)
        serializer = EnrollmentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, homeless_pk=None):
        queryset = Enrollment.objects.filter(pk=pk, PersonalId_id=homeless_pk)
        enroll = get_object_or_404(queryset, pk=pk)
        serializer = EnrollmentSerializer(enroll)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, homeless_pk=None):
        enroll = request.data
        enroll['PersonalId'] = homeless_pk
        serializer = EnrollmentSerializer(data=enroll)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None, homeless_pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class AppointmentViewSet(viewsets.ViewSet):

    def list(self, request, homeless_pk=None):
        queryset = Appointments.objects.filter(personalId_id=homeless_pk)
        serializer = AppointmentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, homeless_pk=None):
        queryset = Appointments.objects.filter(pk=pk, personalId_id=homeless_pk)
        enroll = get_object_or_404(queryset, pk=pk)
        serializer = AppointmentSerializer(enroll)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, homeless_pk=None):
        enroll = request.data
        enroll['personalId'] = homeless_pk
        serializer = AppointmentSerializer(data=enroll)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None, homeless_pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
