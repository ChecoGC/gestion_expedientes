from django import forms
from .models import Expediente, Documento

class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = ["nombre", "descripcion"]


class DocumentoForm(forms.ModelForm):
    archivo = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": True}))

    class Meta:
        model = Documento
        fields = ["archivo"]

    def clean_archivo(self):
        archivos = self.files.getlist("archivo")
        for archivo in archivos:
            if not archivo.name.lower().endswith((".png", ".jpg", ".jpeg", ".pdf")):
                raise forms.ValidationError("Solo se permiten archivos de tipo imagen o PDF.")
        return archivos
