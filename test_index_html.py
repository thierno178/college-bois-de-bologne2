import os

def test_file_exists():
    assert os.path.exists("index.html"), "index.html est manquant!"

def test_contains_nom_etudiant():
    with open("index.html", "r") as file:
        content = file.read()
        assert "<span id=\"nom_etudiant\">" in content, "Le champ nom_etudiant est manquant!"

test_file_exists()
test_contains_nom_etudiant()