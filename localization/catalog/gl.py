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
       "Descarga cancelada; espazo ceibe %dMB menor " \
       "do mínimo %dMB.  Libera espazo no " \
       "teu disco usando Limpeza ou axustando as opcións " \
       "de almacenamento en Preferenzas")
   add("str_critical_error_unknown", "Erro crítico descoñecido mentres descargaba.")

   add("str_error_checking_new_version", "Lamentámolo, aconteceu un erro cando comprobaba se existe unha nova versión. Por favor, téntao máis tarde.")
   add("str_hours", "horas")
   add("str_minutes", "minutos")

   # The next 4 are for the status bar updates during the initial scan.
   add("str_scanning", "Revisando")
   add("str_scanned", "Revisado")
   add("str_feed", "orixe")
   add("str_feeds", "orixes")

   add("str_downloading_new_episodes", "Descargando novos episodios")
   add("str_sched_specific", "Revisar a horas estabelecidas")
   add("str_sched_reg", "Revisar a intervalos regulares")
   add("str_repeat_every", "Repetir cada")
   add("str_next_run_label", "Seguinte revisión:")

   add("str_license", "Este programa é software ceibe; podes redistribuilo e/ou modificalo baixo os termos da licenza GNU (General Public License) publicada pola Free Software Foundation; aplícase a versión 2 da Licenza, ou calquera versión posterior. Este programa distribuese coa intención de que resulte útil, mais sin ningunha garantía; incluso sin garantía implícita de comerciabilidade ou adecuación a un propósito determinado. \n\nOlla a GNU General Public License para máis detalles.")

   add("str_donate", "Donativo a %s" % PRODUCT_NAME)
   add("str_donate_expl", "É importante preservar o esprito comunitario, aberto e público de %s e mante-lo xeito de acceso a este novo medio de comunicación ceibe. Calquera cantidade de diñeiro aledará á equipa de desenrolo e animaraos a traballar en novas prestacións e servizos!" % PRODUCT_NAME)
   add("str_donate_yes", "Sí, lévame á páxina de donacións agora!")
   add("str_donate_two_weeks", "Teño que cavilar un chisco máis, lémbramo outra volta dentro dun par de semanas")
   add("str_donate_already", "Xa fixen a miña donación, non amoses este aviso outra vez")
   add("str_donate_no", "Non, non desexo donar nada e tampouco quero que me avises máis")
   add("str_donate_one_day", "Agora non, lémbramo mañá")
   add("str_donate_proceed", "Proceder")

   add("str_scheduler_dialog", "Programador")
   add("str_scheduler_tab", "Preferenzas")

   add("str_select_import_file", "Selecionar arquivo a importar")
   add("str_add_feed_dialog", "Engadir unha Orixe")
   add("str_edit_feed", "Propiedades da Orixe")

   add("str_really_delete", "Eliminar definitivamente")

   add("str_license_caption", "Licenza")

   add("str_ep_downloaded", "Descargados")
   add("str_ep_skipped_removed_other", "Cancelado/Eliminado/OutraOrixe")
   add("str_dl_state_to_download", "Para descargar")

   add("str_select_none_cleanup", "Cancelar seleción")
   add("str_submit_lang", "Enviar unha linguaxe")

   add("str_dltab_live", "Descargas activas: ")
   add("str_dltab_ul_speed", "Velocidade de subida: ")
   add("str_dltab_dl_speed", "Velocidade de descarga: ")

   ##_________________________________________________________
   ##
   ##     Main window (iPodder.xrc)
   ##_________________________________________________________

   ## File menu
   add("str_file", "Arquivo")
   add("str_import_opml", "Importar Orixes dende opml...")
   add("str_export_opml", "Exportar Orixes como opml...")
   add("str_preferences_menubar", "Preferenzas...")
   add("str_close_window", "Pechar xanela")
   add("str_quit", "Saír")

   add("str_edit", "Edición")
   add("str_select_all", "Selecionar todos")

   add("str_tools", "Ferramentas")
   add("str_check_all", "Revisar todos")
   add("str_catch_up", "Capturar")
   add("str_check_selected", "Revisar selecionados")
   add("str_add_feed", "Engadir Orixe...")
   add("str_remove_selected", "Eliminar Orixe")
   add("str_feed_properties", "Propiedades da Orixe...")
   add("str_scheduler_menubar", "Programador...")

   add("str_select_language", "Trocar idioma")

   ## these are also used for the tabs
   add("str_view", "Ver")
   add("str_downloads", "Descargas")
   add("str_subscriptions", "Subscripcións")
   add("str_podcast_directory", "Directorio de Podcast")
   add("str_cleanup", "Limpeza")

   add("str_help", "Axuda")
   add("str_online_help", "Axuda Online")
   add("str_faq", "FAQ")
   add("str_check_for_update", "Procurar Actualizacións...")
   add("str_report_a_problem", "Informar dun problema")
   add("str_goto_website", "Ir ao website")
   add("str_make_donation", "Facer un donativo")
   add("str_menu_license", "Licenza...")
   add("str_about", "Acerca de...")

   ## Downloadstab Toolbar
   add("str_remove_selected_items", "Eliminar elementos selecionados")
   add("str_cancel_selected_download", "Cancelar descarga")
   add("str_pause_selected", "Pausar selecionados")

   ## Downloadstab States (in columns)
   ## Enclosure states. Use str_dl_state_ prefix to avoid collisions with
   ## other strings, e.g. str_downloading above which isn't capitalized.
   add("str_dl_state_new", "Novo")
   add("str_dl_state_queued", "En cola")
   add("str_dl_state_downloading", "Descargando...")
   add("str_dl_state_downloaded", "Descargado")
   add("str_dl_state_cancelled", "Cancelado")
   add("str_dl_state_finished", "Rematado")
   add("str_dl_state_partial", "Descargado parcialmente")
   add("str_dl_state_clearing", "Limpado")

   ## Subscriptionstab Toolbar
   add("str_check_for_new_podcasts", "Revisar novos podcasts")
   add("str_catch_up_mode", "Capturar - Só descarga as últimas subscripcións")

   add("str_add_new_feed", "Engadir nova orixe");
   add("str_remove_selected_feed", "Eliminar orixe selecionada")
   add("str_properties", "Propiedades")
   add("str_check_selected_feed", "Revisar orixe")

   add("str_scheduler_on", "Programador - On")
   add("str_scheduler_off", "Programador - Off")

   ## Subscriptionstab Scheduler information
   add("str_next_run:", "Seguinte revisión:")

   ## Subscriptionstab episode frame
   add("str_downloading_episode_info", "Descargando info do episodio...")
   add("str_no_episodes_found", "Non se atoparon episodios.")

   ## Directorytab Toolbar
   add("str_refresh", "Actualizar")
   add("str_open_all_folders", "Expandir cartafoles")
   add("str_close_all_folders", "Contraer cartafoles")
   add("str_add", "Engadir")

   ## Directorytab Other items
   add("str_directory_description", "Preme nunha Orixe na árbore, ou teclea/pega na liña de arriba e dalle a Engadir.")

   ## Cleanuptab items
   add("str_select_a_feed", "Seleciona unha Orixe")
   add("str_refresh_cleanup", "Actualizar")

   add("str_look_in", "Procurar episodios en")
   add("str_player_library", "Biblioteca do Reproductor")
   add("str_downloads_folder", "Cartafol de descargas")
   add("str_delete_library_entries", "Eliminar entradas da Biblioteca")
   add("str_delete_files", "Eliminar arquivos")
   add("str_select_all_cleanup", "Selecionar todos")
   add("str_delete", "Eliminar")

   ## Logtab items
   add("str_log", "Rexistro")
   add("str_clear", "Limpar")

   ## Columns (in downloads- and subscriptionstab)
   add("str_lst_name", "Nome")
   add("str_lst_date", "Data")
   add("str_lst_progress", "Progreso")
   add("str_lst_state", "Estado")
   add("str_lst_mb", "MB")
   add("str_lst_location", "Localización")
   add("str_lst_episode", "Episodio")
   add("str_lst_playlist", "Lista de reproducción")

   ## Feed subscription states -- see ipodder/feeds.py SUB_STATES variable
   add("str_subscribed", "Subscrito")
   add("str_disabled", "Desactivado")
   add("str_newly-subscribed", "Recén subscrito")
   add("str_unsubscribed", "Subscripción anulada")
   add("str_preview", "Previsualizar")
   add("str_force", "Forzar")

   ##_________________________________________________________
   ##
   ##   Dialog Windows
   ##_________________________________________________________

   ## OPML Import Dialog
   #--- Select import file

   ## OPML Export Dialog
   add("str_choose_name_export_file", "Elixe un nome para o arquivo a exportar")
   add("str_subs_exported", "Subscripcións exportadas.")

   ## Preferences Dialog
   add("str_preferences", "Preferenzas")

   add("str_save", "Gardar")
   add("str_cancel", "Cancelar")

   # General
   add("str_general", "Xerais")
   add("str_gen_options_expl", "Establece as opcións xerais de %s" % PRODUCT_NAME)
   add("str_hide_on_startup", "Ao iniciar amosar %s unicamente na Bandexa do Sistema" % PRODUCT_NAME)

   add("str_run_check_startup", "Revisar se hai novos podcasts cando se inicia a aplicación")
   add("str_play_after_download", "Reproducir podcasts xusto ao rematar de descargar")
   add("str_location_and_storage", "Opcións de ubicación e almacenamento")
   add("str_stop_downloading", "Adiar as descargas se o espazo en disco diminúe por debaixo de")
   add("str_bad_megabyte_limit_1", "Laméntoo, o límite de megas non semella ser un número enteiro")
   add("str_bad_megabyte_limit_2", "Por favor, téntao de novo.")

   add("str_download_folder", "Descargar podcasts neste cartafol")
   add("str_browse", "Examinar")
   add("str_bad_directory_pref_1", "Laméntoo, non son quen de atopar o cartafol introducido")
   add("str_bad_directory_pref_2", "Por favor, crea o cartafol e téntao de novo.")

   # Threading
   add("str_threads", "Multifíos")
   add("str_multiple_download", "Opcións de descargas múltiples")
   add("str_max_feedscans", "max. de fíos para revisión de orixes por sesión")
   add("str_max_downloads", "max. de descargas por sesión")

   # Network settings
   add("str_networking", "Opcións de Rede")
   add("str_coralize_urls", "Coralizar URL's (experimental)")
   add("str_proxy_server", "Usar un servidor proxy")
   add("str_proxy_address", "Enderezo")
   add("str_proxy_port", "Porto")
   add("str_proxy_username", "Nome de usuario")
   add("str_proxy_password", "Chave")
   add("str_bad_proxy_pref", "Habilitaches o soporte proxy mais non definiches o servidor nin o porto. Por favor volta á pestana das opcións de Rede e introduce a IP e porto do proxy.")

   # Player
   add("str_player", "Reproductor")
   add("str_choose_a_player", "Elixe un reproductor")
   add("str_no_player", "Sin reproductor")

   # Advanced
   add("str_advanced", "Avanzado")
   add("str_options_power_users", "Estas opcións deben ser modificadas por usuarios avanzados")
   add("str_run_command_download", "Executar este comando após cada descarga")
   add("str_rcmd_full_path", "%f = Roteiro completo ao ficheiro descargado")
   add("str_rcmd_podcast_name", "%n = nome do podcast")
   add("str_other_advanced_options", "Outras opcións avanzadas")
   add("str_show_log", "Amosar pestana de Rexistro")

   ## Feed Dialog (add/properties)
   add("str_title", "Título")
   add("str_url", "URL")
   add("str_goto_subs", "Ir á pestana de subscripcións para ve-los episodios desta Orixe")
   add("str_feed_save", "Gardar")
   add("str_feed_cancel", "Cancelar")

   ## Scheduler Dialog
   add("str_enable_scheduler", "Activar Programador")
   add("str_sched_select_type", "Seleciona os botóns para revisar a horas estabelecidas ou a intervalos regulares:")
   add("str_check_at_specific_times", "Revisar a horas estabelecidas")
   add("str_check_at_regular_intervals", "Revisar a intervalos regulares")
   add("str_repeat_every:", "Repetir cada:")
   add("str_latest_run", "Última revisión:")
   add("str_next_run", "Seguinte revisión:")
   add("str_not_yet", "Aínda non")
   #--- Cancel
   add("str_save_and_close", "Gardar e pechar")
   #--- Save

   add("str_time_error", "Unha das horas programadas semella non ser correcta. As horas válidas son do seguinte xeito: 10:02am, 16:43.")

   ## Donations Dialog
   #--- Donativo a iPodder
   #--- É importante preservar o esprito comunitario, aberto e público de iPodder e mante-lo xeito de acceso a este novo medio de comunicación ceibe. Calquera cantidade de diñeiro aledará á equipa de desenrolo e animaraos a traballar en novas prestacións e servizos!
   #--- Sí, lévame á páxina de donacións agora!
   #--- Teño que cavilar un chisco máis, lémbramo outra volta dentro dun par de semanas
   #--- Xa fixen a miña donación, non amoses este aviso outra vez
   #--- Non, non desexo donar nada e tampouco quero que me avises máis
   #--- Agora non, lémbramo mañá
   #--- Proceder

   ## About Dialog
   #--- Versión:
   #--- Programación: Erik de Jonge, Andrew Grumet, Garth Kidd, Perica Zivkovic\nDeseño: Martijn Venrooy\nAnalista de contidos: Mark Alexander Posth\nConcepto: Adam Curry, Dave Winer\nVersión en Galego: Ramiro Rodríguez Suárez\nGrazas a tódolos traductores polas súas comisións!\n\nBaseado nas tecnoloxías Feedparser e BitTorrent.\nEste programa é software ceibe; podes redistribuilo e/ou modificalo baixo os termos da licenza GNU (General Public License) publicada pola Free Software Foundation; aplícase a versión 2 da Licenza, ou calquera versión posterior. Este programa distribuese coa intención de que resulte útil, mais sin ningunha garantía; incluso sin garantía implícita de comerciabilidade ou adecuación a un propósito determinado. \n\nOlla a GNU General Public License para máis detalles.

   ## Statusbar items
   add("str_check_for_new_podcast_button", "Procurar novos podcasts premendo no botón verde")
   add("str_last_check", "Última revisión completada ás")
   add("str_of", "de")
   add("str_item", "elemento")
   add("str_items", "elementos")
   add("str_downloading", "descargando")
   add("str_downloaded", "descargado")
   add("str_enclosure", "ámbito")
   add("str_enclosures", "ámbitos")
   add("str_fetched", "adequiridos")
   add("str_loading_mediaplayer", "Cargando o reproductor...")
   add("str_loaded_mediaplayer", "Cargado o reproductor...")
   add("str_initialized", "%s listo" % PRODUCT_NAME)

   ## Other application strings
   add("str_ipodder_title", PRODUCT_NAME + " - Receptor Podcast v" + __version__)
   add("str_localization_restart", "Para localizar tódolos controis de %s é preciso que reinicies. Preme Ok para reiniciar ou Cancelar para continuar." % PRODUCT_NAME)
   add("str_really_quit", "Descarga en marcha. Queres saír?");
   add("str_double_check", "Semella que aínda hai unha descarga en marcha.");

   # check for update
   add("str_new_version_ipodder", "Está dispoñible unha nova versión de %s, preme Ok para visitar a páxina de descargas." % PRODUCT_NAME)
   add("str_no_new_version_ipodder", "Esta versión de %s está ao día" % PRODUCT_NAME)
   add("str_other_copy_running", "Outra copia de %s está en execución. Por favor, actívaa, agarda a que remate ou péchaa." % PRODUCT_NAME)

   # Windows taskbar right-click menu
   add("str_check_now", "Revisar agora")
   add("str_open_ipodder", "Abrir %s" % PRODUCT_NAME)
   #--- Downloading
   add("str_scanning_feeds", "Revisando orixes")

   # Feed right-click menu
   add("str_remove", "Eliminar")
   add("str_open_in_browser", "Abrir no navegador")

   # Downloads right-click menu
   add("str_play_episode", "Reproducir episodio")
   add("str_clear_selected", "Eliminar elementos selecionados")

