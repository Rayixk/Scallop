from django.conf.urls import url
from django.shortcuts import render, HttpResponse, redirect
from arya.service import sites
from . import models


class UserInfoConfig(sites.AryaConfig):
    list_display = ["user", "name", "department"]


sites.site.register(models.UserInfo, UserInfoConfig)


class DepartmentConfig(sites.AryaConfig):
    list_display = ["name", ]


sites.site.register(models.Department, DepartmentConfig)


class CompanyConfig(sites.AryaConfig):
    list_display = ["name", "bank", "card_num"]


sites.site.register(models.Company, CompanyConfig)


class RecordConfig(sites.AryaConfig):
    list_display = ["apply_for", "status", "operate", "operate_time"]


sites.site.register(models.Record, RecordConfig)


class ActivityApplyConfig(sites.AryaConfig):
    list_display = ["apply_id", "depart", "user"]


sites.site.register(models.ActivityApply, ActivityApplyConfig)


class ApplyTypeConfig(sites.AryaConfig):
    list_display = ["name", ]


sites.site.register(models.ApplyType, ApplyTypeConfig)


class SecondTypeConfig(sites.AryaConfig):
    list_display = ["name","url","base_type"]

sites.site.register(models.SecondType, SecondTypeConfig)



# -----------申请管理---------
class BaseApplyConfig(sites.AryaConfig):

    def put_apply(self,request, *args, **kwargs):
        """填写申请-主页面"""
        apply_types = models.ApplyType.objects.all()
        context = {
            "apply_types":apply_types,
        }
        return render(request,"put_apply.html",context)


    def extra_urls(self):
        app_model_name = self.model_class._meta.app_label, self.model_class._meta.model_name

        patterns = [
            url(r'^put_apply/$', self.wrapper(self.put_apply), name="%s_%s_put_apply" % app_model_name),
        ]
        return patterns


sites.site.register(models.BaseApply, BaseApplyConfig)

