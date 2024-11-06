# Assignment 03
![git-graph](https://github.com/user-attachments/assets/3ce2ba30-baa0-4c3d-9259-4c54830b0263)

## Commands on Visualizing Git
# Git-Übung - Visualisierung und Befehlsdokumentation

## 1. Erstellte Branches:
- `head-servant`
- `servant1`
- `servant2`
- `servant3`
- `trainee`
- `test_servant`

## 2. Wichtige Git-Kommandos:

### Branches erstellen:
```bash
git checkout -b head-servant
git checkout -b servant1
git checkout -b servant2
git checkout -b servant3
git checkout -b trainee
```

## Branches committen:
```bash
git checkout head-servant
git commit -m "branch head-servant erstellt"
git checkout servant1
git commit -m "branch servant unterliegt dem head-servant"
git checkout servant2
git commit -m "branch servant2 unterliegt dem head-servant"
git checkout servant3
git commit -m "branch servant3 unterliegt dem head-servant"
git checkout master
git commit -m "branch master ist der HEAD der Operation"
```

## Tags hinzufügen:
```bash
git checkout master
git tag head_of_operation
git checkout head-servant
git tag in_charge_of_the_servants
git checkout servant1
git tag executes_tasks_given_by_head-servant
git checkout servant2
git tag executes_tasks_given_by_head-servant
git checkout servant3
git tag last_remaining_servant
```
## Merging:
```bash
git checkout master
git merge servant2
git checkout master
git merge servant1
git checkout master
git merge servant3
git checkout master
git merge trainee
```
## Tag für den Testbranch:
```bash
git checkout test_servant
git commit -m "Test commit"
git tag test_visual
```



