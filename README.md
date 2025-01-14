# MembersMap

L'objectif est de ce module : montrer sur une carte le nombre d'adhérents
d'un département, commune par commune et arrondissement par arrondissement
pour les villes de Lyon, Marseille et Paris.

Notes :

* Les scripts traitent des données anonymisées.
* Actuellement, le fichier des adhérents débarassé des champs « sensibles »
  (nom, prénom, numéros de téléphone, profession…)
  doit être au format `CSV`.
* Seuls les champs « Adhésion active ? », « Ville » et « Code postal » sont
  utilisés dans le traitement des données. Il n'est cependant pas nécessaire
  de purger le fichier des adhérents de tous les champs non utilisés dans
  le traitement (ils sont tout simplement ignorés).

## auteurs

* [Xavier Schoepfer](mailto:xavier.schoepfer@xs-net.ninja)

## licence

* GNU General Public License v3
* Coryright (c) 2024, Pace publique, Xavier Schoepfer
