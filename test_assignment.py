# test_assignment.py
import pytest
from assignment import Library, Player, Song, Playlist


# ---------- Test Library ----------
@pytest.mark.parametrize("titles,borrow,expected", [
    (["1984", "The Hobbit"], "1984", "Available books:\nThe Hobbit"),
    (["Dune"], "Dune", "No books available"),
    (["A", "B", "C"], "X", "Available books:\nA\nB\nC"),
])
def test1(titles, borrow, expected):
    lib = Library()
    for t in titles:
        lib.add_book(t)
    lib.borrow_book(borrow)
    assert lib.show_books().strip() == expected.strip()


# ---------- Test Player ----------
@pytest.mark.parametrize("damage,score,expected_health,expected_alive", [
    (30, 50, 70, True),
    (100, 10, 0, False),
    (120, 0, 0, False),
])
def test2(damage, score, expected_health, expected_alive):
    p = Player("John")
    p.take_damage(damage)
    p.add_score(score)
    assert p.health == expected_health
    assert p.is_alive() == expected_alive


# ---------- Test Playlist ----------
def test3():
    s1 = Song("Imagine", "John Lennon", 3.5)
    s2 = Song("Hey Jude", "The Beatles", 4.2)
    pl = Playlist()
    pl.add_song(s1)
    pl.add_song(s2)
    expected = (
        "1. Imagine - John Lennon (3.5 min)\n"
        "2. Hey Jude - The Beatles (4.2 min)\n"
        "Total: 7.7 min"
    )
    assert pl.show_songs().strip() == expected.strip()
    assert pl.total_duration() == pytest.approx(7.7)
