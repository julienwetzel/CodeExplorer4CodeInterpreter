[![en](https://img.shields.io/badge/lang-en-blue.svg)](https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/blob/main/README.md)
[![fr](https://img.shields.io/badge/lang-fr-beige.svg)](https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/blob/main/README.fr.md)
[![es](https://img.shields.io/badge/lang-es-yellow.svg)](https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/blob/main/README.es.md)
[![cmn](https://img.shields.io/badge/lang-cmn-red.svg)](https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/blob/main/README.cmn.md)

# CodeExplorer4CodeInterpreter

CodeExplorer4CodeInterpreter est un logiciel développé en Python conçu pour faciliter l'envoi de plusieurs documents au Code Interpreter de ChatGPT et permettre une interaction aisée avec celui-ci.

<div style="display:flex;">
  <img src="https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/assets/1897591/3f675698-96fd-45d3-96fb-b2033411ebd1" alt="Image 1" width="49%">
  <img src="https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/assets/1897591/9444f225-31ed-4b2a-b1ba-d61161a2087a" alt="Image 2" width="49%">
</div>

## Cas d'utilisation

- **Analyse de projets de code informatique** : CodeExplorer4CodeInterpreter peut être utilisé pour transmettre l'ensemble d'un projet de code informatique au Code Interpreter de ChatGPT. Cela permet aux développeurs de poser des questions sur leur code, d'obtenir des suggestions, des explications ou des corrections potentielles, facilitant ainsi le processus de développement.
- **Analyse de journaux et de publications** : Le logiciel peut également être utilisé pour transmettre plusieurs journaux et publications scientifiques au Code Interpreter de ChatGPT. Les utilisateurs peuvent poser des questions spécifiques sur des articles, demander des résumés ou des analyses supplémentaires, ou obtenir des explications approfondies sur des concepts complexes.
- **Assistance à la rédaction et à la correction** : CodeExplorer4CodeInterpreter peut être utile aux écrivains et aux étudiants pour transmettre des documents tels que des essais, des rapports ou des travaux académiques au Code Interpreter de ChatGPT. Ils peuvent demander des conseils sur la structure, la grammaire, l'amélioration du style d'écriture ou même des suggestions de mots-clés pertinents.
- **Analyse de données** : Le logiciel peut être utilisé pour transmettre des ensembles de données au Code Interpreter de ChatGPT. Les utilisateurs peuvent poser des questions sur les données, obtenir des visualisations, des statistiques ou des recommandations sur les méthodes d'analyse à appliquer.
- **Aide à la recherche d'informations** : Le logiciel peut faciliter la recherche d'informations en transmettant des documents contenant des informations spécifiques au Code Interpreter de ChatGPT. Les utilisateurs peuvent poser des questions sur des sujets variés et obtenir des réponses détaillées basées sur le contenu des documents transmis.

## Fonctionnalités

- CodeExplorer4CodeInterpreter prend en charge Python 3.7 et versions ultérieures, assurant ainsi la compatibilité avec la plupart des environnements Python modernes.
- Permet d'explorer facilement la base de code d'un projet.
- Génère un script Python qui peut être facilement importé et utilisé dans le plugin ChatGPT Code Interpreter.

## Prérequis

Avant d'exécuter CodeExplorer4CodeInterpreter, assurez-vous d'avoir le module `gitignore_parser` installé dans votre environnement Python. Vous pouvez l'installer à l'aide de pip :

```bash
pip install gitignore-parser
```

## Premiers pas

Pour commencer avec CodeExplorer4CodeInterpreter, vous devez avoir Python 3.7 ou une version supérieure installée sur votre système.

Clonez le dépôt en utilisant la commande suivante :
```bash
git clone https://github.com/julienwetzel/CodeExplorer4CodeInterpreter.git
```

Accédez au répertoire cloné :
```bash
cd CodeExplorer4CodeInterpreter
```

Pour générer le script Python contenant le code de votre projet, exécutez la commande suivante :
```bash
python ce4ci.py [project_dir] [output_file]
```

où `[project_dir]` est le répertoire de votre projet et `[output_file]` est le nom du fichier à générer.

Par exemple :
```bash
python ce4ci.py ./ ../../data/ce4ci_dict.py
```

Après avoir exécuté la commande, vous verrez un résumé de l'opération :
```bash
----------------------------------------------------
Total files processed: 5
Total directories processed: 0
Total file contents inserted: 3
Total files ignored due to .gitignore rules: 2
Total files skipped because they are not Unicode: 0
----------------------------------------------------
```
## Utilisation avec le plugin ChatGPT Code Interpreter

Une fois que le script Python est généré, vous pouvez l'utiliser avec le plugin Code Interpreter de ChatGPT.

Dans le prompt ChatGPT, ajoutez le texte suivant :

```bash
All the contents of the project files are in the attached python file.
Import the file with /mnt/data/ce4ci_dict.py and simply run the display_file_content(file_path)
function where file_path is the path of the file. For example, `display_file_content('/your/file.example')
To display the list of all project files, use the get_available_file_paths() function.
```

> Note : `ce4ci_dict.py` est le nom du fichier généré qui a été téléchargé dans le plugin Code Interpreter de ChatGPT. Si `/mnt/data` n'est pas inclus, le fichier ne sera pas trouvé.

## Exploration du dictionnaire Python généré

Pour explorer le dictionnaire Python généré, vous pouvez utiliser le script `ce4ci_print.py`.

Pour afficher le contenu du dictionnaire Python, utilisez la commande suivante :
```bash
python ce4ci_print.py [--list] <script_path> [<file_path>]
```
Par exemple :
```bash
python ce4ci_print.py ../../data/ce4ci_dict.py '/LICENSE'
```
Cela affichera le contenu du fichier LICENSE.

Pour lister les chemins de tous les fichiers contenus dans le dictionnaire, utilisez la commande suivante :
```bash
python ce4ci_print.py ../../data/ce4ci_dict.py --list
```
Cela affichera tous les chemins de fichiers disponibles.

## Licence

Ce projet est sous licence MIT - consultez le fichier [LICENSE.md](https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/blob/main/LICENSE.md) pour plus de détails.
