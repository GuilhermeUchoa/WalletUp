
from . serializers import PortfolioSerializer, AtivosSerializer
from . b3FileUpload import adicionarAtivosDaCarteiraB3ParaPortfolioAppUsuario
from . models import PortfolioModels, AtivosModels
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
import warnings


warnings.simplefilter("ignore")



class AtivosViewSet(viewsets.ModelViewSet):

    queryset = AtivosModels.objects.all()
    serializer_class = AtivosSerializer


class PortfolioViewSet(viewsets.ModelViewSet):

    serializer_class = PortfolioSerializer

    # não utilizo o queryset pois quero que o usuario veja apenas a sua carteira
    def get_queryset(self):
        # Somente retorna frases do usuário autenticado
        return PortfolioModels.objects.filter(usuario=self.request.user.id)

    # Filtro = filter_backends, search = search_fields
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["status"]
    search_fields = ["status", "tipo"]
    ordering_fields = "__all__"


@api_view(['POST'])
def upload_file(request):

    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        name = request.FILES['file'].name

        if name[0:7] == 'posicao':
            adicionarAtivosDaCarteiraB3ParaPortfolioAppUsuario(
                request, uploaded_file)

        # Faça algo com o arquivo, como salvá-lo no servidor
        # Exemplo: uploaded_file.save('/path/to/save/location')
        return JsonResponse({'message': 'File uploaded successfully'})
    else:
        return JsonResponse({'error': 'No file found in request'}, status=400)


