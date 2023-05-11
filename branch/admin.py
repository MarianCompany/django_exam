from django.contrib import admin
from branch.models import Branch
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ExportActionMixin

# Register your models here.


class MyBranch(Branch):
    class Meta:
        proxy = True


class BranchAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name', 'geo')


admin.site.register(Branch, SimpleHistoryAdmin)
admin.site.register(MyBranch, BranchAdmin)
