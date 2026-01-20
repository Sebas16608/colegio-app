from API import SuperApiView
from .serializer import PaymentSerializer
from .models import Payment
# Create your views here.
class PaymentView(SuperApiView):
    model = Payment
    serializer_class = Payment
    filter_fields = ["student", "month", "status", "validated_by"]


