from django.conf.urls.defaults import patterns, url, include
from django.views.generic.simple import direct_to_template

from .users.decorators import login_required
direct_to_template_login = login_required(direct_to_template)

urlpatterns = patterns(
    "",
    url("^$", "tcmui.products.views.product_list", name="products"),
    url("^account/", include("tcmui.users.urls")),
    url("^product/(?P<product_id>\d+)/environment/$",
        "tcmui.environments.views.set_environment",
        name="environment"),
    url("^product/(?P<product_id>\d+)/cycles/$",
        "tcmui.testexecution.views.cycles",
        name="cycles"),

    url("^product/1/cycles/1/$", direct_to_template_login, {"template": "test/run.html"}, name="run"),
    url("^manage/testcase/add/$", direct_to_template_login, {"template": "test/add_case.html"}, name="add"),
)
