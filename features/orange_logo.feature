Feature: Validation logo
  En tant qu'admin je veux ouvrir l'application Orange sur Chrome
  alors le Logo s'affiche sur la page d'acceuil

  Scenario: Presence du logo sur page d acceuil
    When j'ouvre l'application Orange
    Then le Logo s'affiche sur la page d'acceuil
