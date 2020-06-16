#! python
# -*- coding: utf-8 -*-

g_strtable = -1
language_code = __name__.split('.')[-1]

from ipodder.configuration import __version__
from gui.skin import PRODUCT_NAME

def add(label, txt):
    global g_strtable
    g_strtable.AddText(language_code, label, txt)

def AddStrings(strtable):
    global g_strtable
    g_strtable = strtable

    #############################################
    ## MV: 11:25 PM 2/20/2005
    ## READ THIS BEFORE EDITING/ADDING!!
    ## If you add new items, add them in the 'New strings' part.
    ## We can easily send them to the translators that way.
    #############################################

    ##_________________________________________________________
    ##
    ##     New strings
    ##_________________________________________________________

    add("str_goto_background_on_close_title", "设置关闭行为")
    add("str_goto_background_on_close_warn", \
        "当关闭主窗口时，%s可以在后台运行或退出，\n" \
        "你希望%s继续运行？" % (PRODUCT_NAME,PRODUCT_NAME))
    add("str_goto_background_on_close_pref", "当关闭主窗口时，继续后台运行")
    add("str_yes", "是")
    add("str_no", "否")
    add("str_dont_ask", "别再问我")
    add("str_ok", "OK")
    add("str_hide_window", "隐藏窗口")
    add("str_show_window", "显示窗口")

    add("str_catchup_pref", "跟进动作将会永久地跳过旧的曲目")
    add("str_set_catchup_title", "设置跟进行为")
    add("str_set_catchup_description", \
        "当使用跟进动作时，%s只是处理每个Feed中最新的一个Podcast\n" \
        "请选择%s应该怎样处理跳过的条目" % (PRODUCT_NAME,PRODUCT_NAME))
    add("str_skip_permanently", "永久跳过")
    add("str_skip_temporarily", "只是这次跳过")
    
    add("str_set_oneclick_handler", "设置单击处理器")
    add("str_set_oneclick_handler_warn",\
        "%s不是你当前的Podcast单击订阅处理器。\n" \
        "当点击单击订阅链接时，启动%s吗？" % (PRODUCT_NAME,PRODUCT_NAME))
    add("str_ensure_oneclick_handler", "总是使用%s进行单击订阅" % PRODUCT_NAME)
    
    add("str_txt_feedmanager", " 兼容的Feed管理器")
    add("str_feedmanager_btn_podnova", "www.PodNova.com - 搜索或浏览Podcast，单击订阅")

    add("str_open_downloads_folder", "打开下载目录")
    add("str_chkupdate_on_startup", "启动时检查新版本")
    add("str_bad_feedmanager_url", "请为Feed管理输入一个合法的URL")
    add("str_feed_manager", "Feed管理")
    add("str_feedmanager_enable", "同步我的订阅到一个远程服务")
    add("str_opml_url", "OPML URL")
    add("str_set_track_genre", "设置音轨流派为")
    add("str_auto_delete", "自动删除曲目，时间大于")
    add("str_days_old", "天的")
    
    add("str_show_notes", "显示注解")
    add("str_close", "关闭")

    add("str_critical_error_minspace_exceeded", \
        "跳过下载; 目前可用空间为%dMB, 小于 " \
        "设定的最小值 %dMB.  请释放硬盘空间 " \
        "用清除功能或在“参数选择”中调整“存储管理”选项")
    add("str_critical_error_unknown", "下载过程中出现严重的未知错误")
    
    add("str_error_checking_new_version", "很抱歉，检查新版本过程中出错，请稍后重试")
    add("str_hours", "小时")
    add("str_minutes", "分钟")

    # The next 4 are for the status bar updates during the initial scan.
    add("str_scanning", "扫描中")
    add("str_scanned", "扫描完成")
    add("str_feed", "Feed")
    add("str_feeds", "Feeds")
    
    add("str_downloading_new_episodes", "下载中的新曲目")
    add("str_sched_specific", "在指定时间检查")
    add("str_sched_reg", "在固定时间间隔内检查")
    add("str_repeat_every", "重复每隔")
    add("str_next_run_label", "下次运行")
    
    add("str_license", "This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the  License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of  merchantability or fitness for a particular purpose. \n\nSee the GNU General Public License for more details.")

    add("str_donate", "捐助%s" % PRODUCT_NAME)
    add("str_donate_expl", "It's important to keep community-owned %s applications online and keep this new way of consuming media free as in speech. Any amount of money will make the team happy and encourage them to work on new features and services!" % PRODUCT_NAME)
    add("str_donate_yes", "是的，马上带我去捐助页面！")
    add("str_donate_two_weeks", "我想再了解一下,两周后再显示")
    add("str_donate_already", "我已经捐助了，别再显示对话窗")
    add("str_donate_no", "我不想捐助，别再显示对话窗")
    add("str_donate_one_day", "现在不想捐助，1天后再次提醒我")
    add("str_donate_proceed", "继续")

    add("str_scheduler_dialog", "定时器")
    add("str_scheduler_tab", "设置")

    add("str_select_import_file", "选择导入文件")    
    add("str_add_feed_dialog", "添加新的Feed")
    add("str_edit_feed", "Feed属性")

    add("str_really_delete", "真的删除")

    add("str_license_caption", "版权协议")

    add("str_ep_downloaded", "已下载")
    add("str_ep_skipped_removed_other", "跳过/删除/其他的Feed")
    add("str_dl_state_to_download", "待下载")

    add("str_select_none_cleanup", "全不选")
    add("str_submit_lang", "提交一种语言")
    
    add("str_dltab_live", "活动的下载进程: ")
    add("str_dltab_ul_speed", "上传速度: ")
    add("str_dltab_dl_speed", "下载速度: ")


    ##_________________________________________________________
    ##
    ##     Main window (iPodder.xrc)
    ##_________________________________________________________


    
    ## File menu
    add("str_file", "文件")
    add("str_import_opml", "从OPML文件导入Feeds...")
    add("str_export_opml", "导出Feeds到OPML文件...")
    add("str_preferences_menubar", "个人设定...")
    add("str_close_window", "关闭窗口")
    add("str_quit", "退出")

    add("str_edit", "编辑")
    add("str_select_all", "全选")

    add("str_tools", "工具")
    add("str_check_all", "全部检查")
    add("str_catch_up", "跟进")
    add("str_check_selected", "检查选中的")
    add("str_add_feed", "添加新的Feed...")
    add("str_remove_selected", "删除Feed")
    add("str_feed_properties", "Feed属性...")
    add("str_scheduler_menubar", "定时器...")
    
    add("str_select_language", "选择语言")

    ## these are also used for the tabs
    add("str_view", "查看")
    add("str_downloads", "下载")
    add("str_subscriptions", "订阅")
    add("str_podcast_directory", "Podcast目录")
    add("str_cleanup", "清理")

    add("str_help", "帮助")
    add("str_online_help", "在线帮助")
    add("str_faq", "常见问题解答")
    add("str_check_for_update", "检查更新...")
    add("str_report_a_problem", "问题报告")
    add("str_goto_website", "访问网站")
    add("str_make_donation", "捐助")
    add("str_menu_license", "版权协议...")
    add("str_about", "关于...")


    ## Downloadstab Toolbar
    add("str_remove_selected_items", "删除选中的条目")
    add("str_cancel_selected_download", "取消下载（选中的条目）")
    add("str_pause_selected", "暂停下载（选中的条目）")

    ## Downloadstab States (in columns)
    ## Enclosure states. Use str_dl_state_ prefix to avoid collisions with
    ## other strings, e.g. str_downloading above which isn't capitalized.
    add("str_dl_state_new", "新建")
    add("str_dl_state_queued", "在队列中")
    add("str_dl_state_downloading", "下载中")
    add("str_dl_state_downloaded", "已下载")
    add("str_dl_state_cancelled", "已取消")
    add("str_dl_state_finished", "已完成")
    add("str_dl_state_partial", "部分下载")
    add("str_dl_state_clearing", "正在清理")


    ## Subscriptionstab Toolbar
    add("str_check_for_new_podcasts", "全部检查 - 检查新的Podcast")
    add("str_catch_up_mode", "跟进 - 仅下载最新的Podcast")

    add("str_add_new_feed", "添加Feed");
    add("str_remove_selected_feed", "删除选中的Feed")
    add("str_properties", "属性")
    add("str_check_selected_feed", "检查选中的Feed")

    add("str_scheduler_on", "定时器 - 打开")
    add("str_scheduler_off", "定时器 - 关闭")        

    ## Subscriptionstab Scheduler information
    add("str_next_run:", "下次运行")

    ## Subscriptionstab episode frame
    add("str_downloading_episode_info", "下载中的曲目信息...")
    add("str_no_episodes_found", "没有找到曲目。")


    ## Directorytab Toolbar
    add("str_refresh", "刷新")
    add("str_open_all_folders", "打开所有目录")
    add("str_close_all_folders", "关闭所有目录")
    add("str_add", "添加")

    ## Directorytab Other items
    add("str_directory_description", "在目录中点击一个Feed，或在上面的空白处输入或粘贴，然后点击添加")




    ## Cleanuptab items
    add("str_select_a_feed", "选择一个Feed")
    add("str_refresh_cleanup", "刷新")
    
    add("str_look_in", "查找曲目在...")        
    add("str_player_library", "播放器媒体库")
    add("str_downloads_folder", "下载目录")
    add("str_delete_library_entries", "删除媒体库中的条目")
    add("str_delete_files", "删除文件")
    add("str_select_all_cleanup", "全选")
    add("str_delete", "删除")



    ## Logtab items
    add("str_log", "日志")
    add("str_clear", "清理")


    ## Columns (in downloads- and subscriptionstab)
    add("str_lst_name", "名称")
    add("str_lst_date", "日期")        
    add("str_lst_progress", "进度")
    add("str_lst_state", "状态")
    add("str_lst_mb", "MB")
    add("str_lst_location", "位置")
    add("str_lst_episode", "曲目")
    add("str_lst_playlist", "播放列表")

    ## Feed subscription states -- see ipodder/feeds.py SUB_STATES variable
    add("str_subscribed", "已订阅")
    add("str_disabled", "已失效")
    add("str_newly-subscribed", "最近订阅")
    add("str_unsubscribed", "已退订")
    add("str_preview", "预览")
    add("str_force", "强制")
    





    ##_________________________________________________________
    ##
    ##   Dialog Windows
    ##_________________________________________________________



    ## OPML Import Dialog
    #--- Select import file

    ## OPML Export Dialog
    add("str_choose_name_export_file", "为导出文件选择一个名字")
    add("str_subs_exported", "所有的订阅已经导出")
    
    ## Preferences Dialog
    add("str_preferences", "配置")
    
    add("str_save", "保存")
    add("str_cancel", "取消")
    
    # General
    add("str_general", "通用")
    add("str_gen_options_expl", "为%s程序设置通用选项" % PRODUCT_NAME)
    add("str_hide_on_startup", "启动后只在系统托盘中显示%s" % PRODUCT_NAME)

    add("str_run_check_startup", "启动时自动检查新Podcast")
    add("str_play_after_download", "所有曲目下载完就播放")
    add("str_location_and_storage", "位置和存储管理")
    add("str_stop_downloading", "停止下载，当硬盘空间剩余容量最小到")
    add("str_bad_megabyte_limit_1", "请输入整数")
    add("str_bad_megabyte_limit_2", "请重试")

    add("str_download_folder", "下载Podcast到此目录")
    add("str_browse", "浏览")
    add("str_bad_directory_pref_1", "找不到指定的目录")
    add("str_bad_directory_pref_2", "请先创建此目录然后重试")

    
    # Threading
    add("str_threads", "线程")
    add("str_multiple_download", "多线程下载设置")
    add("str_max_feedscans", "为搜索Feed，每个会话最大线程")
    add("str_max_downloads", "每个会话最大下载线程")
   
    # Network settings
    add("str_networking", "网络设置")
    add("str_coralize_urls", "Coralize URLs (实验的)")
    add("str_proxy_server", "用代理服务器")
    add("str_proxy_address", "地址")
    add("str_proxy_port", "端口")
    add("str_proxy_username", "用户名")
    add("str_proxy_password", "密码")
    add("str_bad_proxy_pref", "你选择使用代理服务器，但没有提供其地址和端口，请重新设置")

    # Player
    add("str_player", "播放器")
    add("str_choose_a_player", "选择一个播放器")
    add("str_no_player", "没有播放器")
    
    # Advanced
    add("str_advanced", "高级")
    add("str_options_power_users", "这些选项适用于高级用户")
    add("str_run_command_download", "在完成每个下载后运行这个命令")
    add("str_rcmd_full_path", "%f = 下载文件的全路径")
    add("str_rcmd_podcast_name", "%n = Podcast名称")
    add("str_other_advanced_options", "其他高级选项")
    add("str_show_log", "在程序中显示日志标签")



    ## Feed Dialog (add/properties)
    add("str_title", "标题")
    add("str_url", "URL")
    add("str_goto_subs", "到订阅标签中查看这个Feed对应的曲目")
    add("str_feed_save", "保存")
    add("str_feed_cancel", "取消")




    ## Scheduler Dialog
    add("str_enable_scheduler", "打开定时器")
    add("str_sched_select_type", "定时器运行方式:")
    add("str_check_at_specific_times", "在指定时间检查")
    add("str_check_at_regular_intervals", "在固定时间间隔检查")
    add("str_repeat_every:", "重复每隔")
    add("str_latest_run", "最后一次运行")
    add("str_next_run", "下次运行")
    add("str_not_yet", "还没有")
    #--- Cancel
    add("str_save_and_close", "保存并关闭")
    #--- Save

    add("str_time_error", "时间格式不正确，正确的时间格式应该像这样: 10:02am, 16:43")


    ## Donations Dialog
    #--- Donate to iPodder
    #--- It's important to keep non-commercial iPodder applications online and keep this new way of consuming media free. Any amount of money will make the team happy and encourage them to work on new features!
    #--- Yes, take me to the donations page now!
    #--- I still have to check it a bit more, show this again in two weeks
    #--- I allready made a donation, don't show this dialog again
    #--- No, I don't want to donate, never show this dialog again
    #--- Not now, notify me again in 1 day
    #--- OK




    ## About Dialog
    #--- Version:
    #--- Programming: Erik de Jonge, Andrew Grumet, Garth Kidd, Perica Zivkovic\nDesign: Martijn Venrooy\nContent strategist: Mark Alexander Posth\nConcept: Adam Curry, Dave Winer\nThanks to all translators for their commitments!\n\nBased on Feedparser and BitTorrent technology.\nThis program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the  License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of  merchantability or fitness for a particular purpose. \n\nSee the GNU General Public License for more details.




    ## Statusbar items
    add("str_check_for_new_podcast_button", "点击绿色按钮，检查新的Podcast")
    add("str_last_check", "最后检查完成于")
    add("str_of", "的")
    add("str_item", "条目")
    add("str_items", "条目")
    add("str_downloading", "下载中")
    add("str_downloaded", "下载完成")
    add("str_enclosure", "enclosure")
    add("str_enclosures", "enclosures")
    add("str_fetched", "抓取完成")
    add("str_loading_mediaplayer", "正在引导Media Player...")
    add("str_loaded_mediaplayer", "Media Player引导完成...")        
    add("str_initialized", "%s 准备完成" % PRODUCT_NAME)




    ## Other application strings
    add("str_ipodder_title", PRODUCT_NAME + " - Podcast 接收机 v" + __version__)
    add("str_localization_restart", "%s的语言切换需要重新启动，点击确定重新启动，点击取消继续" % PRODUCT_NAME)
    add("str_really_quit", "一个下载进程在运行，真的退出？");
    add("str_double_check", "已经有一个下载进程在运行");
    
    # check for update
    add("str_new_version_ipodder", "已经有新版本的%s了，去下载页面" % PRODUCT_NAME)
    add("str_no_new_version_ipodder", "这个版本的%s已经是最新的" % PRODUCT_NAME)
    add("str_other_copy_running", "另一个%s正在运行中，你可以选择打开它或等它完成或中止它" % PRODUCT_NAME)

    # Windows taskbar right-click menu
    add("str_check_now", "立刻检查")        
    add("str_open_ipodder", "打开%s" % PRODUCT_NAME)
    #--- Downloading
    add("str_scanning_feeds", "扫描的Feed")

    # Feed right-click menu
    add("str_remove", "删除")        
    add("str_open_in_browser", "在浏览器中打开")
    
    

    # Downloads right-click menu
    add("str_play_episode", "用Media Player播放曲目")
    add("str_clear_selected", "清理选中的条目")
    



