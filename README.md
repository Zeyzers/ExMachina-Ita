# Documentazione del bot Discord
## Introduzione
Questa documentazione fornisce una panoramica delle funzionalità, della struttura e dell'utilizzo del bot Discord sviluppato per la gestione del server e le interazioni con gli utenti.

## Indice
1. [Introduzione](#introduzione)
2. [Installazione](#installazione)
3. [Uso](#uso)
4. [Gestione degli eventi](#Gestione degli eventi)
5. [Comandi](#comandi)
6. [Utilità](#utilità)
7. [Contributo](#contributo)
8. [Licenza](#licenza)

## Installazione
1. Clonare il repository sul computer locale.
2. Installare i requisiti usando `pip install -r requirements.txt`.
3. Creare un file `.env` nella directory principale e aggiungere il token del bot Discord come `DISCORD_TOKEN=token`.

## Uso
1. Eseguire il bot eseguendo `main.py`.
2. Invitare il bot al proprio server Discord utilizzando l'URL OAuth2 generato dall'applicazione bot nel portale degli sviluppatori Discord.

## Gestione degli eventi
- **on_ready()**: Viene attivato quando il bot si connette a Discord ed è pronto a ricevere eventi. Inizializza lo stato del bot e sincronizza i comandi a ogni gilda.
- **start_typing()**: Funzione per iniziare a digitare nel canale prima di eseguire un comando.
- **stop_typing()**: Funzione per interrompere la digitazione dopo l'esecuzione di un comando.
- **before_invoke()**: Registrazione di `start_typing()` come before_invoke per tutti i comandi.
- **after_invoke()**: Registrazione di `stop_typing()` come after_invoke per tutti i comandi.

## Comandi
Il bot fornisce i seguenti comandi:
- **help**: Visualizza i comandi disponibili e le loro descrizioni.
- **ping**: Fornisce la latenza tra il server e l'API Discord.
- **userinfo**: Visualizza le informazioni su un utente.
- **serverinfo**: Visualizza le informazioni sul server.
- **roll**: Lancia una quantità personalizzata di dadi con un numero personalizzato di facce.
- **kick**: Caccia un utente dal server con un motivo opzionale.
- **ban**: Bandisce un utente dal server con un motivo opzionale.
- **pardon**: Perdona un utente precedentemente bandito dal server.
- **clear**: Cancella una quantità specifica di messaggi dal canale corrente.
- **lockdown**: Blocca o sblocca un canale per limitare o consentire i messaggi degli utenti.
- **rolereact**: Imposta le reazioni ai ruoli ad un messaggio per consentire agli utenti di autoassegnarsi i ruoli reagendo.
- **tempvoice**: Crea canali vocali temporanei che vengono eliminati automaticamente dopo un periodo di inattività.

## Utilità
- `generate_help_message(ctx)`: Genera un messaggio embed contenente informazioni di aiuto per i comandi.
- `__sync_commands_to_guild()`: Funzione per inviare tutti i comandi a tutte le gilde.

## Contribuire
I contributi sono benvenuti! Se avete idee per nuove funzionalità o miglioramenti, sentitevi liberi di aprire un problema o di inviare una richiesta di pull.

## Licenza
Questo progetto è rilasciato sotto licenza [MIT License](LICENSE).
