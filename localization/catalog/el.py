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

    add("str_username", "Όνομα Χρήστη")
    add("str_password", "Κωδικός")
    add("str_missing_proxy_password", "Ένα όνομα χρήστη για διακομιστή μεσολάβησης (proxy) ορίστηκε, αλλά όχι και ένας κωδικός. \n" \
        "Παρακαλώ σβήστε το όνομα χρήστη, ή δώστε ένα κωδικό.")

    add("str_goto_background_on_close_title", "Ορισμός τρόπου τερματισμού")
    add("str_goto_background_on_close_warn", \
        "Το %s μπορεί να συνεχίσει διακριτικά την λειτουργία του μετά το κλείσιμο. \n" \
        "Διαφορετικά μπορεί να τερματίσει την λειτουργία του.  Θα θέλατε το %s \n" \
        "να εξακολουθήσει να λειτουργεί;" % (PRODUCT_NAME,PRODUCT_NAME))
    add("str_goto_background_on_close_pref", "Διακριτική λειτουργία με το κλείσιμο του κυρίως παραθύρου.")
    add("str_yes", "Ναι")
    add("str_no", "Όχι")
    add("str_dont_ask", "Να μην ερωτηθώ ξανά")
    add("str_ok", "Επιβεβαίωση")
    add("str_hide_window", "Απόκρυψη Παραθύρου")
    add("str_hide_tray_icon", "Απόκρυψη Εικονιδίου στη Γραμμή Εργασίας")
    add("str_show_window", "Εμφάνιση Παραθύρου")

    add("str_catchup_pref", "Η Αναπλήρωση (catch-up) προσπερνά τα παλιότερα επεισόδια, οριστικά.")
    add("str_set_catchup_title", "Ορισμός τρόπου Αναπλήρωσης")
    add("str_set_catchup_description", \
        "Όταν ελέγχει σε κατάσταση Αναπλήρωσης, το %s προσπερνά όλα εκτός από τα πιο πρόσφατα \n" \
        "στοιχεία σε κάθε Feed. Παρακαλώ, διαλέξτε τι να κάνει το %s με τα \n" \
        "προσπερασμένα στοιχεία." % (PRODUCT_NAME,PRODUCT_NAME))
    add("str_skip_permanently", "Προσπέρασμα Οριστικά")
    add("str_skip_temporarily", "Προσπέρασμα μόνο αυτή τη φορά")
    
    add("str_set_oneclick_handler", "Ορισμός ανάληψης με ένα κλίκ")
    add("str_set_oneclick_handler_warn",\
        "Το %s αυτή την στιγμή δεν έχει ρυθμιστεί να αναλαμβάνει Άμεσες Συνδρομές (με ένα κλίκ) σε Podcasts. \n" \
        "Θέλετε να ρυθμιστεί το %s να ξεκινά όταν κάνετε κλίκ σε Άμεσες Συνδρομές (με ένα κλίκ);" % (PRODUCT_NAME,PRODUCT_NAME))
    add("str_ensure_oneclick_handler", "Πάντα να χρησιμοποιείται το %s για άμεση (με ένα κλίκ) συνδρομή" % PRODUCT_NAME)
    
    add("str_txt_feedmanager", "Συμβατοί Διαχειριστές Feed:")
    add("str_feedmanager_btn_podnova", "www.PodNova.com - Εύρεση Podcasts, Άμεση Συνδρομή (με ένα κλίκ)")

    add("str_open_downloads_folder", "Άνοιγμα Φακέλου κατεβασμένων αρχείων")
    add("str_chkupdate_on_startup", "Έλεγχος για νέα έκδοση του προγράμματος με το ξεκίνημα.")
    add("str_bad_feedmanager_url", "Παρακαλώ δώστε μία έγκυρη διεύθυνση (URL) για τον Διαχειριστή Feed.")
    add("str_feed_manager", "Διαχειριστής Feed")
    add("str_feedmanager_enable", "Συγχρονισμός των συνδρομών μου μέσω μίας απομακρυσμένης υπηρεσίας")
    add("str_opml_url", "Διεύθυνση (URL) OPML")
    add("str_set_track_genre", "Ορισμός του είδους του κομματιού ως")
    add("str_auto_delete", "Αυτόματη διαγραφή Επεισοδίων παλιότερων από")
    add("str_days_old", "ημέρες")
    
    add("str_show_notes", "Εμφάνιση Σημειώσεων")
    add("str_close", "Κλείσιμο")
    
    add("str_critical_error_minspace_exceeded", \
        "Το Κατέβασμα προσπεράστηκε; ο ελεύθερος χώρος είναι %dMB λιγότερος " \
        "από τα ελάχιστα %dMB.  Παρακαλώ, ελευθερώστε χώρο " \
        "στο δίσκο σας με την Εκκαθάριση ή προσαρμόστε τις ρυθμίσεις Διαχείρισης " \
        "Αποθήκευσης στις Επιλογές")
    add("str_critical_error_unknown", "Άγνωστο σφάλμα κατά το κατέβασμα αρχείων.")
    
    add("str_error_checking_new_version", "Υπήρξε ένα σφάλμα κατά τον έλεγχο για νέα έκδοση. Παρακαλώ προσπαθήστε ξανά αργότερα.")
    add("str_hours", "ώρες")
    add("str_minutes", "λεπτά")

    # The next 4 are for the status bar updates during the initial scan.
    add("str_scanning", "Διερεύνηση")
    add("str_scanned", "Διερευνήθηκαν")
    add("str_feed", "Feed")
    add("str_feeds", "Feeds")
    
    add("str_downloading_new_episodes", "Κατέβασμα νέων Επεισοδίων")
    add("str_sched_specific", "Έλεγχος σε συγκεκριμένες χρονικές στιγμές")
    add("str_sched_reg", "Έλεγχος ανά τακτά διαστήματα")
    add("str_repeat_every", "Επανάληψη κάθε")
    add("str_next_run_label", "Επόμενη εκτέλεση:")
    
    add("str_license", "Αυτό το πρόγραμμα είναι ελεύθερο λογισμικό, μπορείτε να το επαναδιανέμετε και/ή να το τροποποιήσετε σύμφωνα με τους όρους της Άδειας Χρήσης GNU General Public License όπως αυτή εκδίδεται από το Free Software Foundation στην Δεύτερη (2) εκδοσή της ή κατ'επιλογή σας όποια μεταγενέστερη άδεια. Αυτό το πρόγραμμα διανέμεται με την ελπίδα πως θα είναι χρήσιμο, αλλά χωρίς καμία εγγύηση, χωρίς καν την υπονοούμενη εγγύηση εμπορικής διαθεσιμότητας ή καταλληλότητας για συγκεκριμένο σκοπό. \n\nΔείτε την GNU General Public License Άδεια Χρήσης για περισσότερες πληροφορίες.")

    add("str_donate", "Δωρίστε στο %s" % PRODUCT_NAME)
    add("str_donate_expl", "Το %s είναι ιδιοκτησία της παγκόσμιας κοινότητας των χρηστών του. Είναι σημαντικό να διατηρηθεί αυτός ο νέος τρόπος πρόσβασης σε μέσα επικοινωνίας ελεύθερος. Οποιοδήποτε χρηματικό ποσό θα έδινε χαρά και ενθάρρυνση στην ομάδα του %s για την ανάπτυξη νέων λειτουργιών και υπηρεσιών." % (PRODUCT_NAME,PRODUCT_NAME))
    add("str_donate_yes", "Ναι, επίσκεψη στην ιστοσελίδα δωρεών τώρα!")
    add("str_donate_two_weeks", "Θέλω να το δοκιμάσω λίγο ακόμα, εμφάνιση αυτού του μηνύματος ξανά μετά από δύο εβδομάδες.")
    add("str_donate_already", "Έχω ήδη δωρήσει, μην εμφανιστεί ξανά αυτό το μήνυμα.")
    add("str_donate_no", "Όχι, δεν θέλω να κάνω οποιαδήποτε δωρεά ποτέ, να μην εμφανιστεί ξανά αυτό το μήνυμα.")
    add("str_donate_one_day", "Όχι τώρα, υπενθυμίστε μου πάλι αύριο.")
    add("str_donate_proceed", "Συνέχεια")

    add("str_scheduler_dialog", "Προγραμματιστής")
    add("str_scheduler_tab", "Ρυθμίσεις")

    add("str_select_import_file", "Επιλογή αρχείου προς εισαγωγή")    
    add("str_add_feed_dialog", "Προσθήκη ενός Feed")
    add("str_edit_feed", "Ιδιότητες Feed")

    add("str_really_delete", "Επιβεβαίωση διαγραφής")

    add("str_license_caption", "Άδεια Χρήσης")

    add("str_ep_downloaded", "Κατεβασμένο")
    add("str_ep_skipped_removed_other", "Προσπερασμένο/Διαγραμμένο/Άλλο")
    add("str_ep_to_download", "Προς Κατέβασμα")

    add("str_select_none_cleanup", "Select none")
    add("str_submit_lang", "Υποβολή Γλώσσας")
    
    add("str_dltab_live", "Ενεργά κατεβάσματα αρχείων: ")
    add("str_dltab_ul_speed", "Ταχύτητα ανεβάσματος: ")
    add("str_dltab_dl_speed", "Ταχύτητα κατεβάσματος: ")


    ##_________________________________________________________
    ##
    ##     Main window (iPodder.xrc)
    ##_________________________________________________________


    
    ## File menu
    add("str_file", "Αρχείο")
    add("str_import_opml", "Εισαγωγή Feed από opml...")
    add("str_export_opml", "Εξαγωγή των Feed ως opml...")
    add("str_preferences_menubar", "Επιλογές...")
    add("str_close_window", "Κλείσιμο παραθύρου")
    add("str_quit", "Εγκατάλειψη")

    add("str_edit", "Επεξεργασία")
    add("str_select_all", "Επιλογή όλων")

    add("str_tools", "Εργαλεία")
    add("str_check_all", "Έλεγχος όλων")
    add("str_catch_up", "Αναπλήρωση")
    add("str_check_selected", "Έλεγχος επιλεγμένων")
    add("str_add_feed", "Προσθήκη ενός Feed...")
    add("str_remove_selected", "Αφαίρεση ενός Feed")
    add("str_feed_properties", "Ιδιότητες Feed...")
    add("str_scheduler_menubar", "Προγραμματιστής...")
    
    add("str_select_language", "Επιλογή γλώσσας")

    ## these are also used for the tabs
    add("str_view", "Προβολή")
    add("str_downloads", "Κατέβασμα Αρχείων")
    add("str_subscriptions", "Συνδρομές")
    add("str_podcast_directory", "Ευρετήριο Podcast")
    add("str_cleanup", "Εκκαθάριση")

    add("str_help", "Βοήθεια")
    add("str_online_help", "Online Βοήθεια")
    add("str_faq", "Συχνές Ερωτήσεις")
    add("str_check_for_update", "Έλεγχος νέας έκδοσης...")
    add("str_report_a_problem", "Αναφορές Προβλημάτων")
    add("str_goto_website", "Επίσκεψη στο Website")
    add("str_make_donation", "Δωρεές")
    add("str_menu_license", "Άδεια Χρήσης...")
    add("str_about", "Αναφορικά...")


    ## Downloadstab Toolbar
    add("str_remove_selected_items", "Απομάκρυνση επιλεγμένων αντικειμένων")
    add("str_cancel_selected_download", "Ακύρωση επιλεγμένου κατεβάσματος αρχείου")
    add("str_pause_selected", "Παύση επιλεγμένων")

    ## Downloadstab States (in columns)
    ## Enclosure states. Use str_dl_state_ prefix to avoid collisions with
    ## other strings, e.g. str_downloading above which isn't capitalized.
    add("str_dl_state_new", "Νέο")
    add("str_dl_state_queued", "Στη σειρά")
    add("str_dl_state_downloading", "Κατεβαίνει")
    add("str_dl_state_downloaded", "Κατεβασμένο")
    add("str_dl_state_cancelled", "Ακυρώθηκε")
    add("str_dl_state_finished", "Ολοκλήρωσε")
    add("str_dl_state_partial", "Τμηματικά κατεβασμένο")
    add("str_dl_state_clearing", "Clearing")


    ## Subscriptionstab Toolbar
    add("str_check_for_new_podcasts", "Έλεγχος για νέα Podcasts")
    add("str_catch_up_mode", "Catch-up - Κατέβασμα μόνο των τελευταίων νέων συνδρομών")

    add("str_add_new_feed", "Προσθήκη νέου feed");
    add("str_remove_selected_feed", "Αφαίρεση επιλεγμένου Feed")
    add("str_properties", "Ιδιότητες Feed")
    add("str_check_selected_feed", "Έλεγχος/Κατέβασμα επιλεγμένου Feed")

    add("str_scheduler_on", "Προγραμματιστής - Ενεργός")
    add("str_scheduler_off", "Προγραμματιστής - Ανενεργός")        

    ## Subscriptionstab Scheduler information
    add("str_next_run:", "Επόμενη εκτέλεση:")

    ## Subscriptionstab episode frame
    add("str_downloading_episode_info", "Κατέβασμα πληροφοριών Επεισοδίων...")
    add("str_no_episodes_found", "Δεν βρέθηκαν επεισόδια.")


    ## Directorytab Toolbar
    add("str_refresh", "Ανανέωση")
    add("str_open_all_folders", "Άνοιγμα όλων των φακέλων")
    add("str_close_all_folders", "Κλείσιμο όλων των φακέλων")
    add("str_add", "Προσθήκη")

    ## Directorytab Other items
    add("str_directory_description", "Κάντε κλίκ σε ένα Feed του καταλόγου ή εισάγετε ένα στη φόρμα και κάντε κλίκ Προσθήκη")




    ## Cleanuptab items
    add("str_select_a_feed", "Επιλέξτε ένα Feed")
    add("str_refresh_cleanup", "Ανανέωση")
    
    add("str_look_in", "Αναζήτηση Επεισοδίων σε")        
    add("str_player_library", "Βιβλιοθήκη Προγράμματος Αναπαραγωγής")
    add("str_downloads_folder", "Φάκελος Κατεβασμένων αρχείων")
    add("str_delete_library_entries", "Διαγραφή εισαγωγών βιβλιοθήκης")
    add("str_delete_files", "Διαγραφή κατεβασμένων αρχείων")
    add("str_select_all_cleanup", "Επιλογή όλων")
    add("str_delete", "Διαγραφή")




    ## Logtab items
    add("str_log", "Καταγραφή")
    add("str_clear", "Εκκαθάριση")


    ## Columns (in downloads- and subscriptionstab)
    add("str_lst_name", "Όνομα")
    add("str_lst_date", "Ημερομηνία")        
    add("str_lst_progress", "Πρόοδος")
    add("str_lst_state", "Κατάσταση")
    add("str_lst_mb", "MB")
    add("str_lst_location", "Τοποθεσία")
    add("str_lst_episode", "Επεισόδιο")
    add("str_lst_playlist", "Λίστα Αναπαραγωγής")

    ## Feed subscription states -- see ipodder/feeds.py SUB_STATES variable
    add("str_subscribed", "Συνδρομή")
    add("str_disabled", "Απενεργοποιημένο")
    add("str_newly-subscribed", "Νέα Συνδρομή")
    add("str_unsubscribed", "Ακυρωμένη Συνδρομή")
    add("str_preview", "Προεσκόπηση")
    add("str_force", "Εξαναγκασμός")
    





    ##_________________________________________________________
    ##
    ##   Dialog Windows
    ##_________________________________________________________



    ## OPML Import Dialog
    #--- Select import file

    ## OPML Export Dialog
    add("str_choose_name_export_file", "Επιλέξτε όνομα για το αρχείο προς εξαγωγή")
    add("str_subs_exported", "Οι Συνδρομές έχουν εξαχθεί.")
    
    ## Preferences Dialog
    add("str_preferences", "Επιλογές")
    
    add("str_save", "Αποθήκευση")
    add("str_cancel", "Άκυρο")
    
    # General
    add("str_general", "Γενικά")
    add("str_gen_options_expl", "Καθορισμός γενικών επιλογών για την εφαρμογή %s" % PRODUCT_NAME)
    add("str_hide_on_startup", "Στην εκκίνηση να εμφανίζεται το %s στο Πλαίσιο Συστήματος" % PRODUCT_NAME)

    add("str_run_check_startup", "Έλεγχος για νέα Podcasts με την εκκίνηση του προγράμματος")
    add("str_play_after_download", "Αναπαραγωγή κατεβασμένων αρχείων αμέσως μετά την λήψη τους")
    add("str_location_and_storage", "Ρυθμίσεις Διαχείρισης Αποθήκευσης")
    add("str_stop_downloading", "Τερματισμός κατεβάσματος αρχείων σε περίπτωση που ο ελεύθερος χώρος του Σκληρού Δίσκου φτάσει τα")
    add("str_bad_megabyte_limit_1", "Λυπάμαι, το ελάχιστο όριο ΜΒ πρέπει να είναι ακέραιος αριθμός")
    add("str_bad_megabyte_limit_2", "Παρακαλώ προσπαθήστε ξανά.")

    add("str_download_folder", "Κατέβασμα Podcasts σε αυτόν τον φάκελο")
    add("str_browse", "Αναζήτηση")
    add("str_bad_directory_pref_1", "Λυπάμαι, δεν μπορεί να εντοπιστεί ο φάκελος που επιλέξατε")
    add("str_bad_directory_pref_2", "Παρακαλώ δημιουργήστε τον και προσπαθήστε ξανά.")

    
    # Threading
    add("str_threads", "Threading")
    add("str_multiple_download", "Multiple download settings")
    add("str_max_feedscans", "maximal threads for feedscanning per session")
    add("str_max_downloads", "maximal downloads per session")
   
    # Network settings
    add("str_networking", "Ρυθμίσεις Δικτύου")
    add("str_coralize_urls", "Coralize URLs (πειραματικό)")
    add("str_proxy_server", "Χρήση ενός διακομιστή μεσολάβησης (proxy server)")
    add("str_proxy_address", "Διεύθυνση")
    add("str_proxy_port", "Port")
    add("str_proxy_username", "Όνομα Χρήστη")
    add("str_proxy_password", "Κωδικός")
    add("str_bad_proxy_pref", "Έχετε ενεργοποιήσει την υποστήριξη για διακομιστή μεσολάβησης (proxy) αλλά δεν δώσατε Διεύθυνση και port.  Παρακαλώ επιστρέψτε στις Ρυθμίσεις Δικτύου και ορίστε Διεύθυνση και port.")

    # Player
    add("str_player", "Πρόγραμμα Αναπαραγωγής")
    add("str_choose_a_player", "Επιλογή προγράμματος αναπαραγωγής")
    add("str_no_player", "Κανένα πρόγραμμα αναπαραγωγής")
    
    # Advanced
    add("str_advanced", "Για Προχωρημένους")
    add("str_options_power_users", "Αυτές οι επιλογές μπορούν να χρησιμοποιηθούν από Προχωρημένους Χρήστες")
    add("str_run_command_download", "Εκτέλεση αυτής της εντολής μετά από κάθε κατέβασμα αρχείου")
    add("str_rcmd_full_path", "%f = Πλήρης τοποθεσία δίσκου για το κατεβασμένο αρχείο")
    add("str_rcmd_podcast_name", "%n = Όνομα Podcast")
    add("str_other_advanced_options", "Άλλες προχωρημένες επιλογές")
    add("str_show_log", "Εμφάνιση καρτέλας Καταγραφής")



    ## Feed Dialog (add/properties)
    add("str_title", "Τίτλος")
    add("str_url", "Διεύθυνση URL")
    add("str_goto_subs", "Πηγαίνετε στην καρτέλα Συνδρομές για να δείτε τα επεισόδια αυτού του Feed")
    add("str_feed_save", "Αποθήκευση")
    add("str_feed_cancel", "Άκυρο")




    ## Scheduler Dialog
    add("str_enable_scheduler", "Ενεργοποίηση Προγραμματιστή")
    add("str_sched_select_type", "Επιλέξτε έλεγχο σε συγκεκριμένες χρονικές στιγμές ή ανά τακτά χρονικά διαστήματα:")
    add("str_check_at_specific_times", "Έλεγχος στις παρακάτω συγκεκριμένες χρονικές στιγμές")
    add("str_check_at_regular_intervals", "Έλεγχος ανά τακτά διαστήματα")
    add("str_repeat_every:", "Επανάληψη κάθε:")
    add("str_latest_run", "Πιο πρόσφατη εκτέλεση:")
    add("str_next_run", "Επόμενη εκτέλεση:")
    add("str_not_yet", "Όχι ακόμα")
    #--- Cancel
    add("str_save_and_close", "Αποθήκευση και Κλείσιμο")
    #--- Save

    add("str_time_error", "Κάποια από τις προγραμματισμένες στιγμές δεν είναι σωστή. Οι έγκυρες χρονικές στιγμές έχουν την μορφή:  10:02am, 16:43.")


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
    add("str_check_for_new_podcast_button", "Ελέγξτε για νέα Podcasts πατώντας το πράσινο κουμπί ελέγχου.")
    add("str_last_check", "Ο τελευταίος έλεγχος ολοκληρώθηκε στις")
    add("str_of", "of")
    add("str_item", "αντικείμενο")
    add("str_items", "αντικείμενα")
    add("str_downloading", "κατεβαίνει")
    add("str_downloaded", "κατεβασμένο")
    add("str_enclosure", "enclosure")
    add("str_enclosures", "enclosures")
    add("str_fetched", "fetched")
    add("str_loading_mediaplayer", "Άνοιγμα προγράμματος αναπαραγωγής...")
    add("str_loaded_mediaplayer", "Το πρόγραμμα αναπαραγωγής ενεργοποιήθηκε...")        
    add("str_initialized", "%s έτοιμο" % PRODUCT_NAME)




    ## Other application strings
    add("str_ipodder_title", PRODUCT_NAME + " - Podcast receiver v" + __version__)
    add("str_localization_restart", "Για να μεταφραστούν όλα τα κουμπιά ελέγχου του %s χρειάζεται επανεκκίνηση. Πατήστε Επιβεβαίωση για κλείσιμο, ή Άκυρο για συνέχεια." % PRODUCT_NAME)
    add("str_really_quit", "Ένα κατέβασμα αρχείου είναι σε εξέλιξη. Σίγουρα να τερματίσει;");
    add("str_double_check", "Φαίνεται πως κάποιο κατέβασμα αρχείου βρίσκεται σε εξέλιξη.");
    
    # check for update
    add("str_new_version_ipodder", "Υπάρχει μία νέα έκδοση του %s, πατήστε Επιβεβαίωση για επίσκεψη στον ιστοχώρο κατεβάσματος." % PRODUCT_NAME)
    add("str_no_new_version_ipodder", "Αυτή η έκδοση του %s είναι ενήμερη." % PRODUCT_NAME)
    add("str_other_copy_running", "Ένα άλλο αντίγραφο του %s είναι ανοικτό. Παρακαλώ ανοίξτε το, περιμένετε να ολοκληρώσει, ή κλείστε το." % PRODUCT_NAME)

    # Windows taskbar right-click menu
    add("str_check_now", "Έλεγχος Τώρα")        
    add("str_open_ipodder", "Άνοιγμα %s" % PRODUCT_NAME)
    #--- Downloading
    add("str_scanning_feeds", "Έλεγχος Feeds")

    # Feed right-click menu
    add("str_remove", "Αφαίρεση")
    add("str_open_in_browser", "Άνοιγμα στον Φυλλομετρητή")
    
    

    # Downloads right-click menu
    add("str_play_episode", "Αναπαραγωγή επεισοδίου στο πρόγραμμα αναπαραγωγής ήχου")
    add("str_clear_selected", "Εκκαθάριση επιλεγμένων αντικειμένων")
    



