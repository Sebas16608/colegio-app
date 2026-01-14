from API import SuperApiView
from .models import Events
from .serializers import EventSerializer
# Create your views here.
class EventView(SuperApiView):
    model = Events
    serializer_class = EventSerializer
    filter_fields = ["title", "id"]