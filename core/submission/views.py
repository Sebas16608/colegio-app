from API import SuperApiView
from .serializer import SubmissionSerializer
from .models import Submission
# Create your views here.
class SubmissionView(SuperApiView):
    model = Submission
    serializer_class = SubmissionSerializer
    filter_fields = ["id"]
