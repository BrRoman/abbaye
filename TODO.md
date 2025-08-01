# GÉNÉRAL:
- Accueil : "Vous êtes (n'êtes pas) connecté comme…" / Login / Signup.
- Page de login : ajouter signup.
- User: Préférences:
  - Affichage liste/calendrier.
  - Recevoir mail fêtes moines ("la veille", "le jour même", "jamais").
- Boutons "Annuler" : ajouter une flèche gauche avant le mot "Annuler".
- Everywhere in the site: when create and update, put an "else:" corresponding to the "if request.method == 'POST':" before "form = …".
- Pagination (datatables trop lourdes et lentes) pour hôtellerie, séjours etc. Inutile pour des petits tableaux.


# AGENDA:
- Calendrier.
- Fetcher les retraites et leurs nombres dans la page du P. Savio.
- Empêcher date_to < date_from.
- On change date_from: date_to = date_from.
- Après validation d'un événement : renvoyer sur la semaine de l'événement (pas la semaine en cours).


# HÔTELLERIE:
- Jours de promenades, retraites.
- Séjour : dans le formulaire, mettre tous les repas avec cases à cocher, pour pouvoir décliquer les repas sautés au cas par cas. (Autre solution : un formset de date + repas ?)
- Un laïc (Personne "non-prêtre") ne devrait pas pouvoir célébrer (case "Prêtre avec Messe" dans la fiche Séjour).


# IMPRIMERIE:
- "Ajouter…" (client, projet etc.) : bouton à mettre en haut.
- Générer devis PDF.
- Générer BL PDF.
- Suivi projet de A à Z.


# LIVRETS:
## Option "3 jours" ne fonctionne pas: parce qu'il attend 5 jours? à cause du formset? (suppr. de 2 forms)
## Vérifier lectures propres pour les Abbés (saint Antoine au moins ne semble pas fait).
## Lectures Ste Famille année C.
## Cendres: antiennes ad lotionem pedum.
## Dimanches, solennités, Cendres etc.: homélie.
## Carême:
- *Oratio super populum*.
- Commémoraisons (Stes Perpétue et Félicité etc.).
- Cendres (et autres ?): Prière universelle.
## Pour les livrets "full":
- P. Vianney:
    • Lettrine au début et à chaque division de psaume (si possible) à Tierce
    • Oraison du jour sur une seule page
    • Je mettrai aussi une lettrine au début de chaque oraison
    • Dans les partitions, les accents ne sont pas nécessaire pour les mots de 2 syllabes (si possible)
    • Toujours dans les partitions: i à la place du j
    • Lettrine au début du canon
    • Quand il y a des V/. et R/. la deuxième ligne devrait être en retrait (si possible), cf. p. 2, 18, 20
    • Enlever la rubrique en bas de la page 20.
- P. Louis;
    • Par esprit de contradiction, je n’ai pas de correction importante, mais seulement de détail (ma spécialité est plutôt dans le filtrage du moucheron): on ne met pas deux-points en fin de ligne dans un titre (par ex. « Antienne d’Introït : »). Et pour la lecture et l’évangile, je mettrais plutôt comme dans un missel « Lecture de la lettre de saint Paul Apôtre aux Éphésiens »… Bon, évidemment, vous allez trouver ça compliqué!
    • Dans la partition du « Per ipsum », PER devrait être en capitales.


# MÉMO:
## Installation:
### Raccourcis clavier:
VirtualBox WindowsXP
virtualbox VirtualBox\ VMs/WindowsXP/WindowsXP.vbox
### Installation avec aptitude hors-proxy:
aptitude -o Acquire::http::proxy=false install […]


## HTML:
Rediriger d'une page html vers une autre:
Dans le <head>:
<meta http-equiv="refresh" content="0; url=http://example.com/" />


# MOINES:
- Models: check dates are consistent (birthday < entry < habit etc.).
- Details: modal.


