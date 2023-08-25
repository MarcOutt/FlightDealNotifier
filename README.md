# Flight Deal Notifier

Flight Deal Notifier est un programme Python qui vous aide à rechercher et surveiller des offres de vols à bas prix vers différentes destinations. Le programme utilise des données de vols et d'itinéraires pour chercher des vols abordables et envoie des notifications par e-mail (ou SMS) lorsque des offres intéressantes sont trouvées.

## Fonctionnalités

- Utilise le service Flight Search pour obtenir les données de vols et les informations sur les destinations.
- Stocke les informations sensibles dans un fichier `private_infos.py` qui n'est pas suivi par Git.
- Utilise le fichier `.gitignore` pour exclure les fichiers sensibles et les détails de connexion de votre dépôt Git.
- Utilise la classe `NotificationManager` pour créer et envoyer des notifications par e-mail.
- Permet de spécifier des critères tels que les prix de vol maximum pour déclencher des notifications.
- Organise les données de destinations et les codes IATA dans une classe `DataManager`.
- Effectue une recherche de vols pour les destinations spécifiées dans les données.
- Vérifie les prix des vols et envoie des notifications en fonction des critères définis.

## Démarrage

1. Clonez le dépôt sur votre machine locale.
2. Configurez vos informations sensibles dans `private_infos.py`. Consultez `private_infos_example.py` pour la structure requise.
3. Installez les dépendances requises en exécutant `pip install -r requirements.txt`.
4. Exécutez le script principal pour commencer à surveiller les offres de vols.

## Utilisation

Le programme peut être exécuté périodiquement pour surveiller les offres de vols et vous notifier lorsque des vols abordables sont trouvés pour les destinations spécifiées. Configurez simplement les paramètres dans `private_infos.py`, exécutez le script et attendez les notifications.

## Contributions

Les contributions sont les bienvenues ! Si vous avez des suggestions ou des améliorations, n'hésitez pas à soumettre une pull request.

---

Profitez de la recherche de superbes offres de vols et bon voyage !
