# LVIA GUINEE

L'application de gestion des points de lectures dans les différentes communes de la guinée

## Processus de travail avec le projet

1. Télécharger le projet à l'aide des commandes ci-après: 
   ````
   git clone https://github.com/Altgras/lviaguinee.git
   
   ````
2. Une fois Téléchargé, assurez vous que git,python soient installé
3. Ensuite naviguez jusqu'à la racine du projet
4. Créer une branche portant le nom de la tâche que vous êtes en train d'effectuer à l'aide de la cmde:
   ````
   git checkout -b nom_de_votre_branche
   ````
5. Après modification d'une tâche au sein du projet, ajouter votre changement à l'aide de la cmde: 
  ````
  git add .
  git commit -m "votre message illustrant votre changement"
  ````
6. Vous pouvez vérifier l'état des changements à tout moment à l'aide de la cmde: 
  ````
  git status
  ````
7. Si vous souhaitez remonter vos changements pour qu'on puisse les examiner, tapez la cmde: 
  ````
  git push origin nom_de_votre_branche
  ````
  * NB: Assurez vous d'avoir toujours effectué un "commit" avant de faire un "push"
8. Après avoir remonté les changements, créer un "Pull Request" dépuis l'interface graphique
9. Pour basculer d'une branche à une autre, on tape la cmd ci-après:
````
git checkout nom_branche
````
