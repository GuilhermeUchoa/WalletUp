from django.db import models
from django.db.models import Sum, F
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete, post_init
from django.dispatch import receiver
import yfinance as yf

class AtivosModels(models.Model):  # Ativos BASE

    TIPO = (
        ("Acoes", "Acoes"),
        ("Brazilian Depositary Receipts", "Brazilian Depositary Receipts"),
        ("Fundo de Investimento", "Fundo de Investimento"),
        ("Tesouro Direto", "Tesouro Direto"),
        ("Outros", "Outros")
    )

    ativoPrincipal = models.CharField(
        max_length=50, blank=False, null=False, primary_key=True)
    cotacao = models.FloatField(blank=False, null=False, default=0)
    tipo = models.CharField(blank=False, null=False, choices=TIPO, max_length=250, default="Outros")
    dy = models.FloatField(blank=True, null=True)
    atualizacao = models.DateTimeField(auto_now=True)
    
    # A task ja esta salvando toda vez que ela roda não é necessaria essa função, somente quando adicionar novo ativo, entao preciso pensar em algo
    # def save(self, *args, **kwargs):
    #     if(self.tipo != "Tesouro Direto"):
    #         self.cotacao = round(yf.download(f"{self.ativoPrincipal}.SA").iloc[-1]['Close'],2)
    #     return super().save()

    def __str__(self):
        return f'{self.ativoPrincipal}'


class PortfolioModels(models.Model):

    StatusToBuy = (
        ("comprar", "comprar"),
        ("aguardar", "aguardar"),
        ("vender", "vender")
    )

    TIPO = (
        ("Acoes", "Acoes"),
        ("Brazilian Depositary Receipts", "Brazilian Depositary Receipts"),
        ("Fundo de Investimento", "Fundo de Investimento"),
        ("Tesouro Direto", "Tesouro Direto"),
        ("Outros", "Outros"),
    )

    # Usuario
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    # Dados iniciais
    ativo = models.ForeignKey(AtivosModels, on_delete=models.CASCADE) # Ativo aqui só receebe o nome do ativo pois __str__ de  Ativomodels é o nome do ativo
    cotacao = models.FloatField(blank=True, null=True, default=0, editable=False)
    quantidade = models.FloatField(blank=True, null=True, default=0)
    

    # Porcentagens
    porcentagem = models.FloatField(blank=True, null=True)
    variacaoAnual = models.FloatField(blank=True, null=True, editable=False)
    dy = models.FloatField(blank=True, null=True, editable=False)
    
    # metas
    meta = models.FloatField(blank=True, null=True)
    metaDividendYield = models.FloatField(blank=True, null=True)

    # Classificação
    status = models.CharField(
        max_length=250, choices=StatusToBuy, default="comprar")
    tipo = models.CharField(max_length=250, choices=TIPO, editable=False)
    aporte = models.IntegerField(blank=True, null=True, default=0)

    # Valuation
    precoMedio = models.FloatField(blank=True, null=True)
    valuationDy = models.FloatField(blank=True, null=True)  # preco maximo a 6%
    valuationDFC = models.FloatField(blank=True, null=True)

    # Anotacoes
    comentarios = models.TextField(blank=True, null=True)
    
    # Valuation qualitativo
    question0 = models.FloatField(default=0)
    question1 = models.FloatField(default=0)
    question2 = models.FloatField(default=0)
    question3 = models.FloatField(default=0)
    question4 = models.FloatField(default=0)
    question5 = models.FloatField(default=0)
    question6 = models.FloatField(default=0)
    question7 = models.FloatField(default=0)
    question8 = models.FloatField(default=0)
    question9 = models.FloatField(default=0)
    question10 = models.FloatField(default=0)
    question11 = models.FloatField(default=0)

    # Formulario
    scoreQualitativo = models.FloatField(blank=True, null=True, default=0)
    
    # Calculos
    def valuationDy(self):
        pass

    # Cria o score qualitativo
    def calculoScoreQualitativo(self):
        soma = (self.question0 + self.question1 + self.question2 + self.question3 + self.question4 + self.question5 + self.question6 +
                self.question7 + self.question8 + self.question9 + self.question10 + self.question11)

        return float(soma)


    class Meta:
        # Restrições: o par (usuario, ativo) deve ser único
        constraints = [
            models.UniqueConstraint(
                fields=['usuario', 'ativo'], name='unique_portfolio_per_user')
        ]

    def save(self, *args, **kwargs):
        self.scoreQualitativo = self.calculoScoreQualitativo()  # Antes de salvar, calcula o score qualitativo
        self.cotacao = self.ativo.cotacao # ativo é um objeto do tipo AtivosModels
        self.tipo = self.ativo.tipo
        self.dy = self.ativo.dy
        return super().save()
    
    
    def __str__(self):
        return f'{self.usuario.username} - {self.ativo}'




# Signals para atualizar o valor da cotacao
@receiver(post_save, sender=AtivosModels)
def atualizar_portfolioModels_com_ativosModels(sender, instance, **kwargs):
    """Atualiza as cotações nos portfolios dos usuários quando a cotação do ativo é alterada."""
    # Obtém os portfolios que têm esse ativo
    portfolios = PortfolioModels.objects.filter(ativo=instance)
    for portfolio in portfolios:
        # Atualiza a cotação do ativo para os portfolios relacionados
        portfolio.cotacao = instance.cotacao
        portfolio.tipo = instance.tipo
        portfolio.save()


@receiver(post_delete, sender=AtivosModels)
def limpar_portfolios_ativos_deletados(sender, instance, **kwargs):
    """Limpa os portfolios que estão relacionados a um ativo excluído."""
    PortfolioModels.objects.filter(ativo=instance).delete()