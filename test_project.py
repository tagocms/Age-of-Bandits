import project.project as project
import pytest
import random
from datetime import date


def test_attack_hit():
    random.seed(20)
    assert project.attack_hit(5, 20, 10)["hit"] == True
    random.seed(20)
    assert project.attack_hit(5, 20, 20)["hit"] == False
    random.seed(20)
    assert project.attack_hit(10, 20, 14)["hit"] == True
    random.seed(20)
    assert project.attack_hit(1, 20, 10)["hit"] == False
    random.seed(20)
    assert project.attack_hit(5, 20, 10)["die rolled"] == 5
    random.seed(20)
    assert project.attack_hit(5, 20, 20)["die rolled"] == 5
    random.seed(20)
    assert project.attack_hit(10, 20, 14)["die rolled"] == 5
    random.seed(20)
    assert project.attack_hit(1, 20, 10)["die rolled"] == 5


def test_create_row_leaderboard():
    assert project.create_row_leaderboard("tiago", "Mage", 10)["Player"] == "tiago"
    assert project.create_row_leaderboard("tiago", "Mage", 10)["Vocation"] == "Mage"
    assert project.create_row_leaderboard("tiago", "Mage", 10)["Turns"] == 10
    assert project.create_row_leaderboard("tiago", "Mage", 10)["Date"] == date.today()


def test_validate_vocation():
    assert project.validate_vocation("test") == False
    assert project.validate_vocation("Mage") == True
    assert project.validate_vocation("M") == True
    assert project.validate_vocation("Warrior") == True
    assert project.validate_vocation("War") == False
    assert project.validate_vocation("e") == False


def test_validate_name():
    assert project.validate_name("Test") == True
    assert project.validate_name("Test64") == False
    assert project.validate_name("64") == False
