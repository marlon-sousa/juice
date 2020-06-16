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

    #######################################################
    ## MV: 03 mar 2005 22:00
    ## A LIRE AVANT D'EDITER / AJOUTER !!
    ## Si vous ajoutez de nouvelles entrées,
    ## ajoutez les dans la partie "Nouvelles chaines'.
    ## On pourra facilement les transmettre aux traducteurs.
    #######################################################

    ##_________________________________________________________
    ##
    ##     Nouvelles chaines
    ##_________________________________________________________

    add("str_error_checking_new_version", "Nous sommes désolé, il y a eu une erreur lors de la vérification de mise à jour. Essayer de nouveau plus tard.")
    add("str_hours", "heures")
    add("str_minutes", "minutes")

    # The next 4 are for the status bar updates during the initial scan.
    add("str_scanning", "Recherche en cours")
    add("str_scanned", "Recherche terminée")
    add("str_feed", "source")
    add("str_feeds", "sources")

    add("str_downloading_new_episodes", "Téléchargement de nouveaux épisodes")

    add("str_select_none_cleanup", "Aucun")
    add("str_submit_lang", "Soumettre une traduction")
    
    add("str_dltab_live", "Téléchargement en cours : ")
    add("str_dltab_ul_speed", "Vitesse d'envoi : ")
    add("str_dltab_dl_speed", "Vitesse de réception : ")
    


    add("str_sched_specific", "Vérifier à heure régulière")
    add("str_sched_reg", "Vérifier à intervals réguliers")
    add("str_repeat_every", "Répéter tous les")
    add("str_next_run_label", "Prochaine vérification :")
    
    add("str_menu_license", "Licence")
    add("str_license", "Ce programme est libre, vous pouvez le redistribuer et/ou le modifier selon les termes de la Licence Publique Générale GNU publiée par la Free Software Foundation (version 2 ou bien toute autre version ultérieure choisie par vous). Ce programme est distribué car potentiellement utile, mais SANS AUCUNE GARANTIE, ni explicite ni implicite, y compris les garanties de commercialisation ou d'adaptation dans un but spécifique.\n\nReportez-vous à la Licence Publique Générale GNU pour plus de détails.")
    add("str_donate", "Faites un don pour %s" % PRODUCT_NAME)
    add("str_donate_expl", "Il est important de garder les applications %s communautaire en ligne et de garder cette nouvelle façon de consommer les médias, libre. Quelque soit la somme, l'équipe de développement sera contente et sera encouragée à développer de nouvelles fonctionnalités et de nouveaux services !" % PRODUCT_NAME)
    add("str_donate_yes", "Oui, envoyez-moi sur la page de contributions !")
    add("str_donate_two_weeks", "Je dois encore y jeter un oeil, montre moi ça de nouveau dans 2 semaines.")
    add("str_donate_already", "J'ai déjà fait un don. Ne me montre plus cette fenêtre.")
    add("str_donate_no", "Non, je ne veux pas faire de don, ne me montre plus cette fenêtre.")
    add("str_donate_one_day", "Pas maintenant, rappelez-moi demain")
    add("str_donate_proceed", "Allez, on y va :o)")

    add("str_preferences", "Préférences")
    add("str_preferences_menubar", "Préférences...")

    add("str_scheduler_dialog", "Programmateur")
    add("str_scheduler_tab", "Préférences")
    add("str_scheduler_menubar", "Programmateur...")

    add("str_select_import_file", "Choisir un fichier à importer")    
    add("str_add_feed_dialog", "Ajouter une source")
    add("str_edit_feed", "Propriétés de la source")

    add("str_really_delete", "Vraiment effacer")

    add("str_license_caption", "Licence")

    add("str_ep_downloaded", "téléchargé")
    add("str_ep_skipped_removed_other", "Sauté/Enlevé/AutreSource")
    add("str_dl_state_to_download", "A télécharger")


    
    ##_________________________________________________________
    ##
    ##     Fenêtre principale (iPodder.xrc)
    ##_________________________________________________________


    
    ## File menu
    add("str_file", "Fichier")
    add("str_import_opml", "Importer depuis un fichier OPML...")
    add("str_export_opml", "Exporter vers un fichier OPML...")
    add("str_preferences_menubar", "Préférences...")
    add("str_close_window", "Fermer la fenêtre")
    add("str_quit", "Quitter")

    add("str_edit", "Edition")
    add("str_select_all", "Tout sélectionner")

    add("str_tools", "Outils")
    add("str_check_all", "Tout vérifier")
    add("str_catch_up", "Marquer 'à jour'")
    add("str_check_selected", "Vérifier les sélections")
    add("str_add_feed", "Ajouter une source...")
    add("str_remove_selected", "Enlever une source")
    add("str_feed_properties", "Propriétés de la source...")
    add("str_scheduler_menubar", "Programmateur...")
    

    add("str_select_language", "Langue")

    ## Ils sont aussi utilisés pour les onglets
    add("str_view", "Affichage")
    add("str_downloads", "Téléchargements")
    add("str_subscriptions", "Abonnement")
    add("str_podcast_directory", "Bibliothèque de podcasts")
    add("str_cleanup", "Nettoyer")

    add("str_help", "Aide")
    add("str_online_help", "Aide en ligne")
    add("str_faq", "FAQ")
    add("str_check_for_update", "Vérifier les mises à jour...")
    add("str_report_a_problem", "Rapporter un problème")
    add("str_goto_website", "Aller sur le site")
    add("str_make_donation", "Faire un don")
    add("str_menu_license", "Licence...")
    add("str_about", "A propos...")


    ## Barre d'outils  : Téléchargement
    add("str_remove_selected_items", "Enlever les items sélectionnés")
    add("str_cancel_selected_download", "Annuler les téléchargements sélectionnés")
    add("str_pause_selected", "Pause")

    ## Etat onglet de téléchargement (dans les colonnes)
    ## Etats de l'Enclosure. Utiliser le préfixe str_dl_state_ afin d'éviter
    ## les collisions avec d'autres chaines, e.g. str_downloading ci-dessus
    ## qui ne sont pas en majuscule.
    add("str_dl_state_new", "Nouveau")
    add("str_dl_state_queued", "A la queue")
    add("str_dl_state_downloading", "En téléchargement")
    add("str_dl_state_downloaded", "Téléchargé")
    add("str_dl_state_cancelled", "Annulé")
    add("str_dl_state_finished", "Terminé")
    add("str_dl_state_partial", "Téléchargé partiellement")
    add("str_dl_state_clearing", "Nettoyage")


    ## Barre d'outil : Abonnement
    add("str_check_for_new_podcasts", "Recherche de nouveaux podcasts")
    add("str_catch_up_mode", "Catch-up - Seulement les derniers abonnements")

    add("str_add_new_feed", "Ajouter de nouvelles sources");
    add("str_remove_selected_feed", "Enlever les sources sélectionnées")
    add("str_properties", "Propriétés")
    add("str_check_selected_feed", "Vérifier les sources sélectionnées")

    add("str_scheduler_on", "Programmateur en marche")
    add("str_scheduler_off", "Programmateur arrêté")        

    ## Onglet Souscription : Info Programmateur
    add("str_next_run:", "Prochaine vérification :")

    ## Onglet Souscription : cadre épisode
    add("str_downloading_episode_info", "Téléchargement des infos de l'épisode...")
    add("str_no_episodes_found", "Aucun épisode.")


    ## Onglet Répertoire
    add("str_refresh", "Rafraîchir")
    add("str_open_all_folders", "Ouvrir tous les dossiers")
    add("str_close_all_folders", "Fermer tous les dossiers")
    add("str_add", "Ajouter")

    ## Onglet Répertoire : Autres entrées
    add("str_directory_description", "Cliquez sur une source ou entrez / collez dans le champ ci-dessus, puis cliquer Ajouter.")


    ## Onglet Nettoyage
    add("str_select_a_feed", "Sélectionner une source")
    add("str_refresh_cleanup", "Rafraîchir")
    
    add("str_look_in", "Chercher un épisode dans")        
    add("str_player_library", "Bibliothèque du lecteur")
    add("str_downloads_folder", "Dossier de téléchargement")
    add("str_delete_library_entries", "Effacer les entrées de la bibliothèque")
    add("str_delete_files", "Effacer les fichiers")
    add("str_select_all_cleanup", "Tout sélectionner")
    add("str_delete", "Nettoyer")




    ## Onglet journal
    add("str_log", "Journal")
    add("str_clear", "Vider")


    ## Colonnes (dans téléchargements et souscriptions)
    add("str_lst_name", "Nom")
    add("str_lst_date", "Date")        
    add("str_lst_progress", "Progression")
    add("str_lst_state", "Etat")
    add("str_lst_mb", "Mo")
    add("str_lst_location", "Lieu")
    add("str_lst_episode", "Episode")
    add("str_lst_playlist", "Playlist")

    ## Etat des abonnements -- voir les variables ipodder/feeds.py SUB_STATES
    add("str_subscribed", "Abonné")
    add("str_disabled", "Désactivé")
    add("str_newly-subscribed", "Nouveau abonnement")
    add("str_unsubscribed", "Désabonné")
    add("str_preview", "Prévisualisation")
    add("str_force", "Forcer")
    





    ##_________________________________________________________
    ##
    ##   Fenêtre de dialogue
    ##_________________________________________________________



    ## Fenêtre d'import OPML
    #--- Selection fichier import

    ## Fenêtre d'esport OPML
    add("str_choose_name_export_file", "Sélectionner un nom de fichier d'export")
    add("str_subs_exported", "Abonnements exportés.")
    
    ## Fenetre Préférences
    add("str_preferences", "Préférences")
    
    add("str_save", "Sauver")
    add("str_cancel", "Annuler")
    
    # Général
    add("str_general", "Général")
    add("str_gen_options_expl", "Définis les options générales de %s" % PRODUCT_NAME)
    add("str_hide_on_startup", "Au lancement, ne montrer que l'icone du system tray")

    add("str_run_check_startup", "Vérifier l'arrivée de nouveaux podcasts au démarrage de l'application")
    add("str_play_after_download", "Jouer les podcasts juste après leur téléchargement")
    add("str_location_and_storage", "Gestion des lieux de stockage")
    add("str_stop_downloading", "Arrêter les téléchargements si le disque dur atteint une taille minimum de")
    add("str_bad_megabyte_limit_1", "Désolé, la limite en MegaOctet ne semble pas être un entier")
    add("str_bad_megabyte_limit_2", "Essayez encore une fois.")

    add("str_download_folder", "Télécharger les podcasts dans ce dossier")
    add("str_browse", "Naviguer")
    add("str_bad_directory_pref_1", "Désolé, nous ne pouvons pas trouver les dossiers que vous avez entré")
    add("str_bad_directory_pref_2", "Créé le dossier et essayez de nouveau. Merci.")

    
    # Fil (threads)
    add("str_threads", "Téléchargement simultané")
    add("str_multiple_download", "Préférences de téléchargement simultané")
    add("str_max_feedscans", "Nombre maximal de recherche par session")
    add("str_max_downloads", "Nombre maximal de téléchargement par session")
   
    # Préférences réseau
    add("str_networking", "Préférences réseau")
    add("str_coralize_urls", "URL sur Coral CDN (experimental)")
    add("str_proxy_server", "Utiliser un serveur proxy")
    add("str_proxy_address", "Adresse")
    add("str_proxy_port", "Port")
    add("str_proxy_username", "Identifiant")
    add("str_proxy_password", "Mot de passe")
    add("str_bad_proxy_pref", "Vous avez activé le support proxy, mais vous n'avez pas donné ni d'hôte, ni de port. Revenez dans les préférences réseau et entrez le nom d'hôte et le port.")

    # Lecteur
    add("str_player", "Lecteur")
    add("str_choose_a_player", "Sélectionner un lecteur")
    add("str_no_player", "Aucun lecteur")
    
    # Advancé
    add("str_advanced", "Avancé")
    add("str_options_power_users", "Ces options peuvent être utilisées par les utilisateurs avancés")
    add("str_run_command_download", "Lancer cette commande après chaque téléchargement")
    add("str_rcmd_full_path", "%f = chemin complet du fichier téléchargé")
    add("str_rcmd_podcast_name", "%n = nom du podcast")
    add("str_other_advanced_options", "Autres options avancées")
    add("str_show_log", "Montrer l'onglet journal")



    ## Fenêtre de feeds (ajout/propriétés)
    add("str_title", "Titre")
    add("str_url", "URL")
    add("str_goto_subs", "Aller à l'onglet Abonnement pour voir les épisodes de cette source")
    add("str_feed_save", "Sauver")
    add("str_feed_cancel", "Annuler")




    ## Fenêtre programmateur
    add("str_enable_scheduler", "Activer le programmateur")
    add("str_sched_select_type", "Sélectionnez le type de programmateur ci-dessous :")
    add("str_check_at_specific_times", "Vérifier à heure régulière")
    add("str_check_at_regular_intervals", "Vérifier à intervals réguliers")
    add("str_repeat_every:", "Répéter toutes les :")
    add("str_latest_run", "Dernière vérification :")
    add("str_next_run", "Prochaine vérification :")
    add("str_not_yet", "pas encore")
    #--- Annuler
    add("str_save_and_close", "Sauver et fermer")
    #--- Sauver

    add("str_time_error", "Une des heures programmées ne semble pas correcte. Exemple valide : 10:02am, 16:43.")


    ## Fenêtre A propos
    #--- Version:
    #--- Programmation : Erik de Jonge, Andrew Grumet, Garth Kidd, Perica Zivkovic\nDesign: Martijn Venrooy\nStratège de contenu : Mark Alexander Posth\nConcept: Adam Curry, Dave Winer\nMerci à tous les traducteurs pour leur apports !\n\nBasé sur Feedparser et la technologie BitTorrent.\nCe programme est libre, vous pouvez le redistribuer et/ou le modifier selon les termes de la Licence Publique Générale GNU publiée par la Free Software Foundation (version 2 ou bien toute autre version ultérieure choisie par vous). Ce programme est distribué car potentiellement utile, mais SANS AUCUNE GARANTIE, ni explicite ni implicite, y compris les garanties de commercialisation ou d'adaptation dans un but spécifique. Reportez-vous à la Licence Publique Générale GNU pour plus de détails.


    ## Entrée de la barre de Status
    add("str_check_for_new_podcast_button", "Vérifier l'arrivée de nouveaux podcasts en cliquant le bouton vert")
    add("str_last_check", "Dernière vérification :")
    add("str_of", "de")
    add("str_item", "item")
    add("str_items", "items")
    add("str_downloading", "en téléchargement")
    add("str_downloaded", "téléchargé")
    add("str_enclosure", "enclosure")
    add("str_enclosures", "enclosures")
    add("str_fetched", "récupéré")
    add("str_loading_mediaplayer", "Lancement de votre lecteur de média...")
    add("str_loaded_mediaplayer", "Lecteur de média lancé...")        
    add("str_initialized", "%s prêt" % PRODUCT_NAME)




    ## Chaine pour d'autres applications
    add("str_ipodder_title", "%s - Récepteur de podcast v" % PRODUCT_NAME + __version__)
    add("str_localization_restart", "Pour changer la langue, %s doit être redémarré. Cliquez sur OK pour quitter proprement, ou Annuler pour continuer." % PRODUCT_NAME)
    add("str_really_quit", "Un téléchargement est en cours. Vraiment quitter ?");
    add("str_double_check", "Apparemment un téléchargement est en cours.");
    
    # Mise à jour
    add("str_new_version_ipodder", "Une nouvelle version de %s est disponible, cliquez sur OK pour aller sur le site." % PRODUCT_NAME)
    add("str_no_new_version_ipodder", "Cette version de %s est à jour" % PRODUCT_NAME)
    add("str_other_copy_running", "Une autre copie de %s est déja lancée. Mettez-la en avant, et attendez qu'elle se termine ou tuez le processus." % PRODUCT_NAME)

    # Menu contextuel (bouton droit de la souris, Windows)
    add("str_check_now", "Vérifier maintenant")        
    add("str_open_ipodder", "Ouvrir %s" % PRODUCT_NAME)
    #--- Téléchargement
    add("str_scanning_feeds", "Vérifications des sources")

    # Menu contextuel (Feed)
    add("str_remove", "Enlever")        
    add("str_open_in_browser", "Ouvrir dans un navigateur")
    
    

    # Menu contectuel (T2léchargements)
    add("str_play_episode", "Jouer l'épisode")
    add("str_clear_selected", "Nettoyer les entrées sélectionnées")
    




