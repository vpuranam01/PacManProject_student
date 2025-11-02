import pytest
import pygame
from ghost import Ghost
from player import Player

@pytest.fixture
def walls():
    return [pygame.Rect(0, 0, 20, 600), pygame.Rect(780, 0, 20, 600)]

@pytest.fixture
def player():
    return Player(100, 100)

def test_ghost_initialization():
    ghost = Ghost(50, 50, (255, 0, 0))
    assert ghost.x == 50
    assert ghost.y == 50
    assert ghost.color == (255, 0, 0)
    assert ghost.speed == 1
    assert ghost.radius == 10

def test_ghost_moves_without_walls(player):
    ghost = Ghost(50, 50, (255, 0, 0))
    old_x, old_y = ghost.x, ghost.y
    ghost.move([], player)
    assert (ghost.x, ghost.y) != (old_x, old_y)

def test_ghost_wall_collision(player, walls):
    ghost = Ghost(10, 300, (255, 0, 0))
    ghost.direction = "left"
    ghost.move(walls, player)
    # Should not move through wall
    assert ghost.x >= 10
