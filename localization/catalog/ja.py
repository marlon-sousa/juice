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
    ## We can easily throw them to the translators that way.
    #############################################



    ##_________________________________________________________
    ##
    ##     New strings
    ##_________________________________________________________


    add("str_error_checking_new_version", "We're sorry, but there was an error checking for a new version.  Please try again later.")
    add("str_hours", "hours")
    add("str_minutes", "minutes")

    # The next 4 are for the status bar updates during the initial scan.
    add("str_scanning", "Scanning")
    add("str_scanned", "Scanned")
    add("str_feed", "feed")
    add("str_feeds", "feeds")
    
    add("str_downloading_new_episodes", "Downloading new episodes")
    add("str_sched_specific", "Check at specific times")
    add("str_sched_reg", "Check at regular intervals")
    add("str_repeat_every", "Repeat every")
    add("str_next_run_label", "Next run:")
    
    add("str_license", "This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the  License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of  merchantability or fitness for a particular purpose. \n\nSee the GNU General Public License for more details.")

    add("str_donate", "Donate to %s" % PRODUCT_NAME)
    add("str_donate_expl", "It's important to keep community-owned %s applications online and keep this new way of consuming media free as in speech. Any amount of money will make the team happy and encourage them to work on new features and services!" % PRODUCT_NAME)
    add("str_donate_yes", "Yes, take me to the donations page now!")
    add("str_donate_two_weeks", "I still have to check it a bit more, show this again in two weeks")
    add("str_donate_already", "I allready made a donation, don't show this dialog again")
    add("str_donate_no", "No, I don't want to donate, never show this dialog again")
    add("str_donate_one_day", "Not now, notify me again in 1 day")
    add("str_donate_proceed", "Proceed")

    add("str_scheduler_dialog", "Scheduler")
    add("str_scheduler_tab", "Settings")

    add("str_select_import_file", "Select import file")    
    add("str_add_feed_dialog", "Add a Feed")
    add("str_edit_feed", "Feed properties")

    add("str_really_delete", "Really delete")

    add("str_license_caption", "License")

    add("str_ep_downloaded", "Downloaded")
    add("str_ep_skipped_removed_other", "Skipped/Removed/OtherFeed")
    add("str_dl_state_to_download", "To Download")

    add("str_select_none_cleanup", "Select none")
    add("str_submit_lang", "Submit a language")
    
    add("str_dltab_live", "Live downloads: ")
    add("str_dltab_ul_speed", "Upload speed: ")
    add("str_dltab_dl_speed", "Download speed: ")


    ##_________________________________________________________
    ##
    ##     Main window (iPodder.xrc)
    ##_________________________________________________________


    
    ## File menu
    add("str_file", "ファイル")
    add("str_import_opml", "opml からのフィードをインポート")
    add("str_export_opml", "opml としてフィードをエキスポート")
    add("str_preferences", "個人設定")
    add("str_close_window", "ウィンドウを閉じる")
    add("str_quit", "終了")

    add("str_edit", "編集")
    add("str_select_all", "すべてを選択")

    add("str_tools", "ツール")
    add("str_check_all", "すべての新着を確認")
    add("str_catch_up", "新着のポッドキャストをダウンロード")
    add("str_check_selected", "選択項目の新着を確認")
    add("str_add_feed", "フィードを追加する")
    add("str_remove_selected", "フィードを削除する")
    add("str_feed_properties", "フィードのプロパティ")
    add("str_scheduler", "スケジューラ")

    add("str_select_language", "言語")

    ## these are also used for the tabs
    add("str_view", "表示")
    add("str_downloads", "ダウンロード")
    add("str_subscriptions", "購読")
    add("str_podcast_directory", "ポッドキャストディレクトリ")
    add("str_cleanup", "クリーンアップ")

    add("str_help", "ヘルプ")
    add("str_online_help", "オンラインヘルプ")
    add("str_faq", "FAQ")
    add("str_check_for_update", "更新を確認")
    add("str_report_a_problem", "問題を報告する")
    add("str_goto_website", "ホームページに行く")
    add("str_make_donation", "寄付する")
    add("str_about", "%s について" % PRODUCT_NAME)


    ## Downloadstab Toolbar
    add("str_remove_selected_items", "選択された項目を削除")
    add("str_cancel_selected_download", "選択されたダウンロードをキャンセル")
    add("str_pause_selected", "選択されたダウンロードを一時停止")

    ## Downloadstab States (in columns)
    ## Enclosure states. Use str_dl_state_ prefix to avoid collisions with
    ## other strings, e.g. str_downloading above which isn't capitalized.
    add("str_dl_state_new", "新規")
    add("str_dl_state_queued", "順番待ち")
    add("str_dl_state_downloading","ダウンロード中")
    add("str_dl_state_downloaded","ダウンロード完了")
    add("str_dl_state_cancelled", "キャンセル")
    add("str_dl_state_finished", "終了")
    add("str_dl_state_partial", "部分的にダウンロード終了")

    add("str_dl_state_clearing", "クリア中")


    ## Subscriptionstab Toolbar
    add("str_check_for_new_podcasts", "新しいポッドキャストを確認")
    add("str_catch_up_mode", "最後に購読したポッドキャストを最新に")

    add("str_add_new_feed", "新しいフィードを追加");
    add("str_remove_selected_feed", "選択されたフィードを削除")
    add("str_properties", "プロパティ")
    add("str_check_selected_feed", "選択されたフィードを確認")

    add("str_scheduler_on", "スケジューラ - オン")
    add("str_scheduler_off", "スケジューラ - オフ")

    ## Subscriptionstab Scheduler information
    add("str_next_run:", "次の実行:")

    ## Subscriptionstab episode frame
    add("str_downloading_episode_info", "ダウンロード中のエピソードの情報は...")
    add("str_no_episodes_found", "エピソードが見つかりませんでした。")


    ## Directorytab Toolbar
    add("str_refresh", "更新")
    add("str_open_all_folders", "すべてのフォルダを開く")
    add("str_close_all_folders", "すべてのフォルダを閉じる")
    add("str_add", "追加")

    ## Directorytab Other items
    add("str_directory_description", "ツリー中のフィードをクリックするか、上のテキストボックスに入力して、追加をクリックしてください。")




    ## Cleanuptab items
    add("str_select_a_feed", "フィードを選択")
    add("str_refresh_cleanup", "更新")
    
    add("str_look_in", "エピソードを探す場所は ... ")        
    add("str_player_library", "プレイヤライブラリ")
    add("str_downloads_folder", "ダウンロードフォルダ")
    add("str_delete_library_entries", "ライブラリの項目を削除")
    add("str_delete_files", "ファイルを削除")
    add("str_select_all_cleanup", "すべてを選択")
    add("str_delete", "削除")




    ## Logtab items
    add("str_log", "ログ")
    add("str_clear", "クリア")


    ## Columns (in downloads- and subscriptionstab)
    add("str_lst_name", "名前")
    add("str_lst_date", "日付")        
    add("str_lst_progress", "進捗")
    add("str_lst_state", "状態")
    add("str_lst_mb", "MB")
    add("str_lst_location", "場所")
    add("str_lst_episode", "エピソード")
    add("str_lst_playlist", "プレイリスト")

    ## Feed subscription states -- see ipodder/feeds.py SUB_STATES variable
    add("str_subscribed", "購読済み")
    add("str_disabled", "無効化")
    add("str_newly-subscribed", "最近の購読")
    add("str_unsubscribed", "未購読")
    add("str_preview", "プレビュー")
    add("str_force", "強制")
    





    ##_________________________________________________________
    ##
    ##   Dialog Windows
    ##_________________________________________________________



    ## OPML Import Dialog


    ## OPML Export Dialog
    add("str_choose_name_export_file", "エキスポートするファイルの名前を選択")
    add("str_subs_exported", "エキスポートする購読")
    
    ## Preferences Dialog
    add("str_save", "保存")
    add("str_cancel", "キャンセル")
    
    # General
    add("str_general", "全般")
    add("str_gen_options_expl", "%s の全般的なオプションを設定" % PRODUCT_NAME)
    add("str_hide_on_startup", "スタートアップ時に %s をシステムトレイに置く" % PRODUCT_NAME)

    add("str_run_check_startup", "スタートアップ時に新着のポッドキャストを確認")
    add("str_play_after_download", "ダウンロード完了後すぐに再生")
    add("str_location_and_storage", "ロケーションと場所の管理")
    add("str_stop_downloading", "ダウンロードを続けてもいいハードディスク残量は最低")

    add("str_bad_megabyte_limit_1", "メガバイトの制限が 整数 ではありませんでした。")
    add("str_bad_megabyte_limit_2", "整数で指定してください。")

    add("str_download_folder", "このフォルダにポッドキャストをダウンロードする")
    add("str_browse", "ブラウズ")

    add("str_bad_directory_pref_1", "入力したディレクトリが見つかりませんでした。")
    add("str_bad_directory_pref_2", "ディレクトリを作ってから、もう一度行ってください。")

    
    # Threading
    add("str_threads", "スレッディング")
    add("str_multiple_download", "複数ダウンロードの設定")
    add("str_max_feedscans", "セッションごとのフィードスキャニングの最大スレッド数")
    add("str_max_downloads", "セッションごとの最大ダウンロード数")
   
    # Network settings
    add("str_networking", "ネットワーク設定")
    add("str_coralize_urls", "URL を coralize (experimental)")
    add("str_proxy_server", "プロキシサーバの使用")
    add("str_proxy_address", "プロキシのアドレス")
    add("str_proxy_port", "ポート")
    add("str_proxy_username", "ユーザ名")
    add("str_proxy_password", "パスワード")
    add("str_bad_proxy_pref", "プロキシサポートを有効にした場合は、プロキシホストとポートを設定してください。")

    # Player
    add("str_player", "プレイヤ")
    add("str_choose_a_player", "プレイヤを選択してください")

    add("str_no_player", "プレイヤがありません。")
    
    # Advanced
    add("str_advanced", "高度な機能")
    add("str_options_power_users", "これらのオプションはパワーユーザ用です。")
    add("str_run_command_download", "ダウンロードする度にこのコマンドを実行")
    add("str_rcmd_full_path", "%f = ダウンロードされたファイルのフルパス")
    add("str_rcmd_podcast_name", "%n = ポッドキャストの名前")
    add("str_other_advanced_options", "他の高度なオプション")
    add("str_show_log", "ログのタブを表示")



    ## Feed Dialog (add/properties)
    add("str_title", "タイトル")
    add("str_url", "URL")
    add("str_goto_subs", "このフィードのエピソードを表示するには、購読タブを開いてください。")
    add("str_feed_save", "保存")
    add("str_feed_cancel", "キャンセル")




    ## Scheduler Dialog
    add("str_enable_scheduler", "スケジューラを有効に")
    add("str_sched_select_type", "下のラジオボタンを選択することで、新着の確認を指定した時刻または間隔で行えます。")
    add("str_check_at_specific_times", "これらの時刻に新着の確認を行います。")
    add("str_check_at_regular_intervals", "この間隔で新着の確認を行います")
    add("str_repeat_every:", "次の回数繰り返します : ")
    add("str_latest_run", "最後に実行したのは :")
    add("str_next_run", "次の実行は :")
    add("str_not_yet", "まだ ")
    #--- Cancel
    add("str_save_and_close", "保存して終了")
    #--- Save

    add("str_time_error","時刻の形式が誤っています。次の形式で指定してください : 10:02am, 16:43.")



    ## Statusbar items
    add("str_check_for_new_podcast_button", "Check for new podcasts by pressing the button green check button")
    add("str_last_check", "最後に新着の確認をしたのは、")
    add("str_of", "の")
    add("str_item", "項目")
    add("str_items", "項目")
    add("str_downloading", "ダウンロード中")
    add("str_downloaded", "ダウンロード完了")
    add("str_enclosure", "enclosure")
    add("str_enclosures", "enclosures")
    add("str_fetched", "取得済み")
    add("str_loading_mediaplayer", "メディアプレイヤをロード中")
    add("str_loaded_mediaplayer", "メディアプレーヤのロード完了")        
    add("str_initialized", "%s は準備ができました" % PRODUCT_NAME)




    ## Other application strings
    add("str_ipodder_title", "%s - Podcast receiver v" % PRODUCT_NAME + __version__)
    add("str_localization_restart", "%s の言語設定の変更には再起動が必要です。%s を終了してもよいときは、Ok をクリックしてください。続けるには Cancel をクリックしてください。" % (PRODUCT_NAME,PRODUCT_NAME))
    add("str_really_quit", "ダウンロード中です。本当に %s を終了しますか？" % PRODUCT_NAME);
    add("str_double_check", "ダウンロードが始まっているようです。終了しますか？");
    
    # check for update
    add("str_new_version_ipodder", "%s の新しいバージョンが利用可能です。ダウンロードサイトに行くには Ok をクリックしてください。" % PRODUCT_NAME)
    add("str_no_new_version_ipodder", "今お使いの %s は最新です。" % PRODUCT_NAME)
    add("str_other_copy_running", "%s が別に実行中です。そちらを終了もしくは強制終了させてください" % PRODUCT_NAME)

    # Windows taskbar right-click menu
    add("str_check_now", "今すぐ新着の確認をする")
    add("str_open_ipodder", "%s を開く" % PRODUCT_NAME)

    #--- Downloading

    add("str_scanning_feeds", "フィードのスキャン中")

    # Feed right-click menu
    add("str_remove", "削除")        
    add("str_open_in_browser", "ブラウザーの中で開く")

    # Downloads right-click menu
    add("str_play_episode", "エピソードの再生")
    add("str_clear_selected", "選択された項目のクリア")
    
