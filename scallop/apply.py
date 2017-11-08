# Created by yang
from django.shortcuts import render,redirect,HttpResponse
from . import models


def activity_apply(request):
    user_id=request.session["user_info"].get("nid")#通过session中已经登录的user信息获取到user_id
    User_obj=models.User.objects.filter(pk=user_id).first()#查找到user对象
    user_obj=models.UserInfo.objects.filter(user_id=user_id).first()#通过user对象查找到userinfo对象。
    company_list=models.Company.objects.all()#获取所有的公司列表
    context={
        "user_obj":user_obj,
        "company_list":company_list,
    }
    if request.method=="POST":
        """
        利用form表单POST请求提交过来的表格数据写入到ActivityApply表。
        """
        # print("____|",request.POST)
        form=request.POST.get("form")
        product_name=request.POST.get("product_name")
        product_version=request.POST.get("product_version")
        advocate_platform=request.POST.get("advocate_platform")
        advocate_des=request.POST.get("advocate_des")
        apply_cause=request.POST.get("apply_cause")#列表多选菜单。修改为单选框。
        if request.POST.get("apply_cause")==4:
            apply_cause=request.POST.get("apply_other")
            # print("其他____",apply_cause)
        anticipate=request.POST.get("anticipate")
        fg=request.POST.get("fg")
        before_result=request.POST.get("before_result")
        bg=request.POST.get("bg")
        payer=request.POST.get("payer")
        budget=request.POST.get("budget")
        exigence=request.POST.get("exigence")
        write_model={
            "depart":user_obj.department,
            "user":User_obj,
            "form":form,
            "payer_id":payer,
            "budget":budget,
            "exigence":exigence,
            "apply_type_id":6,
            "product_name":product_name,
            "product_version":product_version,
            "advocate_platform":advocate_platform,
            "advocate_des":advocate_des,
            "apply_cause":apply_cause,
            "anticipate":anticipate,
            "first_generalize":fg,
            "before_result":before_result,
            "buy_goods":bg,
            "attachment":None#上传文件我暂时先弄成None做测试的
        }
        models.ActivityApply.objects.create(**write_model)
        return HttpResponse("入库成功")
    return render(request,"apply/activity.html",context)


def apply(request,apply_name):
    """处理订单填写"""
    print(apply_name)
    handel_apply = {
        "activityapply": activity_apply,
    }

    if apply_name not in handel_apply:
        return HttpResponse("url有误,请检查您要申请的订单类型是否正确")

    return handel_apply["activityapply"](request)