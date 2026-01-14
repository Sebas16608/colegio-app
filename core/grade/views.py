from API import SuperApiView
from .models import Grade
from .serializer import GradeSerializer
# Create your views here.
class GradeView(SuperApiView):
    model = Grade
    serializer_class = GradeSerializer
    filter_fields = ["grade", "id"]