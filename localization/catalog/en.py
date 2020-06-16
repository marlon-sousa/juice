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
    ##    u"Should we set iPodder to launch from one-click subscription links?" % PRODUCT_NAME)

    
    ##_________________________________________________________
    ##
    ##     New strings
    ##_________________________________________________________

    add("str_sort_cleanup_by_size", "Sort cleanup tab by size.")
    add("str_copy_location", "Copy Location")
    add("str_set_file_types", "Set file types")
    add("str_set_file_types_warn", \
        "%s is not currently set to handle some file types. \n" \
        "Would you like to set them now?" % PRODUCT_NAME)
    add("str_subscription_options", "One-click Subscription options:")
    add("str_enforce_settings", "Enforce these settings at startup")
    add("str_file_types", "File Types")
    add("str_play_button_enqueues", "Play button enqueues selected track")
    add("str_authentication", "Authentication")
    add("str_dl_state_skipped", "Skipped")
    add("str_dl_state_removed", "Removed")
    add("str_dl_selected", "Download selected")
    
    add("str_username", "Username")
    add("str_password", "Password")
    add("str_missing_proxy_password", "A proxy username was set but no proxy password. \n" \
        "Please either clear the username or enter a password.")

    add("str_goto_background_on_close_title", "Set close behavior")
    add("str_goto_background_on_close_warn", \
        "%s can continue running in the background after its main window \n" \
        "is closed.  Or %s can quit.  Would you like %s to continue \n" \
        "running?" % (PRODUCT_NAME,PRODUCT_NAME,PRODUCT_NAME))
    add("str_goto_background_on_close_pref", "Continue running in the background when I close the main window")
    add("str_yes", "Yes")
    add("str_no", "No")
    add("str_dont_ask", "Don't ask me again")
    add("str_ok", "OK")
    add("str_hide_window", "Hide window")
    add("str_hide_tray_icon", "Hide Tray Icon")
    add("str_show_window", "Show window")

    add("str_catchup_pref", "Catchup skips older episodes permanently")
    add("str_set_catchup_title", "Set catchup behavior")
    add("str_set_catchup_description", \
        "When checking in Catchup mode, %s will skip all but the top \n" \
        "item in each feed.  Please specify how %s should treat the \n" \
        "skipped items." % (PRODUCT_NAME,PRODUCT_NAME))
    add("str_skip_permanently", "Skip permanently")
    add("str_skip_temporarily", "Skip this time only")
    
    add("str_txt_feedmanager", "Compatible feedmanagers:")
    add("str_feedmanager_btn_podnova", "www.PodNova.com - Search or browse podcasts, single click subscribing")

    add("str_open_downloads_folder", "Open downloads folder")
    add("str_chkupdate_on_startup", "Check for new versions of the application at startup.")
    add("str_bad_feedmanager_url", "Please enter a valid URL for the feed manager.")
    add("str_feed_manager", "Feed manager")
    add("str_feedmanager_enable", "Synchronize my subscriptions from a remote service")
    add("str_opml_url", "OPML URL")
    add("str_set_track_genre", "Set track genre to")
    add("str_auto_delete", "Automatically delete episodes more than")
    add("str_days_old", "days old")
    
    add("str_show_notes", "Show Notes")
    add("str_close", "Close")
    
    add("str_critical_error_minspace_exceeded", \
        "Download skipped; free space %dMB less " \
        "than min %dMB.  Please free up space on " \
        "your disk using Cleanup or adjust the storage " \
        "management settings in Preferences")
    add("str_critical_error_unknown", "Unknown critical error while downloading.")
    
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

    add("str_donate", "Donate to Juice")
    add("str_donate_expl", "It's important to keep community-owned Juice applications online and keep this new way of consuming media free as in speech. Any amount of money will make the team happy and encourage them to work on new features and services!")
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
    add("str_file", "File")
    add("str_import_opml", "Import feeds from opml...")
    add("str_export_opml", "Export feeds as opml...")
    add("str_preferences_menubar", "Preferences...")
    add("str_close_window", "Close window")
    add("str_quit", "Quit")

    add("str_edit", "Edit")
    add("str_select_all", "Select all")

    add("str_tools", "Tools")
    add("str_check_all", "Check all")
    add("str_catch_up", "Catch-up")
    add("str_check_selected", "Check selected")
    add("str_add_feed", "Add a Feed...")
    add("str_remove_selected", "Remove Feed")
    add("str_feed_properties", "Feed properties...")
    add("str_scheduler_menubar", "Scheduler...")
    
    add("str_select_language", "Select language")

    ## these are also used for the tabs
    add("str_view", "View")
    add("str_downloads", "Downloads")
    add("str_subscriptions", "Subscriptions")
    add("str_podcast_directory", "Podcast directory")
    add("str_cleanup", "Cleanup")

    add("str_help", "Help")
    add("str_online_help", "Online Help")
    add("str_faq", "FAQ")
    add("str_check_for_update", "Check for Update...")
    add("str_report_a_problem", "Report a Problem")
    add("str_goto_website", "Go to the Website")
    add("str_make_donation", "Make a Donation")
    add("str_menu_license", "License...")
    add("str_about", "About...")


    ## Downloadstab Toolbar
    add("str_remove_selected_items", "Remove selected items")
    add("str_cancel_selected_download", "Cancel selected download")
    add("str_pause_selected", "Pause selected")

    ## Downloadstab States (in columns)
    ## Enclosure states. Use str_dl_state_ prefix to avoid collisions with
    ## other strings, e.g. str_downloading above which isn't capitalized.
    add("str_dl_state_new", "New")
    add("str_dl_state_queued", "Queued")
    add("str_dl_state_downloading", "Downloading")
    add("str_dl_state_downloaded", "Downloaded")
    add("str_dl_state_cancelled", "Cancelled")
    add("str_dl_state_finished", "Finished")
    add("str_dl_state_partial", "Partially downloaded")
    add("str_dl_state_clearing", "Clearing")


    ## Subscriptionstab Toolbar
    add("str_check_for_new_podcasts", "Check for new podcasts")
    add("str_catch_up_mode", "Catch-up - Only download the last new subscriptions")

    add("str_add_new_feed", "Add new feed");
    add("str_remove_selected_feed", "Remove selected feed")
    add("str_properties", "Feed Properties")
    add("str_check_selected_feed", "Check/Download selected feed")

    add("str_scheduler_on", "Scheduler - On")
    add("str_scheduler_off", "Scheduler - Off")        

    ## Subscriptionstab Scheduler information
    add("str_next_run:", "Next run:")

    ## Subscriptionstab episode frame
    add("str_downloading_episode_info", "Downloading episode info...")
    add("str_no_episodes_found", "No episodes found.")


    ## Directorytab Toolbar
    add("str_refresh", "Refresh")
    add("str_open_all_folders", "Open all folders")
    add("str_close_all_folders", "Close all folders")
    add("str_add", "Add")

    ## Directorytab Other items
    add("str_directory_description", "Click on a feed in the tree or type/paste in the space above then click add.")




    ## Cleanuptab items
    add("str_select_a_feed", "Select a feed")
    add("str_refresh_cleanup", "Refresh")
    
    add("str_look_in", "Look for episodes in")        
    add("str_player_library", "Player library")
    add("str_downloads_folder", "Downloads folder")
    add("str_delete_library_entries", "Delete library entries")
    add("str_delete_files", "Delete downloaded files")
    add("str_select_all_cleanup", "Select all")
    add("str_delete", "Delete")




    ## Logtab items
    add("str_log", "Log")
    add("str_clear", "Clear")


    ## Columns (in downloads- and subscriptionstab)
    add("str_lst_name", "Name")
    add("str_lst_date", "Date")        
    add("str_lst_progress", "Progress")
    add("str_lst_state", "State")
    add("str_lst_mb", "MB")
    add("str_lst_location", "Location")
    add("str_lst_episode", "Episode")
    add("str_lst_playlist", "Playlist")

    ## Feed subscription states -- see ipodder/feeds.py SUB_STATES variable
    add("str_subscribed", "Subscribed")
    add("str_disabled", "Disabled")
    add("str_newly-subscribed", "Newly Subscribed")
    add("str_unsubscribed", "Unsubscribed")
    add("str_preview", "Preview")
    add("str_force", "Force")
    





    ##_________________________________________________________
    ##
    ##   Dialog Windows
    ##_________________________________________________________



    ## OPML Import Dialog
    #--- Select import file

    ## OPML Export Dialog
    add("str_choose_name_export_file", "Choose a name for the export file")
    add("str_subs_exported", "Subscriptions exported.")
    
    ## Preferences Dialog
    add("str_preferences", "Preferences")
    
    add("str_save", "Save")
    add("str_cancel", "Cancel")
    
    # General
    add("str_general", "General")
    add("str_gen_options_expl", "Set the general options for the %s application" % PRODUCT_NAME)
    add("str_hide_on_startup", "At startup only show %s in the system tray" % PRODUCT_NAME)

    add("str_run_check_startup", "Run a check for new podcasts when the application is started")
    add("str_play_after_download", "Play downloads right after they're downloaded")
    add("str_location_and_storage", "Location and storage management")
    add("str_stop_downloading", "Stop downloading if harddisk reaches a minimal of")
    add("str_bad_megabyte_limit_1", "Sorry, the megabyte limit doesn't look like an integer")
    add("str_bad_megabyte_limit_2", "Please try again.")

    add("str_download_folder", "Download podcasts into this folder")
    add("str_browse", "Browse")
    add("str_bad_directory_pref_1", "Sorry, we couldn't find the directory you entered")
    add("str_bad_directory_pref_2", "Please create it and try again.")

    
    # Threading
    add("str_threads", "Threading")
    add("str_multiple_download", "Multiple download settings")
    add("str_max_feedscans", "maximal threads for feedscanning per session")
    add("str_max_downloads", "maximal downloads per session")
   
    # Network settings
    add("str_networking", "Network settings")
    add("str_coralize_urls", "Coralize URLs (experimental)")
    add("str_proxy_server", "Use a proxyserver")
    add("str_proxy_address", "Address")
    add("str_proxy_port", "Port")
    add("str_proxy_username", "Username")
    add("str_proxy_password", "Password")
    add("str_bad_proxy_pref", "You enabled proxy support but didn't provide a proxy host and port.  Please return to the Network settings tab and set the proxy host and port.")

    # Player
    add("str_player", "Player")
    add("str_choose_a_player", "Choose a player")
    add("str_no_player", "No player")
    
    # Advanced
    add("str_advanced", "Advanced")
    add("str_options_power_users", "These options can be used by Power Users")
    add("str_run_command_download", "Run this command after each download")
    add("str_rcmd_full_path", "%f = Full path to downloaded file")
    add("str_rcmd_podcast_name", "%n = Podcast name")
    add("str_rcmd_episode_title", "%e = Episode title")
    add("str_other_advanced_options", "Other advanced options")
    add("str_show_log", "Show log tab in application")



    ## Feed Dialog (add/properties)
    add("str_title", "Title")
    add("str_url", "URL")
    add("str_goto_subs", "Go to subscriptions tab to see this feed's episodes")
    add("str_feed_save", "Save")
    add("str_feed_cancel", "Cancel")
    add("str_feed_autodl", "Automatically download new episodes")




    ## Scheduler Dialog
    add("str_enable_scheduler", "Enable scheduler")
    add("str_sched_select_type", "Select radio buttons below to check at specific times or at regular intervals:")
    add("str_check_at_specific_times", "Check at these specific times")
    add("str_check_at_regular_intervals", "Check at regular intervals")
    add("str_repeat_every:", "Repeat every:")
    add("str_latest_run", "Latest run:")
    add("str_next_run", "Next run:")
    add("str_not_yet", "Not yet")
    #--- Cancel
    add("str_save_and_close", "Save and close")
    #--- Save

    add("str_time_error", "One of the scheduled times doesn't look right. Valid times look like this: 10:02am, 16:43.")


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
    add("str_check_for_new_podcast_button", "Check for new podcasts by pressing the button green check button")
    add("str_last_check", "Last check completed at")
    add("str_of", "of")
    add("str_item", "item")
    add("str_items", "items")
    add("str_downloading", "downloading")
    add("str_downloaded", "downloaded")
    add("str_enclosure", "enclosure")
    add("str_enclosures", "enclosures")
    add("str_fetched", "fetched")
    add("str_loading_mediaplayer", "Loading your media player...")
    add("str_loaded_mediaplayer", "Loaded your media player...")        
    add("str_initialized", "%s ready" % PRODUCT_NAME)




    ## Other application strings
    add("str_ipodder_title", PRODUCT_NAME + " - Podcast receiver v" + __version__)
    add("str_localization_restart", "To localize all controls of %s a restart is required. Click Ok to shutdown cleanly, cancel to continue." % PRODUCT_NAME)
    add("str_really_quit", "A download is in progress.  Really quit?");
    add("str_double_check", "It looks like a download is already in progress.");
    
    # check for update
    add("str_new_version_ipodder", "A new version of %s is available, press Ok to go to the download site." % PRODUCT_NAME)
    add("str_no_new_version_ipodder", "This version of %s is up to date" % PRODUCT_NAME)
    add("str_other_copy_running", "Another copy of %s is running. Please raise it, wait for it to complete, or kill it." % PRODUCT_NAME)

    # Windows taskbar right-click menu
    add("str_check_now", "Check Now")        
    add("str_open_ipodder", "Open %s" % PRODUCT_NAME)
    #--- Downloading
    add("str_scanning_feeds", "Scanning feeds")

    # Feed right-click menu
    add("str_remove", "Remove")        
    add("str_open_in_browser", "Open in browser")
    
    

    # Downloads right-click menu
    add("str_play_episode", "Play episode in mediaplayer")
    add("str_clear_selected", "Clear selected items")
    



