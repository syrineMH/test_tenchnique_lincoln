# test_tenchnique_lincoln
## Partie 1:

Le projet est constitué des repertoires suivantes :

1-bin : contient le script qui contient le pipeline demandé.

2-data: contient les data (output+Input)

3-sources : contient les modules et les classes du projet

4-tests : contient les tests unitaires

5-utils : contient les fonctions utile, réutilisable sur les fichiers et les dataframes.

6-un fichier config.py qui contient un les variables de configuration du projet.

7-un repertoire .github/workflows  qui contient un fichier 
python-app.yml pour vérifier l'exactitude du nouveau code avant son intégration

8-SQL : contient deux fichiers. Chaque fichier présente la réponse de la requete SQL demandée.

9-un fichier requirement pour installer tous les dépendencies nécessaire au fonctionnement 
du projet.

Le point d'entrée est le fichier bin.py du répertoire bin, qui permet de déclencher 
le data pipeline de génération du json qui contient les relations des 
drugs avec les journaux et les pubmed et les clinicals trials. Le pipeline exécute les traitements suivants :

1-data_preparation:


 Cette tache contient :
 La collecte des données :(collecter les path pour chaque source).

 Le prétraitement des données : (qualité des fichiers, caster les données au type approprié,
 enlever les lignes qui contiennent des valeurs vides ou Nan)

La preparation des données : retourne le path de d'un seul fichier csv pour chaque source. Ce fichier 
contient l'intégralité des données pré-traitées
et prètes pour le traitement 


1-data_traitement: 

La classe Mentions contient l'intégralité de traitement sur les données.
Cette classe contient un traitement spécifique pour chaque source ce qui permet de retirer à part pour d'autre besoin chaque 
partie du traitement indépendament.

Le module data traitement appele la classe Mentions, cree le fichier résultat et  retourne le path de ce fichier json.

Le module ad hoc feature n'appartient pas au pipeline.
Ce module lit le fichier résultat json et retourne le journal qui a mentionné plus de drugs
### Améliorations possibles :


* gérer les exceptions

* Data processing :

1- J'ai remarqué des erreurs d'encodage dans les données.

2-Pour les lignes qui possédent des données manquantes, j'ai procédé par éliminer ces valeurs mais je pense
que corriger ces données est une meilleure solution pour éviter le risque
de perte d'information.

## Partie 2: Pour aller plus loin

Pour pouvoir traiter des grosses volumétries des données, on peut envisager les améliorations suivantes :

* migrer vers un environement big data ou Cloud pour pouvoir stocker des données de grandes volumétries.

* Utiliser un calcul parallèle (framework spark (pyspark)).

* utiliser des outils cloud manager pour les exécutions des étapes de workflow.


## Partie 3: SQL
#### Requete 1:

Cette requête se base à appliquer une simple agrégation pour calculer le chiffre d'affaires
(somme(prix multiplié par le nombre des produits vendus) en groupant par date.

``` 
SELECT date,sum(prod_price*prod_qty) as Ventes
FROM Transaction
WHERE date BETWEEN "2019-01-01" AND "2019-12-31"
GROUP BY date; 
```
#### Requete 2:
Cette requête utilise les commandes CASE pour pouvoir pivoter les résultats d'agrégations sur une subquery. La subquery fait une  jointure avec la table PRODUCT_NOMENCLATURE et calcul le chiffre d'affaires 
en groupant par (client id,product id)
```
SELECT client_id,
       sum(case when product_type="MEUBLE" then transaction_amount else 0 end) AS ventes_meuble,
       sum(case when product_type="DECO" then transaction_amount else 0 end) AS ventes_deco


FROM ( Select client_id,product_type,sum(prod_price * prod_qty) as 'transaction_amount'
FROM Transaction
LEFT JOIN PRODUCT_NOMENCLATURE ON Transaction.prod_id = PRODUCT_NOMENCLATURE.prod_id
WHERE date BETWEEN "2020-01-01" AND "2020-12-31"
GROUP BY client_id,product_type ) AS X
GROUP BY X.client_id
```