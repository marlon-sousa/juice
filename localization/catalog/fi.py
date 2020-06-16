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

    add("str_critical_error_minspace_exceeded", \
        "Lataus ohitettu; vapaata tilaa %dMt vähemmän " \
        "kuin tarvittava %dMt.  Vapauta levytilaa " \
        "käyttämällä siivoustoimintoa tai muuttamalla arkistointi- " \
        "asetuksia Asetuksista")
    add("str_critical_error_unknown", "Tuntematon kriittinen virhe latauksessa.")
    
    add("str_error_checking_new_version", "Pahoittelemme häiriötä version tarkistamisessa. Yritä uudelleen myöhemmin.")
    add("str_hours", "tuntia")
    add("str_minutes", "minuuttia")

    # The next 4 are for the status bar updates during the initial scan.
    add("str_scanning", "Etsii")
    add("str_scanned", "Etsiminen valmis")
    add("str_feed", "virta")
    add("str_feeds", "virtaa")
    
    add("str_downloading_new_episodes", "Lataa uusia jaksoja")
    add("str_sched_specific", "Tarkista määrättyinä aikoina")
    add("str_sched_reg", "Tarkista säännöllisesti")
    add("str_repeat_every", "Toista joka")
    add("str_next_run_label", "Seuraava suoritus:")
    
    add("str_license", "Tämä ohjelma on ilmainen ja vapaa; voit levittää ja/tai muokata sitä GNU General Public License:ssä määrätyllä tavalla, jonka on julkaissut Free Software Foundation; joko lisensiin version 2, tai (valintasi mukaan) uudemman version mukaan. Tätä ohjelmaa levitetään siinä toivossa, että se olisi hyödyllinen, mutta ilman minkäänlaista takuuta; ei edes takuuta sen sopivuudesta tiettyyn tarkoitukseen. \n\nLue GNU General Public License jos haluat lisätietoja.")

    add("str_donate", "Lahjoita rahaa %sille" % PRODUCT_NAME)
    add("str_donate_expl", "On tärkeää pitää yhteisön omistamia %s-ohjelmia verkossa ja pitää yllä sananvapautta tässä uudessa tavassa kuluttaa mediaa . Mikä tahansa rahasumma tekee työryhmän onnelliseksi ja rohkaisee heitä työskentelemään uusien ominaisuuksien ja palvelujen parissa!" % PRODUCT_NAME)
    add("str_donate_yes", "Kyllä, siirry lahjoitussivulle!")
    add("str_donate_two_weeks", "Minun pitää vielä tutustua paremmin, näytä tämä ilmoitus uudestaan kahden viikon kuluttua")
    add("str_donate_already", "Olen jo lahjoittanut, älä näytä tätä enää")
    add("str_donate_no", "Ei, en halua lahjoittaa, älä koskaan näytä tätä ilmoitusta enää")
    add("str_donate_one_day", "Ei nyt, ilmoita uudestaan päivän kuluttua")
    add("str_donate_proceed", "Jatka")

    add("str_scheduler_dialog", "Ajastin")
    add("str_scheduler_tab", "Asetukset")

    add("str_select_import_file", "Valitse tuotava tiedosto")    
    add("str_add_feed_dialog", "Lisää virta")
    add("str_edit_feed", "Virran ominaisuudet")

    add("str_really_delete", "Tuhoa oikeasti")

    add("str_license_caption", "Lisenssi")

    add("str_ep_downloaded", "Ladttu")
    add("str_ep_skipped_removed_other", "Hypätty/Poistettu/MuuVirta")
    add("str_dl_state_to_download", "Latausjonossa")

    add("str_select_none_cleanup", "Älä valitse mitään")
    add("str_submit_lang", "Lähetä kieli")
    
    add("str_dltab_live", "Aktiivisia latauksia: ")
    add("str_dltab_ul_speed", "Lähetysnopeus: ")
    add("str_dltab_dl_speed", "Latausnopeus: ")


    ##_________________________________________________________
    ##
    ##     Main window (iPodder.xrc)
    ##_________________________________________________________


    
    ## File menu
    add("str_file", "Tiedosto")
    add("str_import_opml", "Tuo virtoja opml:nä...")
    add("str_export_opml", "Vie virtoja opml:nä...")
    add("str_preferences_menubar", "Asetukset...")
    add("str_close_window", "Sulje ikkuna")
    add("str_quit", "Lopeta")

    add("str_edit", "Muokkaa")
    add("str_select_all", "Valitse kaikki")

    add("str_tools", "Työkalut")
    add("str_check_all", "Tarkista kaikki")
    add("str_catch_up", "Ota kiinni")
    add("str_check_selected", "Tarkista valitut")
    add("str_add_feed", "Lisää virta...")
    add("str_remove_selected", "Poista virta")
    add("str_feed_properties", "Virran ominaisuudet...")
    add("str_scheduler_menubar", "Ajastin...")
    
    add("str_select_language", "Valitse kieli")

    ## these are also used for the tabs
    add("str_view", "Näkymä")
    add("str_downloads", "Lataukset")
    add("str_subscriptions", "Tilatut virrat")
    add("str_podcast_directory", "Podcast-hakemisto")
    add("str_cleanup", "Siivoa")

    add("str_help", "Ohje")
    add("str_online_help", "Online-ohje")
    add("str_faq", "UKK")
    add("str_check_for_update", "Tarkista päivitystarve...")
    add("str_report_a_problem", "Raportoi ongelma")
    add("str_goto_website", "Siirry kotisivulle")
    add("str_make_donation", "Tee lahjoitus")
    add("str_menu_license", "Lisenssi...")
    add("str_about", "Tietoja...")


    ## Downloadstab Toolbar
    add("str_remove_selected_items", "Poista valitut")
    add("str_cancel_selected_download", "Keskeytä valittu lataus")
    add("str_pause_selected", "Pidä tauko valituissa")

    ## Downloadstab States (in columns)
    ## Enclosure states. Use str_dl_state_ prefix to avoid collisions with
    ## other strings, e.g. str_downloading above which isn't capitalized.
    add("str_dl_state_new", "Uusi")
    add("str_dl_state_queued", "Jonossa")
    add("str_dl_state_downloading", "Lataa")
    add("str_dl_state_downloaded", "Ladattu")
    add("str_dl_state_cancelled", "Keskeytetty")
    add("str_dl_state_finished", "Valmis")
    add("str_dl_state_partial", "Osittain ladattu")
    add("str_dl_state_clearing", "Poistaa")


    ## Subscriptionstab Toolbar
    add("str_check_for_new_podcasts", "Tarkista podcastit")
    add("str_catch_up_mode", "Ota kiinni - Lataa vain viimeisimmät uudet tilaukset")

    add("str_add_new_feed", "Lisää uusi virta");
    add("str_remove_selected_feed", "Poista valittu virta")
    add("str_properties", "Ominaisuudet")
    add("str_check_selected_feed", "Tarkista valittu virta")

    add("str_scheduler_on", "Ajastin - päällä")
    add("str_scheduler_off", "Ajastin - poissa päältä")        

    ## Subscriptionstab Scheduler information
    add("str_next_run:", "Seuraava tarkistus:")

    ## Subscriptionstab episode frame
    add("str_downloading_episode_info", "Lataa tietoa jaksosta...")
    add("str_no_episodes_found", "Jaksoja ei löytynyt.")


    ## Directorytab Toolbar
    add("str_refresh", "Päivitä")
    add("str_open_all_folders", "Avaa kaikki kansiot")
    add("str_close_all_folders", "Sulje kaikki kansiot")
    add("str_add", "Lisää")

    ## Directorytab Other items
    add("str_directory_description", "Klikkaa virtaa puukuvaimessa tai kirjoita/liitä virta yllä olevaan laatikkoon ja paina Lisää.")




    ## Cleanuptab items
    add("str_select_a_feed", "Valitse virta")
    add("str_refresh_cleanup", "Päivitä")
    
    add("str_look_in", "Etsi jaksoja:")        
    add("str_player_library", "Soittimen kirjastosta")
    add("str_downloads_folder", "Latauskansiosta")
    add("str_delete_library_entries", "Poista kirjastomerkinnät")
    add("str_delete_files", "Poista tiedostot")
    add("str_select_all_cleanup", "Valitse kaikki")
    add("str_delete", "Poista")




    ## Logtab items
    add("str_log", "Loki")
    add("str_clear", "Tyhjennä")


    ## Columns (in downloads- and subscriptionstab)
    add("str_lst_name", "Nimi")
    add("str_lst_date", "Päivämäärä")        
    add("str_lst_progress", "Edistys")
    add("str_lst_state", "Tila")
    add("str_lst_mb", "Mt")
    add("str_lst_location", "Sijainti")
    add("str_lst_episode", "Jakso")
    add("str_lst_playlist", "Soittolista")

    ## Feed subscription states -- see ipodder/feeds.py SUB_STATES variable
    add("str_subscribed", "Tilattu")
    add("str_disabled", "Estetty")
    add("str_newly-subscribed", "Viime aikoina tilattu")
    add("str_unsubscribed", "Tilaus peruutettu")
    add("str_preview", "Esikatsele")
    add("str_force", "Pakota")
    





    ##_________________________________________________________
    ##
    ##   Dialog Windows
    ##_________________________________________________________



    ## OPML Import Dialog
    #--- Valitse tuotava tiedosto

    ## OPML Export Dialog
    add("str_choose_name_export_file", "Valitse nimi vientitiedostolle")
    add("str_subs_exported", "Tilatut virrat viety.")
    
    ## Preferences Dialog
    add("str_preferences", "Asetukset")
    
    add("str_save", "Tallenna")
    add("str_cancel", "Keskeytä")
    
    # General
    add("str_general", "Yleistä")
    add("str_gen_options_expl", "%s:in yleiset asetukset" % PRODUCT_NAME)
    add("str_hide_on_startup", "Näytä %s vain tehtäväpalkissa käynnistyttyä" % PRODUCT_NAME)

    add("str_run_check_startup", "Tarkista uudet podcastit käynnistyksen yhteydessä")
    add("str_play_after_download", "Toista lataukset heti lataamisen jälkeen")
    add("str_location_and_storage", "Sijainnin ja arkistoinnin määritykset")
    add("str_stop_downloading", "Lopeta lataaminen kun levyllä on enää tilaa:")
    add("str_bad_megabyte_limit_1", "Megatavurajaa ei voi lukea")
    add("str_bad_megabyte_limit_2", "Yritä uudestaan.")

    add("str_download_folder", "Lataa podcastit tähän kansioon")
    add("str_browse", "Selaa...")
    add("str_bad_directory_pref_1", "Kirjoittamaasi kansiota ei löydy")
    add("str_bad_directory_pref_2", "Luo se ja yritä uudestaan.")

    
    # Threading
    add("str_threads", "Säikeistys")
    add("str_multiple_download", "Usean päällekkäisen latauksen asetukset")
    add("str_max_feedscans", "maksimimäärä säikeitä virtojen etsimiseen sessiota kohden")
    add("str_max_downloads", "maksimimäärä latauksia sessiota kohden")
   
    # Network settings
    add("str_networking", "Verkkoasetukset")
    add("str_coralize_urls", "Koralisoi URL:it (kokeilu)")
    add("str_proxy_server", "Käytä välityspalvelinta")
    add("str_proxy_address", "Osoite")
    add("str_proxy_port", "Portte")
    add("str_proxy_username", "Käyttäjänimi")
    add("str_proxy_password", "Salasana")
    add("str_bad_proxy_pref", "Sallit välityspalvelintuen, mutta et antanut palvelimen osoitetta ja porttia.  Palaa Verkkoasetuksiin ja anna proxyn osoite sekä portti.")

    # Player
    add("str_player", "Soitin")
    add("str_choose_a_player", "Valitse soitin")
    add("str_no_player", "Ei soitinta")
    
    # Advanced
    add("str_advanced", "Erityisasetukset")
    add("str_options_power_users", "Nämä asetukset on tarkoitettu tehokäyttäjille")
    add("str_run_command_download", "Suorita tämä komento jokaisen latauksen jälkeen")
    add("str_rcmd_full_path", "%f = Ladatun tiedoston koko polku")
    add("str_rcmd_podcast_name", "%n = Podcastin nimi")
    add("str_rcmd_episode_title", "%e = Jakson otsikko")
    add("str_other_advanced_options", "Muita erityisasetuksia")
    add("str_show_log", "Näytä lokipalkki ohjelmassa")



    ## Feed Dialog (add/properties)
    add("str_title", "Otsikko")
    add("str_url", "Osoite")
    add("str_goto_subs", "Mene Tilausikkunaan nähdäksesi tämän virran jaksot")
    add("str_feed_save", "Tallenna")
    add("str_feed_cancel", "Peruuta")




    ## Scheduler Dialog
    add("str_enable_scheduler", "Salli ajastin")
    add("str_sched_select_type", "Valitse alla olevista painikkeista, haluatko ohjelman tekevän tarkistuksen asetettuna aikana, vai säännöllisesti:")
    add("str_check_at_specific_times", "Tarkista asetettuina aikoina")
    add("str_check_at_regular_intervals", "Tarkista säännöllisin väliajoin")
    add("str_repeat_every:", "Toista joka:")
    add("str_latest_run", "Viimeisin suoritus:")
    add("str_next_run", "Seuraava suoritus:")
    add("str_not_yet", "Ei vielä")
    #--- Cancel
    add("str_save_and_close", "Tallenna ja sulje")
    #--- Save

    add("str_time_error", "Yksi annetuista ajoista ei ole luettavissa. Ohjelma ymmärtää kellonaikoja muodossa: 10:02am tai 16:43.")


    ## Donations Dialog
    #--- Lahjoita iPodderille
    #--- On tärkeää pitää yhteisön omistamia iPodder-ohjelmia verkossa ja pitää yllä sananvapautta tässä uudessa tavassa kuluttaa mediaa . Mikä tahansa rahasumma tekee työryhmän onnelliseksi ja rohkaisee heitä työskentelemään uusien ominaisuuksien ja palvelujen parissa!
    #--- Kyllä, siirry lahjoitussivulle!
    #--- Minun pitää vielä tutustua paremmin, näytä tämä ilmoitus uudestaan kahden viikon kuluttua
    #--- Olen jo lahjoittanut, älä näytä tätä enää
    #--- Ei, en halua lahjoittaa, älä koskaan näytä tätä ilmoitusta enää
    #--- Ei nyt, ilmoita uudestaan päivän kuluttua
    #--- OK




    ## About Dialog
    #--- Versio:
    #--- Ohjelmointi: Erik de Jonge, Andrew Grumet, Garth Kidd, Perica Zivkovic\nSuunnittelu: Martijn Venrooy\nSisältöstrategisti: Mark Alexander Posth\nKonsepti: Adam Curry, Dave Winer\nKiitoksia kaikille kääntäjille!\n\nPerustuu Feedparser- ja BitTorrent-teknologiaan.\nTämä ohjelma on ilmainen ja vapaa; voit levittää ja/tai muokata sitä GNU General Public License:ssä määrätyllä tavalla, jonka on julkaissut Free Software Foundation; joko lisensiin version 2, tai (valintasi mukaan) uudemman version mukaan. Tätä ohjelmaa levitetään siinä toivossa, että se olisi hyödyllinen, mutta ilman minkäänlaista takuuta; ei edes takuuta sen sopivuudesta tiettyyn tarkoitukseen. \n\nLue GNU General Public License jos haluat lisätietoja.




    ## Statusbar items
    add("str_check_for_new_podcast_button", "Tarkista uudet podcastit painamalla vihreää tarkistuspainiketta")
    add("str_last_check", "Viimeisin tarkistus suoritettu aikaan")
    add("str_of", ":sta")
    add("str_item", "kohde")
    add("str_items", "kohdetta")
    add("str_downloading", "lataa")
    add("str_downloaded", "ladattu")
    add("str_enclosure", "sisälytettyä")
    add("str_enclosures", "sisällytetyt")
    add("str_fetched", "haetut")
    add("str_loading_mediaplayer", "Lataa mediasoitinta...")
    add("str_loaded_mediaplayer", "Mediasoitin ladattu...")        
    add("str_initialized", "%s valmis" % PRODUCT_NAME)




    ## Other application strings
    add("str_ipodder_title", PRODUCT_NAME + " - Podcast-vastaanotin v" + __version__)
    add("str_localization_restart", "Kaikkien toimintojen kääntymiseen tarvitaan ohjelman uudelleenkäynnistys. Paina OK sammuttaaksesi ohjelman, paina Peruuta keskeyttääksesi.")
    add("str_really_quit", "Lataus on kesken.  Poistutaanko silti?");
    add("str_double_check", "Näyttää kuin lataus olisi jo käynnissä.");
    
    # check for update
    add("str_new_version_ipodder", "Uusi versio %s:ista on saatavilla, paina Ok siirtyäksesi lataussivulle." % PRODUCT_NAME)
    add("str_no_new_version_ipodder", "Tämä versio %sista on ajan tasalla." % PRODUCT_NAME)
    add("str_other_copy_running", "Toinen kopio %sista on auki. Valitse se, odota sen valmistumista, tai lopeta se." % PRODUCT_NAME)

    # Windows taskbar right-click menu
    add("str_check_now", "Tarkista nyt")        
    add("str_open_ipodder", "Avaa %s" % PRODUCT_NAME)
    #--- Downloading
    add("str_scanning_feeds", "Tarkistaa virtoja")

    # Feed right-click menu
    add("str_remove", "Poista")        
    add("str_open_in_browser", "Avaa selaimessa")
    
    

    # Downloads right-click menu
    add("str_play_episode", "Toista jakso mediasoittimessa")
    add("str_clear_selected", "Poista valitut")
    
