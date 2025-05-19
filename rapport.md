Rapport TP_Pipeline 19/05/2025

1. Objectif :
Mettre en place un pipeline CI/CD avec tests automatiques.

2. Fonction :
La fonction divide(a, b) permet de diviser deux nombres. Elle renvoie une erreur si on divise par zéro.

3. Tests :
Trois tests unitaires :
    Cas normal
    Cas négatif
    Cas d'erreur (division par zéro)

4. Pipeline CI/CD :
Utilisation de GitHub Actions pour lancer automatiquement les tests à chaque push ou pull_request.

5. Simulation de bug :
J’ai supprimé la sécurité, ce qui a fait échouer le test.
Après correction, les tests passent à nouveau.

6. Couverture de tests :
Ajout de pytest-cov pour vérifier que toutes les lignes de code sont bien testées.

7. Questions de réflexion :

Pourquoi les tests dans le pipeline ?
->Pour détecter les bugs dès qu’on modifie le code.

Avantages de l’automatisation ?
->Gain de temps, moins d’erreurs humaines, tests toujours faits.

Améliorer la couverture ?
->Ajouter plus de cas (valeurs nulles, très grandes, types non numériques…).

Outils choisis ?
->GitHub Actions car gratuit et intégré à GitHub.

