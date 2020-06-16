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

    ## REMOVED strings
    ##
    ## add("str_ensure_oneclick_handler", u"Always use %s for one-click subscription" % PRODUCT_NAME)
    ## add("str_set_oneclick_handler", u"Set one-click handler")
    ## add("str_set_oneclick_handler_warn",\
    ##    u"%s is not currently your one-click subscription handler for podcasts. \n" \
    ##    u"Should we set %s to launch from one-click subscription links?" % (PRODUCT_NAME,PRODUCT_NAME))

    
    ##_________________________________________________________
    ##
    ##     New strings
    ##_________________________________________________________

    add("str_copy_location", "העתק מיקום")
    add("str_set_file_types", "קבע סוגי קבצים")
    add("str_set_file_types_warn", \
        "%s אינו מוגדר כרגע לעבודה עם מספר סוגי קבצים. \n" \
        "האם ברצונך לקבוע אותם כעת?" % PRODUCT_NAME)
    add("str_subscription_options", "אפשרויות מינוי בלחיצת כפתור:")
    add("str_enforce_settings", "הכרח מאפיינים אלו בזמן הטעינה")
    add("str_file_types", "סוגי קבצים")
    add("str_play_button_enqueues", "כפתור הניגון מוסיף את הפרקים הנבחרים לתור")
    add("str_authentication", "אימות")
    add("str_dl_state_skipped", "דולג")
    add("str_dl_state_removed", "הוסר")
    
    add("str_username", "שם משתמש")
    add("str_password", "סיסמא")
    add("str_missing_proxy_password", "נקבע שם משתמש ל proxy ללא סיסמא. \n" \
        "אנא מחק את שם המשתמש או הססמא.")

    add("str_goto_background_on_close_title", "קבע התנהגות בסגירה")
    add("str_goto_background_on_close_warn", \
        "%s יכול להמשיך לרוץ ברקע לאחר סגירת \n" \
        "החלון הראשי.  לחילופין %s יכול לצאת.  האם ברצונך ש \n" \
        "ימשיך לרוץ?" % (PRODUCT_NAME,PRODUCT_NAME))
    add("str_goto_background_on_close_pref", "המשך ריצה ברקע לאחר סגירת החלון הראשי")
    add("str_yes", "כן")
    add("str_no", "לא")
    add("str_dont_ask", "אל תשאל אותי פעם נוספת")
    add("str_ok", "אישור")
    add("str_hide_window", "הסתר חלון")
    add("str_hide_tray_icon", "הסתר צלמית של ה Tray")
    add("str_show_window", "הצג חלון")

    add("str_catchup_pref", "השלמת חוסרים מדלגת על פרקים ישנים באופן קבוע")
    add("str_set_catchup_title", "הגדר התנהגות 'השלמת חוסרים'")
    add("str_set_catchup_description", \
        "בזמן השלמת חוסרים, %s ידלג על כולם מלבד הפרק האחרון \n" \
        "בכל feed.  אנא הגדר כיצד על %s להתייחס לפרקים שדולגו \n" % (PRODUCT_NAME,PRODUCT_NAME))
    add("str_skip_permanently", "דלג באופן קבוע")
    add("str_skip_temporarily", "דלג בפעם זו בלבד")
    
    add("str_txt_feedmanager", "מנהלי feeds תואמים:")
    add("str_feedmanager_btn_podnova", "www.PodNova.com - חפש או סרוק פודקאסטים, מינוי בלחיצת כפתור")

    add("str_open_downloads_folder", "פתח תיקיית הורדות")
    add("str_chkupdate_on_startup", "בדוק לגרסאות חדשות של התוכנה בזמן העליה.")
    add("str_bad_feedmanager_url", "אנא הכנס URL חוקי למנהל ה feeds.")
    add("str_feed_manager", "Feeds מנהל")
    add("str_feedmanager_enable", "סנכרן את המינויים שלי עם שירות מרוחק")
    add("str_opml_url", "OPML URL")
    add("str_set_track_genre", "Set track genre to")
    add("str_auto_delete", "מחק בצורה אוטומאטית קבצים בני למעלה מ")
    add("str_days_old", "ימים")
    
    add("str_show_notes", "רשימות התוכנית")
    add("str_close", "סגור")
    
    add("str_critical_error_minspace_exceeded", \
        "הורדה דולגה; פנוי %dMB פחות " \
        "מהמינימום %dMB.  אנא נקה מקום בכונן " \
        "שלך באמצעות חלון הניקוי או עדכן את גבולות" \
        "האחסון ב'הגדרות'")
    add("str_critical_error_unknown", "חלה בעיה כלשהי בזמן ההורדה.")
    
    add("str_error_checking_new_version", "חלה תקלה בזמן הבדיקה לגרסה חדשה של התוכנה, אנא נסה שנית מאוחר יותר")
    add("str_hours", "שעות")
    add("str_minutes", "דקות")

    # The next 4 are for the status bar updates during the initial scan.
    add("str_scanning", "סורק")
    add("str_scanned", "סרוק")
    add("str_feed", "feed")
    add("str_feeds", "feeds")
    
    add("str_downloading_new_episodes", "מוריד פרקים חדשים")
    add("str_sched_specific", "בדוק בזמנים קבועים")
    add("str_sched_reg", "בדוק במרווחי זמן קבועים")
    add("str_repeat_every", "חזור בכל")
    add("str_next_run_label", "ריצה הבאה:")
    
    add("str_license", "זוהי תוכנה חופשית; אתה יכול להפיץ אותה מחדש ו/או לשנות אותה תחת התנאים של רשיון GNU General Public License כפי שמפורסם על-ידי ה Free Software Foundation; לפי גרסה 2 או כל גרסה מתקדמת יותר, כרצונך. תוכנה זו מופצת מתוך תקווה שהיא תהיה שימושית, אך ללא אחריות כלשהי; אפילו ללא האפשרות המרומזת של תאימות למסחר או לשימוש כלשהו. \n\nראה GNU General Public License לפרטים נוספים.")

    add("str_donate", "תרום ל %s" % PRODUCT_NAME)
    add("str_donate_expl", "ישנה חשיבות גדולה לשמירה של תוכנות מסוג זה חופשיות, ככלי תומך לחופש הביטוי. כל סכום של כסף יתרום למוטיבציה של המפתחים להוסיף שירותים ותכונות נוספים לתוכנה!")
    add("str_donate_yes", "קח אותי לדף התרומות עכשיו!")
    add("str_donate_two_weeks", "אני צריך לבדוק זאת, הצג לי חלון זה בעוד שבועיים")
    add("str_donate_already", "כבר תרמתי, אל תציג בקשה זו פעם נוספת")
    add("str_donate_no", "אינני מעוניין לתרום, אל תציג בקשה זו פעם נוספת")
    add("str_donate_one_day", "לא עכשיו, בקש מחר פעם נוספת")
    add("str_donate_proceed", "המשך")

    add("str_scheduler_dialog", "מתאם זמנים")
    add("str_scheduler_tab", "הגדרות")

    add("str_select_import_file", "בחר קובץ לייבוא")    
    add("str_add_feed_dialog", "הוסף Feed")
    add("str_edit_feed", "תכונות Feed")

    add("str_really_delete", "מחק באמת")

    add("str_license_caption", "רשיון")

    add("str_ep_downloaded", "ירד")
    add("str_ep_skipped_removed_other", "דולג/הוסר/אחר")
    add("str_ep_to_download", "להורדה")
    add("str_dl_state_to_download", "להורדה")

    add("str_select_none_cleanup", "נקה בחירה")
    add("str_submit_lang", "שלח שפה")
    
    add("str_dltab_live", "הורדות פעילות: ")
    add("str_dltab_ul_speed", "קצב העלאה: ")
    add("str_dltab_dl_speed", "קצב הורדה: ")


    ##_________________________________________________________
    ##
    ##     Main window (iPodder.xrc)
    ##_________________________________________________________


    
    ## File menu
    add("str_file", "קובץ")
    add("str_import_opml", "יבא feeds מ opml...")
    add("str_export_opml", "יצא feeds כ opml...")
    add("str_preferences_menubar", "העדפות...")
    add("str_close_window", "סגור חלון")
    add("str_quit", "צא")

    add("str_edit", "ערוך")
    add("str_select_all", "בחר הכל")

    add("str_tools", "כלים")
    add("str_check_all", "בחר הכל")
    add("str_catch_up", "השלם חוסרים")
    add("str_check_selected", "בדוק את הבחורים")
    add("str_add_feed", "הוסף Feed...")
    add("str_remove_selected", "הסר Feed")
    add("str_feed_properties", "תכונות Feed...")
    add("str_scheduler_menubar", "מתאם זמנים...")
    
    add("str_select_language", "בחר שפה")

    ## these are also used for the tabs
    add("str_view", "תצוגה")
    add("str_downloads", "הורדות")
    add("str_subscriptions", "מינויים")
    add("str_podcast_directory", "תיקיית פודקאסטים")
    add("str_cleanup", "מחיקות")

    add("str_help", "עזרה")
    add("str_online_help", "עזרה מקוונת")
    add("str_faq", "שאלות נפוצות")
    add("str_check_for_update", "בדוק לעדכון...")
    add("str_report_a_problem", "דווח על תקלה")
    add("str_goto_website", "גלוש לאתר")
    add("str_make_donation", "תרום לפרוייקט")
    add("str_menu_license", "רשיון...")
    add("str_about", "אודות...")


    ## Downloadstab Toolbar
    add("str_remove_selected_items", "הסר עצמים שנבחרו")
    add("str_cancel_selected_download", "בטל הורדות שנבחרו")
    add("str_pause_selected", "הפסק זמנית הורדה של הפרקים")

    ## Downloadstab States (in columns)
    ## Enclosure states. Use str_dl_state_ prefix to avoid collisions with
    ## other strings, e.g. str_downloading above which isn't capitalized.
    add("str_dl_state_new", "חדש")
    add("str_dl_state_queued", "בתור")
    add("str_dl_state_downloading", "מוריד")
    add("str_dl_state_downloaded", "ירד")
    add("str_dl_state_cancelled", "בוטל")
    add("str_dl_state_finished", "הסתיים")
    add("str_dl_state_partial", "ירד חלקית")
    add("str_dl_state_clearing", "מנקה")


    ## Subscriptionstab Toolbar
    add("str_check_for_new_podcasts", "בדוק לפרקים חדשים")
    add("str_catch_up_mode", "השלם חוסרים - הורד את המינויים החדשים בלבד")

    add("str_add_new_feed", "הוסף feed");
    add("str_remove_selected_feed", "הסר feed שנבחר")
    add("str_properties", "אפשרויות Feed")
    add("str_check_selected_feed", "בדוק/הורד feed שנבחר")

    add("str_scheduler_on", "מתאם זמנים - פעיל")
    add("str_scheduler_off", "מתאם זמנים - מופסק")        

    ## Subscriptionstab Scheduler information
    add("str_next_run:", "ריצה הבאה:")

    ## Subscriptionstab episode frame
    add("str_downloading_episode_info", "מוריד מידע על הפרקים...")
    add("str_no_episodes_found", "לא נמצאו פרקים.")


    ## Directorytab Toolbar
    add("str_refresh", "רענן")
    add("str_open_all_folders", "פתח את כל התיקיות")
    add("str_close_all_folders", "סגור את כל התיקיות")
    add("str_add", "הוסף")

    ## Directorytab Other items
    add("str_directory_description", "בחר ב feed או הזן במקום המיועד לכך מעלה, והוסף.")




    ## Cleanuptab items
    add("str_select_a_feed", "בחר ב feed")
    add("str_refresh_cleanup", "רענן")
    
    add("str_look_in", "בדוק לפרקים ב")        
    add("str_player_library", "ספריית הנגן")
    add("str_downloads_folder", "סיפריית הורדות")
    add("str_delete_library_entries", "Delete library entries")
    add("str_delete_files", "מחק קבצים שירדו")
    add("str_select_all_cleanup", "בחר הכל")
    add("str_delete", "מחק")




    ## Logtab items
    add("str_log", "רישום")
    add("str_clear", "מחק")


    ## Columns (in downloads- and subscriptionstab)
    add("str_lst_name", "שם")
    add("str_lst_date", "תאריך")        
    add("str_lst_progress", "התקדמות")
    add("str_lst_state", "מצב")
    add("str_lst_mb", "MB")
    add("str_lst_location", "כתובת")
    add("str_lst_episode", "פרק")
    add("str_lst_playlist", "פודקאסט")

    ## Feed subscription states -- see ipodder/feeds.py SUB_STATES variable
    add("str_subscribed", "מנוי")
    add("str_disabled", "מנוטרל")
    add("str_newly-subscribed", "מנוי חדש")
    add("str_unsubscribed", "לא מנוי")
    add("str_preview", "תצוגה מקדימה")
    add("str_force", "הכרח")
    





    ##_________________________________________________________
    ##
    ##   Dialog Windows
    ##_________________________________________________________



    ## OPML Import Dialog
    #--- Select import file

    ## OPML Export Dialog
    add("str_choose_name_export_file", "בחר שם לקובץ היצוא")
    add("str_subs_exported", "מינויים יוצאו.")
    
    ## Preferences Dialog
    add("str_preferences", "העדפות")
    
    add("str_save", "שמור")
    add("str_cancel", "בטל")
    
    # General
    add("str_general", "כללי")
    add("str_gen_options_expl", "קבע אפשרויות כלליות לתוכנה")
    add("str_hide_on_startup", "בעליה, הצג את התוכנה ב ‎Tray בלבד")

    add("str_run_check_startup", "בדוק בטעינת התוכנה אם יש פרקים חדשים")
    add("str_play_after_download", "נגן פרק מייד לאחר הורדתו")
    add("str_location_and_storage", "ניהול מיקום ואחסון")
    add("str_stop_downloading", "הפסק הורדה אם המקום בכונן ירד מתחת לגבול")
    add("str_bad_megabyte_limit_1", "גבול הגודל אינו נראה כמו מספר")
    add("str_bad_megabyte_limit_2", "אנא נסה פעם נוספת.")

    add("str_download_folder", "הורד פודקאסטים לתיקיה זו")
    add("str_browse", "Browse")
    add("str_bad_directory_pref_1", "לא נמצאה התיקייה שהוכנסה")
    add("str_bad_directory_pref_2", "אנא צור אותה ונסה פעם נוספת")

    
    # Threading
    add("str_threads", "מקביליות")
    add("str_multiple_download", "הגדרות להורדה במקביל")
    add("str_max_feedscans", "מספר feeds שיסרקו בהתחברות")
    add("str_max_downloads", "מספר הורדות במקביל")
   
    # Network settings
    add("str_networking", "הגדרות רשת")
    add("str_coralize_urls", "צבע URLs (ניסיוני)")
    add("str_proxy_server", "השתמש ב proxyserver")
    add("str_proxy_address", "כתובת")
    add("str_proxy_port", "Port")
    add("str_proxy_username", "שם משתמש")
    add("str_proxy_password", "סיסמא")
    add("str_bad_proxy_pref", "אפשרת תמיכה ב proxy אך לא קבעת כתובת ו port. אנא חזור להגדרות הרשת כדי לקבוע ערכים אלו.")

    # Player
    add("str_player", "נגן")
    add("str_choose_a_player", "בחר נגן")
    add("str_no_player", "ללא נגן")
    
    # Advanced
    add("str_advanced", "מתקדם")
    add("str_options_power_users", "אפשרויות אלו נועדו למשתמש מתקדם")
    add("str_run_command_download", "הרץ פקודה זו לאחר כל הורדה")
    add("str_rcmd_full_path", "%f = נתיב מלא לקובץ המורד")
    add("str_rcmd_podcast_name", "%n = שם הפודקאסט")
    add("str_other_advanced_options", "אפשרויות מתקדמות נוספות")
    add("str_show_log", "הצג לשונית רישום ביישום")



    ## Feed Dialog (add/properties)
    add("str_title", "כותרת")
    add("str_url", "URL")
    add("str_goto_subs", "גש ללשונית המינויים כדי לצפות בפרקים של פודקאסט זה")
    add("str_feed_save", "שמור")
    add("str_feed_cancel", "בטל")

    ## Scheduler Dialog
    add("str_enable_scheduler", "אפשר תיאום זמנים")
    add("str_sched_select_type", "בחר למטה אם לבדוק בזמנים קבועים ביום, או במרווח זמן קבוע:")
    add("str_check_at_specific_times", "בדוק בזמנים אלו")
    add("str_check_at_regular_intervals", "בדוק במרווחי זמן קבועים")
    add("str_repeat_every:", "חזור בכל:")
    add("str_latest_run", "ריצה אחרונה:")
    add("str_next_run", "ריצה הבאה:")
    add("str_not_yet", "עדיין לא")
    #--- Cancel
    add("str_save_and_close", "שמור וסגור")
    #--- Save

    add("str_time_error", "נראה שאחד מתיאומי הזמנים אינו תקין. זמנים תקינים נראים כך: 10:02am, 16:43.")


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
    add("str_check_for_new_podcast_button", "בדוק לפודקאסטים חדשים על-ידי לחיצה על הכפתור הירוק")
    add("str_last_check", "בדיקה אחרונה הושלמה ב")
    add("str_of", "מתוך")
    add("str_item", "עצם")
    add("str_items", "עצמים")
    add("str_downloading", "מוריד")
    add("str_downloaded", "ירד")
    add("str_enclosure", "enclosure")
    add("str_enclosures", "enclosures")
    add("str_fetched", "fetched")
    add("str_loading_mediaplayer", "טוען את נגן המדיה...")
    add("str_loaded_mediaplayer", "נטען נגן המדיה...")        
    add("str_initialized", "התוכנה מוכנה")




    ## Other application strings
    add("str_ipodder_title", PRODUCT_NAME + " - Podcast receiver v" + __version__)
    add("str_localization_restart", "כדי לשנות שפה יש להתחיל מחדש את התוכנה. לחץ על אישור כדי להתחיל מחדש בצורה מסודרת, או על ביטול כדי להמשיך.")
    add("str_really_quit", "ישנו קובץ בהורדה, באמת לצאת?");
    add("str_double_check", "נראה שקובץ נמצא בהורדה.");
    
    # check for update
    add("str_new_version_ipodder", "ישנה גרסה חדשה של התוכנה, בחר באישור כדי לגלוש לאתר ההורדה")
    add("str_no_new_version_ipodder", "גרסה זו של התוכנה היא העדכנית")
    add("str_other_copy_running", "התוכנה כבר רצה. אנא צא מהריצה הקיימת כדי להריץ את התוכנה שנית")

    # Windows taskbar right-click menu
    add("str_check_now", "בדוק כעת")        
    add("str_open_ipodder", "פתח %s" % PRODUCT_NAME)
    #--- Downloading
    add("str_scanning_feeds", "סורק feeds")

    # Feed right-click menu
    add("str_remove", "הסר")        
    add("str_open_in_browser", "פתח בדפדפן")
    
    

    # Downloads right-click menu
    add("str_play_episode", "נגן פרק בנגן המדיה")
    add("str_clear_selected", "נקה פרקים שנבחרו")
    









