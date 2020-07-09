import xadmin
from xadmin import views

from home.models import Banner


class BaseSetting(object):
    """x admin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings(object):
    """x admin的全局配置"""
    site_title = "晚间码农"  # 设置站点标题
    site_footer = "熬夜喝茶还是喝咖啡"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠


xadmin.site.register(views.CommAdminView, GlobalSettings)


# # 将banner注册到后台  列表显示的字段
class BannerInfo(object):
    list_display = ["title", "orders", "is_show"]


xadmin.site.register(Banner, BannerInfo)


# class NavInfo(object):
#     list_display = ["title", "orders", "is_show"]
#
#
# xadmin.site.register(Nav, NavInfo)