# ORDOMATIC:
- Créer des tests Python.
- Ordos 2011 et 2038 à voir : pb 3e samedi de juin.
- Ordo 2007 : bug.
- Anniv. professions etc.
- Oraison Ste Famille.
- Vigiles Ste Vierge le samedi, attribution intelligente des numéros, pour éviter 4e = 5e.
- Ste Famille : Bizarre, il semble qu'il y ait eu à une époque (2015 au moins) des lectures entièrement différentes pour chaque année.
- ordo_write.py : commentaire Rogations : Code + propre. Il y a 4 cas : vigile = juste "Ben", festum = rien, mémoires mineures = juste "Magnif", et de ea pas vigiles = les 2. TODO : le cas "les 2" n'a pas été testé (pas d'occurrence en 2014). TODO : 2015 problème : veille de l'Ascension = mémoire mineure.
- Sancto : saint Grégoire de Nysse (10/01) : Tirer au clair cette histoire de report à après le Baptême.
- Saint Benoît dimanche : tester que le bon dimanche s'affiche (per annum, post pentec.).
- Présentation dimanche : tester que le bon dimanche s'affiche pour la forme extraordinaire (Septuagésime, etc.).
- ND Mont-Carmel samedi.
- Transfiguration dimanche : il y a des Ières Vêpres, et de plus on calcule quel dimanche (per annum, post Pentecosten).
- Assomption dimanche : vérifier que bon dimanche (per annum, post Pentecosten, dim. d'août).
- Toussaint dimanche : vérifier que bon dimanche (per annum, post Pentecosten, dim. de nov).
- Vérifier les samedis, avec les lectures mariales aux Vigiles. Attention: si le 16/07 tombe un samedi, ce n'est pas la peine (cf. Sancto à ce jour).
- Féries entre Octave de Noël et Baptême: if new_day_date.day == 7 and new_day_date.weekday() != 6: # TODO: Dans quels cas omet-on les "generalities", et dans quels cas les modifie-t-on ?
- Féries per annum : new_day["generalities"] = ("\n\\newpage\n\\ApplyParBox{1cm}{\\ApplyGenerTitleHuge{Tempus Per annum}}\n\\ApplyGenerSubTitle{in Ofﬁcio :}\n\\ApplyGenerList{\n\\item In feriis : hebdomada I per annum vel I post Epiphaniam.}\n\\ApplyGenerSubTitle{ad mensam :}\n\\ApplyGenerList{\n\\item Benedictio de tempore per annum.}" + lectiones_body + "\n\\ApplyGenerList{\n\\item Præfatio communis I, nisi aliter notetur.}\n\\medskip") if i == 0 and j == 0 else "" # TODO : Body = Vigiles… + "in MC : lectiones feriales" à la 1ère férie libre. Pourquoi pas dans le generalities ?
- Texte spécial pour le 3e samedi de juin, s'il tombe avant la Trinité… :) TODO : Ce cas (rarissime) n'a pas encore été testé. functions/tempo.py-new_day["body"] = "\n\\item Ad Vigilias : lectio sabbato 3 (in supplemento 202).\n\\item In MC : Beatæ Mariæ Virginis, Matris et mediatricis gratiæ (CM 30) ; præfatio I de Beata Maria Virgine."
- Remplacer partout les tabulations par 4 espaces.
- Semailles = 1ère férie libre avant l'Ascension (descendre du lundi au mercredi). Récoltes = semaine avant 3e dim. de Septembre (4 temps de sept.) : mercredi ou vendredi, sinon lundi, mardi ou jeudi.
- Fêtes mobiles de l'année suivante à la fin de l'ordo.
- 1er samedi du mois de janvier : in ML avant in MC (7/1/2017 par ex.).
- Octave de Pentecôte : calculer et modifier toutes les mc_bmv (dans various).
- Saint Boniface : 3 cas : TP, entre Pent. et Trin., après Trinité. 2e cas, ajouter cette mention pour les Vigiles : "Ad Vigilias: post lectionem dicitur Responsorium *Iste sanctus*, e Communi Martyris extra Tempus Paschale post primam lectionem I Nocturni."
- Automatiser le report d'un jour de jeûne au lendemain si festum.
- Page de garde: variante "évidée" de la même police.
- 9 janvier 2021: ajouter «- in ML: Missa de sancta Maria in sabbato.
- Pour les fêtes, il me semblerait plus léger de ne mettre en petites capitales que le nom du saint (e.g. S. Bernardi), en laissant son titre en romain (e.g. abbatis et Ecclesiæ doctoris): comme pour les mémoires majeures, mais en gras.
- Alterner 1 année sur 2 saint Clément et saint Colomban :
    \ApplyHeader{\textbf{23} & Feria III - \textsc{S. Columbani}, abbatis - \textbf{memoria maior} - \textit{Alb.}}
    \ApplyBody{
        \item In Officio~: oratio in supplemento 193*.
        \item Ad Vigilias~: lectio in supplemento 193*.
        \item \textit{in ML~: Missa pro abbate.}
        \item In MC~: collecta in MP~; Commune sanctorum et sanctarum (MR 958)~; præfatio de sanctis virginibus et religiosis.}
- Il faudrait que les abréviations utilisées pour les livres bibliques correspondent avec la table donnée en p. 4 (par exemple Io et non pas Jn).

I. Sanctoral
• 6 août (2022) : la Transfiguration, fête du Seigneur, prime sur le dimanche, donc « Vesperæ festi ».
• 17 septembre (années impaires) : à la ligne du Benedictus, il manque une espace « tono III g »

II. Temporal
• Mettre l’oraison des mercredi et vendredi des Quatre-Temps de l’Avent aussi aux vêpres avant le 17 décembre (comme indiqué dans le bréviaire, p. 62 et 65 : « Oratio Præsta / Excita, quæ dicitur ad omnes Horas, etiam ad Vesperas »).

III. Généralités
• Tons des antiennes : espace insécable entre le mode et la différence (III g)
• Indiquer les commémoraisons à faire (ML) : Avent et Carême
• Bénédiction solennelle pour les solennités : ajouter à MC une rubrique « Missa concluditur benedictione sollemni. »
    ◦ 1 er dimanche de l’Avent
    ◦ Noël (Messe de la nuit + Messe du jour)
    ◦ 1 er janvier
    ◦ Épiphanie
    ◦ Pâques (Vigile + Messe du jour)
    ◦ Ascension
    ◦ Pentecôte
    ◦ 29 juin : saints Pierre et Paul
    ◦ 15 août, 8 décembre : B. V. M.
    ◦ Toussaint
• Insérer deux variantes : Flavigny/Solignac
• Carême (MC) :
    ◦ Mercredi des Cendres et vendredis de carême : Canon à genoux

Le Père Abbé Antoine me signale une petite erreur de référence dans l’Ordo, pour le samedi de la 27ᵉ semaine TO années impaires: Ioel 4, 12-21 au lieu de Ioel 3, 12-21.

Sainte Thérèse 15/10 : simplifier les hymnes: Ad vigilias, Laudes et Vesperas: Hymni proprii. Ensuite il n'y a plus qu'à préciser les ant. de Ben. et Magn.

Pour les commémoraisons en Avent et en Carême, il faudrait trouver une solution… Idem pour le cas où les Quatre-Temps tombent un 23 septembre, par exemple: comme saint Pio est une mémoire obligatoire, la commémoraison est in-dis-pen-sable.

Début novembre : "lectio *de memoria*" à affiner (ça peut être avant les lectures SO, du coup inutile de préciser "de memoria").

Saint Bénigne à refondre.

Après les corrections 2022, il reste encore quelques moucherons :
Page 96 (8 septembre), il manque une espace avant la parenthèse: «II(pro».
Page 85 (24 juillet), c’est la préface I du dimanche (et non pas la VIII) pour le XVIIᵉ dimanche per annum.
    Idem page 98 (18 septembre), préface I pour le XXVᵉ dimanche per annum.
    Idem page 112 (13 novembre), préface I pour le XXXIIIᵉ dimanche per annum.
Page 112 (lundi 14 novembre): MC pour les bienfaiteurs défunts (collision avec les antiennes spéciales Ben. et Magn. ?).

Baptême : refondre.

7/1 : Inverser ML/MC.
2/2 : He (pas Hebr (?)), et Lc en gras.

Pour l’évangile de ce lundi notre ordo indique Jn 8, 12-20.
Or, pour les années C, le lectionnaire dit de lire cet évangile lorsque l’évangile de la femme adultère (Jn 8, 1-11) a été lu le dimanche précédent ; donc, lorsque celui-ci n’a pas été lu le dimanche (ce qui est notre cas puisque on a lu celui de l’année A), il faut le lire le lundi.
En conclusion, l’évangile de ce lundi devrait être Jn 8, 1-11.

2022 : saint Bède : "in Officio et in ML": supprimer.

P. Jean Pouchet : "Pour simplifier, il faudrait distinguer entre Fête-Dieu le 24 (avec Saint-Jean-Baptiste le 25) et Sacré-Cœur le 24 (avec Saint-Jean-Baptiste le 23)…"

3e Messe des défunts (septembre): il semble que la référence de l'Évangile ait changé (Jo).

11 juin (2038) : la Saint-Barnabé tombe pendant le temps pascal…

Vérifier le bon comportement "vigile Pentecôte" et "infra octavam Pentecostes" (y compris "4 Temps", y compris "samedi brevior") des saints suivants:
11/5
13/5
15/5
18/5
19/5
25/5
26/5
27/5
30/5
31/5
1/6
2/6
3/6
5/6
9/6
11/6
13/6
19/6

Antiennes du XXIVe dim. ap. la Pentecôte : jamais avant le Christ-Roi. Comme cela ne se produira pas avant plusieurs années, je surseois !

23 décembre : si vendredi : Ant. Benedictus p. 231 et non 220 (plus naturel), dans la mesure où c'est la même.

Præfatio II de BMV à mettre plus souvent ?

Annonciation reportée (2024) : les Vêpres disparaissent (tant les 1ères que les 2e).

Ste Famille : pourquoi jamais les leçons du IIIe Nocturne ? Si confirmation : ne pas préciser "I et II Noct." lors des années paires.

Commémoraison des saints durant le Carême : préciser dans quel Commun chercher le verset.

St Jérôme Émilien : préciser qu'on prend le Trait au Commun des Confesseurs.

P. Irénée _17_ février.

24 juin : saint Jean-Baptiste : "Vesperæ solemnitatis" ??? (2024)
Préface propre Mater Ecclesiæ?

Lectures propres Pentecôte années B et C?

Visitation (31/05): Ad Vigilias: in supplemento 122; invitatorium proprium in supplemento 58 (seulement quand le 31 mai tombe avant la Trinité)
Supprimer "In ML: Missa in PAL; præfatio de sanctis."

Office de saints Maur et Placide : prendre répons, hymne et verset du commun de plusieurs confesseurs (5 octobre) sauf hymne de saint Maur

2024: Messe du samedi des 4 Temps de septembre (III Septembris) décalée par erreur à la IVe semaine de septembre en 2024 (dû à saint Matthieu ?).

Faire la chasse aux ant. de Benedictus et Magnificat inutilement indiquées car tirées du Commun.

Annonciation : le report à Pâques + 8 ne fonctionne pas (2027).

Césures : pas moins de 2 lettres.

Problème du "Quatuor": enlever la queue. Ou changer de police ?

Dominica VII Paschæ: inutile de préciser R. et hymne aux Vêpres, dans la mesure où c'est déjà dit plus haut ("office férial et dominical").

Saint Joseph 1er mai: oraison: 1 fois.

Ordinaire Ascension.

Abbés Cluny: Apoc => Ap (?).

24/6 (2023 ? 2024 ? 2025 ?): "Vesperae solemnitatis" ?

Sainte Famille: préciser dès samedi soir: "Oratio…"

Dom. II post Nativ.: -supprimer "et vesperas" si 5 janvier - "Post I Noct. Resp. IV" ? ou celui du jour.

St Nom de Jésus: inutile de précier (2e Vêpres 2025).

7/1: inutile de préciser "in MC: lectiones feriales": déjà dit 2 fois!


# POLYGLOTTE:
- Table de correspondance des versets.
