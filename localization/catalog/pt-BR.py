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
    ## Traducao realizada Colaborativamente por podcasters brasileiros
    #############################################

    ##_________________________________________________________
    ##
    ##     New strings
    ##_________________________________________________________

    add("str_critical_error_minspace_exceeded", \
        "Download parado; espaço livre (%dMB) " \
        "é menor que o min de %dMB.  Libere espaço em disco " \
        "Utilizando a ferramenta Limpeza ou ajustando " \
        "os valores de gerenciamento nas Preferências")
    add("str_critical_error_unknown", "Erro crítico desconhecido no download.")

    add("str_error_checking_new_version", "Lamentamos, mas houve um erro ao verificar por novas versões. Tente novamente mais tarde.")
    add("str_hours", "horas")
    add("str_minutes", "minutos")

   # The next 4 are for the status bar updates during the initial scan.
    add("str_scanning", "Examinando")
    add("str_scanned", "Examinado")
    add("str_feed", "feed")
    add("str_feeds", "feeds")

    add("str_downloading_new_episodes", "Baixar novos episódios")
    add("str_sched_specific", "Checar por um horário específico")
    add("str_sched_reg", "Checar por um intervalo regular")
    add("str_repeat_every", "Repetir sempre")
    add("str_next_run_label", "Próxima ação:")

    add("str_license", "Este programa é um programa desenvolvido em Software Livre; você pode redistribuir e/ou modifica-lo conforme os termos da licença GNU Public License publicada pela Free Software Foundation; também pela versão 2 da Licença, ou (em sua opção) qualquer versão posterior. Este programa é distribuído na esperança que será útil, mas sem nenhuma garantia; também sem a garantia imposta de mercadabilidade ou de encaixe em algum propósito específico. \n\nPor favor, leia a licença GNU General Public License para maiores detalhes.")

    add("str_donate", "Doações para %s" % PRODUCT_NAME)
    add("str_donate_expl", "É importante para manter os programas e aplicações %s mantido pela comunidade e online e também para manter esse novo modo de consumo de informação livre como no discurso. Qualquer quantia de dinheiro irá fazer a equipe mais feliz além de encorajá-los para continuar trabalhando em novos serviços e melhorias!" % PRODUCT_NAME)
    add("str_donate_yes", "Sim, leve-me a página de doações agora!")
    add("str_donate_two_weeks", "Ainda quero dar mais uma olhada, mostre-me isso em 2 semanas")
    add("str_donate_already", "Eu já fiz minha parte, não mostre este diálogo novamente")
    add("str_donate_no", "Não, eu não quero doar, nunca mais me mostre essa mensagem denovo")
    add("str_donate_one_day", "Não agora, tente novamente amanhã")
    add("str_donate_proceed", "Proceda")

    add("str_scheduler_dialog", "Agendamento")
    add("str_scheduler_tab", "Configurações")

    add("str_select_import_file", "Selecionar arquivo para importar")
    add("str_add_feed_dialog", "Adicionar um Feed")
    add("str_edit_feed", "Feed propriedades")

    add("str_really_delete", "Apagar realmente")

    add("str_license_caption", "Licença")

    add("str_ep_downloaded", "Baixado")
    add("str_ep_skipped_removed_other", "Pulado/Removido/OutroFeed")
    add("str_dl_state_to_download", "Para baixar")

    add("str_select_none_cleanup", "Selecionar nenhum")
    add("str_submit_lang", "Enviar um Idioma")
    add("str_dltab_live", "Baixando agora: ")
    add("str_dltab_ul_speed", "Velocidade de envio: ")
    add("str_dltab_dl_speed", "Velocidade de recebimento: ")



    ##_________________________________________________________
    ##
    ##     Main window (iPodder.xrc)
    ##_________________________________________________________



    ## File menu
    add("str_file", "Arquivo")
    add("str_import_opml", "Importar feeds de opml...")
    add("str_export_opml", "Exportar feeds como opml...")
    add("str_preferences_menubar", "Preferências...")
    add("str_close_window", "Fechar Janela")
    add("str_quit", "Sair")

    add("str_edit", "Editar")
    add("str_select_all", "Selecionar tudo")

    add("str_tools", "Ferramentas")
    add("str_check_all", "Verificar tudo")
    add("str_catch_up", "Pegar tudo")
    add("str_check_selected", "Verificar selecionado")
    add("str_add_feed", "Adicionar um Feed...")
    add("str_remove_selected", "Apagar Feed")
    add("str_feed_properties", "Propriedades Feed...")
    add("str_scheduler_menubar", "Agendamento...")

    add("str_select_language", "Selecionar Idioma")

    ## these are also used for the tabs
    add("str_view", "Visualizar")
    add("str_downloads", "Downloads")
    add("str_subscriptions", "Assinaturas")
    add("str_podcast_directory", "Diretório Podcast")
    add("str_cleanup", "Limpeza")

    add("str_help", "Ajuda")
    add("str_online_help", "Ajuda Online")
    add("str_faq", "FAQ")
    add("str_check_for_update", "Verificar Atualização...")
    add("str_report_a_problem", "Reportar um problema")
    add("str_goto_website", "Ir para o Website")
    add("str_make_donation", "Fazer uma Doação")
    add("str_menu_license", "Licença...")
    add("str_about", "Sobre...")


    ## Downloadstab Toolbar
    add("str_remove_selected_items", "Remover ítens selecionados")
    add("str_cancel_selected_download", "Cancelar downloads selecionados")
    add("str_pause_selected", "Pausar seleção")

    ## Downloadstab States (em colunas)
    ## Enclosure states. Use str_dl_state_ prefix to avoid collisions with
    ## other strings, e.g. str_downloading above which isn't capitalized.
    add("str_dl_state_new", "Novo")
    add("str_dl_state_queued", "Na fila")
    add("str_dl_state_downloading", "Baixando")
    add("str_dl_state_downloaded", "Baixado")
    add("str_dl_state_cancelled", "Cancelado")
    add("str_dl_state_finished", "Finalizado")
    add("str_dl_state_partial", "Parcialmente baixado")
    add("str_dl_state_clearing", "Limpando")


    ## Subscriptionstab Toolbar
    add("str_check_for_new_podcasts", "Procurar por novos podcasts")
    add("str_catch_up_mode", "Pegar - Baixar somente as novas assinaturas")

    add("str_add_new_feed", "Adicionar novo feed");
    add("str_remove_selected_feed", "Apagar feed selecionado")
    add("str_properties", "Propriedades")
    add("str_check_selected_feed", "Checar feed selecionado")

    add("str_scheduler_on", "Agendamento - Ligado")
    add("str_scheduler_off", "Agendamento - Desligado")

    ## Subscriptionstab Scheduler information
    add("str_next_run:", "Próxima ação:")

    ## Subscriptionstab episode frame
    add("str_downloading_episode_info", "Baixando informações sobre episódios...")
    add("str_no_episodes_found", "Nenhum episódio encontrado.")


    ## Directorytab Toolbar
    add("str_refresh", "Atualizar")
    add("str_open_all_folders", "Abrir todos as pastas")
    add("str_close_all_folders", "Fechar todas as pastas")
    add("str_add", "Adicionar")

    ## Directorytab Other items
    add("str_directory_description", "Clique em um feed na árvore ou digite/cole no espaço acima e clique em Adicionar.")




    ## Cleanuptab items
    add("str_select_a_feed", "Selecionar um feed")
    add("str_refresh_cleanup", "Atualizar")

    add("str_look_in", "Procurar por epísódios em")
    add("str_player_library", "Biblioteca do Tocador")
    add("str_downloads_folder", "Diretório de download")
    add("str_delete_library_entries", "Apagar entradas da biblioteca")
    add("str_delete_files", "Apagar arquivos")
    add("str_select_all_cleanup", "Selecionar tudo")
    add("str_delete", "Apagar")




    ## Logtab items
    add("str_log", "Log")
    add("str_clear", "Limpar")


    ## Columns (in downloads- and subscriptionstab)
    add("str_lst_name", "Nome")
    add("str_lst_date", "Data")
    add("str_lst_progress", "Progresso")
    add("str_lst_state", "Estado")
    add("str_lst_mb", "MB")
    add("str_lst_location", "Localização")
    add("str_lst_episode", "Episódio")
    add("str_lst_playlist", "Playlist")

    ##Feed subscription states -- see ipodder/feeds.py SUB_STATES variable
    add("str_subscribed", "Assinado")
    add("str_disabled", "Desabilitado")
    add("str_newly-subscribed", "Novas Postagens")
    add("str_unsubscribed", "Assinatura Cancelada")
    add("str_preview", "Prever")
    add("str_force", "Forçar")






    ##_________________________________________________________
    ##
    ##   Dialog Windows
    ##_________________________________________________________



    ## OPML Import Dialog
    #--- Select import file

    ## OPML Export Dialog
    add("str_choose_name_export_file", "Escolha um nome para exportar o arquivo")
    add("str_subs_exported", "Assinaturas exportadas")

    ## Preferences Dialog
    add("str_preferences", "Preferências")

    add("str_save", "Salvar")
    add("str_cancel", "Cancelar")

    ## General
    add("str_general", "Geral")
    add("str_gen_options_expl", "Ajusta as opções gerais para o programa %s" % PRODUCT_NAME)
    add("str_hide_on_startup", "Ao íniciar mostre somente o %s no systray" % PRODUCT_NAME)

    add("str_run_check_startup", "Verificar por novos podcasts quando iniciado")
    add("str_play_after_download", "Tocar os podcasts assim que terminado o download")
    add("str_location_and_storage", "Gerenciamento de local e armazanagem")
    add("str_stop_downloading", "Parar downloads se o disco rígido alcançar um mínimo de")
    add("str_bad_megabyte_limit_1", "O valor deve ser inteiro")
    add("str_bad_megabyte_limit_2", "Por favor tente novamente.")

    add("str_download_folder", "Salvar os podcasts nesta pasta")
    add("str_browse", "Browse")
    add("str_bad_directory_pref_1", "Não foi possível encontrar o diretório que específicou")
    add("str_bad_directory_pref_2", "Crie-o e tente novamente.")


    ## Threading
    add("str_threads", "Downloads Multplos")
    add("str_multiple_download", "Configurações de downloads mltiplos")
    add("str_max_feedscans", "threads maximos por sesso")
    add("str_max_downloads", "Mximo de Downloads por sessão")

    ## Network settings
    add("str_networking", "Configurações de Rede")
    add("str_coralize_urls", "Coralizar URLs (experimental)")
    add("str_proxy_server", "Usar um servidor proxy")
    add("str_proxy_address", "Endereço")
    add("str_proxy_port", "Porta")
    add("str_proxy_username", "Nome de usuário")
    add("str_proxy_password", "Senha")
    add("str_bad_proxy_pref", "Você habilitou o suporte a proxy, mas não definiu um proxy e uma porta.  Volte as oprções de de Rede e defina um host de proxy e uma porta.")

    ## Player
    add("str_player", "Player")
    add("str_choose_a_player", "Escolha um player")
    add("str_no_player", "Nenhum player")

   # Advanced
    add("str_advanced", "Avançado")
    add("str_options_power_users", "Estas opções podem ser utilizadas por usuários experientes")
    add("str_run_command_download", "Rode este comando após cada download")
    add("str_rcmd_full_path", "%f = Caminho completo para o arquivo baixado")
    add("str_rcmd_podcast_name", "%n = Nome do Podcast")
    add("str_other_advanced_options", "Outras opções avançadas")
    add("str_show_log", "Mostra aba de log no programa")



    ## Feed Dialog (add/properties)
    add("str_title", "Título")
    add("str_url", "URL")
    add("str_goto_subs", "Vá para a aba de assinaturas para ver os episódios")
    add("str_feed_save", "Salvar")
    add("str_feed_cancel", "Cancelar")




    ## Scheduler Dialog
    add("str_enable_scheduler", "Habilitar agendamento")
    add("str_sched_select_type", "Selecione os botões abaixo para checar em hora específica ou periodicamente:")
    add("str_check_at_specific_times", "Checar nestes horários específicos")
    add("str_check_at_regular_intervals", "Checar em intervalos regulares")
    add("str_repeat_every:", "Repetir sempre:")
    add("str_latest_run", "Ultima vez rodado:")
    add("str_next_run", "Próxima vez:")
    add("str_not_yet", "Ainda não")
    #--- Cancel
    add("str_save_and_close", "Salvar e fechar")
    #--- Save

    add("str_time_error", "Um dos horários definidos não parece correto. Horários válidos devem ser assim: 10:02am, 16:43.")


    ## Donations Dialog
    #--- Doar para o iPodder
    #--- É muito importante para manter o  iPodder e suas aplicações online e não-comerciais e para manter este novo modelo de consumo de media livre. Qualquer quantia de dinheiro irá tornar a equipe mais feliz e encorajá-los no trabalho e desenvolvimento de melhorias!
    #--- Sim, leve a página de doaçoes agora!
    #--- Quero dar mais uma olhada antes, me mostre isso em duas semanas
    #--- Eu ja fiz minha parte, não mostre este diálogo novamente
    #--- Não, eu não quero doar nada, e não mostre este diálogo novamente
    #--- Não agora, tente novamente amanhã
    #--- OK




    ## About Dialog
    #--- Versão:
    #--- Programação: Erik de Jonge, Andrew Grumet, Garth Kidd, Perica Zivkovic\nDesign: Martijn Venrooy\nEstrategista de Conteúdo: Mark Alexander Posth\nConceito: Adam Curry, Dave Winer\nAgradecemos a todos os tradutores por suas contribuíções!\n\nBaseado em um Feedparser e na tecnologia BitTorrent.\nEste programa é Software Livre; você pode re-distribuí-lo e/ou modificá-lo sob os termos da Licença GNU General Public License como publicada pela FSF - Free Software Foundation; também sob a licença 2, ou (em sua opção) qualquer versão posterior. Este programa é distribuído na esperança que será útil, mas sem nenhuma garantia; mesmo sem a garantia de mercadabilidade ou de encaixe em algum propósito específico. \n\nVeja a GNU General Public License para mais detalhes.




    ## Statusbar items
    add("str_check_for_new_podcast_button", "Procure por novos podcasts clicando no botão verde")
    add("str_last_check", "Ultima verificação feita em ")
    add("str_of", "de")
    add("str_item", "[ítem")
    add("str_items", "ítens")
    add("str_downloading", "baixando")
    add("str_downloaded", "baixado")
    add("str_enclosure", "embutido")
    add("str_enclosures", "embutidos")
    add("str_fetched", "pego")
    add("str_loading_mediaplayer", "Carregando seu tocador...")
    add("str_loaded_mediaplayer", "Tocador carregado...")
    add("str_initialized", "%s aguardando" % PRODUCT_NAME)




    ## Other application strings
    add("str_ipodder_title", PRODUCT_NAME + " - Podcast receiver v" + __version__)
    add("str_localization_restart", "É necessário que o %s seja re-iniciado. Clique Ok para terminar de forma limpa, cancelar para continuar." % PRODUCT_NAME)
    add("str_really_quit", "Um download está sendo realizado. Quer mesmo sair?");
    add("str_double_check", "Um arquivo está sendo baixado.");

    ## check for update
    add("str_new_version_ipodder", "Uma nova versão do %s esta disponível, clique em  Ok e acesso o site de download." % PRODUCT_NAME)
    add("str_no_new_version_ipodder", "Esta versão é a mais recente")
    add("str_other_copy_running", "Outra cópia do %s está rodando. Pare-a, espere até estar completo, ou mate-a." % PRODUCT_NAME)

    # Windows taskbar right-click menu
    add("str_check_now", "Checar Agora")
    add("str_open_ipodder", "Abrir %s" % PRODUCT_NAME)
    #--- Downloading
    add("str_scanning_feeds", "Procurar feeds")

    # Feed right-click menu
    add("str_remove", "Remover")
    add("str_open_in_browser", "Abrir no navegador")



    ## Downloads right-click menu
    add("str_play_episode", "Tocar episódio no seu tocador")
    add("str_clear_selected", "Limpar ítems selecionados")
