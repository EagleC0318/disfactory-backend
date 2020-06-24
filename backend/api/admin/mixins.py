import csv

from django.http import HttpResponse


def _modify(field_name):
    if field_name == 'get_name':
        return 'name'
    return field_name

class ExportCsvMixin:

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = '輸出成 csv 檔'


class RestoreMixin:

    def restore(self, request, queryset):
        queryset.undelete()

    restore.short_description = '復原'


class ExportLabelMixin:
    def export_labels_as_docx(self, request, queryset):
        return

    export_labels_as_docx.short_description = '下載標籤及交寄執據'
