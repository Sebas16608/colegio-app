from API import SuperApiView
from .serializers import SubjectSerializer
from .models import Subject
# Create your views here.
class SubjectView(SuperApiView):
    model = Subject
    serializer_class = SubjectSerializer
    filter_fields = ["name", "id"]
