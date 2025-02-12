import logging
import os

class Logger:
    def __init__(self, filename="log.txt"):
        # Vérifier si le dossier logs existe, sinon le créer
        log_dir = os.path.dirname(filename)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        self.logger = logging.getLogger("custom_logger")
        self.logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(filename, encoding="utf-8")  # Ajout de l'encodage UTF-8
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    
    def log(self, level, message):
        if level.lower() == "debug":
            self.logger.debug(message)
        elif level.lower() == "info":
            self.logger.info(message)
        elif level.lower() == "warning":
            self.logger.warning(message)
        elif level.lower() == "error":
            self.logger.error(message)
        elif level.lower() == "critical":
            self.logger.critical(message)



"""if _name_ == "_main_":
    # Création d'une instance du logger
    logger = Logger("app.log")

    # Enregistrement de différents types de logs
    logger.log("debug", "Débogage en cours.")
    logger.log("info", "L'utilisateur s'est connecté avec succès.")
    logger.log("warning", "Tentative de connexion suspecte détectée.")
    logger.log("error", "Échec du paiement, solde insuffisant.")
    logger.log("critical", "Défaillance critique du serveur.")"""