from API import SuperApiView
from .models import Enrollment
from .serializer import EnrollmentSerializer

class EnrollmentView(SuperApiView):
    model = Enrollment
    serializer_class = EnrollmentSerializer
    filter_fields = ["id"]