from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView
from .models import Expediente, Documento
from .forms import ExpedienteForm, DocumentoForm

class ExpedienteCreateView(CreateView):
    model = Expediente
    form_class = ExpedienteForm
    template_name = "expedientes/expediente_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["documento_form"] = DocumentoForm(self.request.POST, self.request.FILES)
        else:
            context["documento_form"] = DocumentoForm()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        documento_form = context["documento_form"]

        if documento_form.is_valid():
            self.object = form.save()
            for archivo in self.request.FILES.getlist("archivo"):
                Documento.objects.create(expediente=self.object, archivo=archivo)
            return redirect("expediente_detail", pk=self.object.pk)
        else:
            return self.form_invalid(form)


class ExpedienteDetailView(DetailView):
    model = Expediente
    template_name = "expedientes/expediente_detail.html"


class ExpedienteListView(ListView):
    model = Expediente
    template_name = "expedientes/expediente_list.html"
