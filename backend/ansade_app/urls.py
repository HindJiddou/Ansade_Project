from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategorieViewSet, ThemeViewSet, TableauViewSet, DonneesViewSet, ImportExcelView,TableauDetailStructureView,TableauFiltreView,TableauFiltresOptionsView, TableauFiltreStructureView,TableauAnalyseAPIView,CarteParTableauAPIView,ListeSourcesAPIView, TableauxParSourceAPIView,RechercheGlobaleAPIView

router = DefaultRouter()
router.register(r'categories', CategorieViewSet)
router.register(r'themes', ThemeViewSet)
router.register(r'tableaux', TableauViewSet)
router.register(r'donnees', DonneesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('import-excel/', ImportExcelView.as_view(), name='import-excel'),
    path('tableaux/<int:tableau_id>/structure/', TableauDetailStructureView.as_view(), name='tableau-structure'),
    path('tableaux/<int:tableau_id>/filtres-options/', TableauFiltresOptionsView.as_view()),
    path('tableaux/<int:tableau_id>/filtrer/', TableauFiltreView.as_view(), name='tableau-filtrer'),
    path('tableaux/<int:tableau_id>/filtrer-structure/', TableauFiltreStructureView.as_view(), name='filtrer-structure'),
    path('tableaux/<int:pk>/analyse/', TableauAnalyseAPIView.as_view(), name='tableau-analyse'),
    path("tableaux/<int:tableau_id>/carte/", CarteParTableauAPIView.as_view(), name="carte-par-annee"),
    path('sources/', ListeSourcesAPIView.as_view(), name='liste-sources'),
    path('sources/<path:source>/tableaux/', TableauxParSourceAPIView.as_view(), name='tableaux-par-source'),
    path("recherche-globale/", RechercheGlobaleAPIView.as_view(), name="recherche-globale"),




]
