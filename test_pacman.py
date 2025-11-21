import pytest
import pygame
from pacman import Pacman
from ghost import Ghost


@pytest.fixture
def pacman():
    return Pacman(100, 100)


@pytest.fixture
def walls():
    return [
        pygame.Rect(0, 0, 20, 600),  # Left wall
        pygame.Rect(200, 200, 20, 20),  # Small obstacle
        pygame.Rect(780, 0, 20, 600),  # Right wall
    ]


def test_pacman_initialization(pacman):
    assert pacman.x == 100
    assert pacman.y == 100
    assert pacman.direction == "right"
    assert pacman.speed == 2
    assert pacman.radius == 10


def test_pacman_movement_no_walls(pacman):
    initial_x = pacman.x
    initial_y = pacman.y

    pacman.move("right", [])
    assert pacman.x == initial_x + pacman.speed
    assert pacman.y == initial_y
    assert pacman.direction == "right"

    pacman.move("left", [])
    assert pacman.x == initial_x
    assert pacman.y == initial_y
    assert pacman.direction == "left"


def test_pacman_wall_collision(pacman, walls):
    # Move towards left wall
    pacman.x = 25
    pacman.y = 100
    pacman.move("left", walls)
    assert pacman.x == 25  # Should not move through wall

    # Move towards obstacle
    pacman.x = 190
    pacman.y = 210
    pacman.move("right", walls)
    assert pacman.x == 190  # Should not move through obstacle


"""
UNCOMMENT and FILL THIS IN
"""


def test_pacman_movement_with_obstacles(pacman, walls):
    # Step 1: Move pacman towards an obstacle (left wall)
    pacman.x = 25
    pacman.y = 100
    pacman.move("left", walls)
    assert pacman.x == 25  # Should not move through the left wall

    # Step 2: Move pacman towards an obstacle (small obstacle at (200, 200))
    pacman.x = 190
    pacman.y = 210
    pacman.move("right", walls)
    assert pacman.x == 190  # Should not move through the small obstacle

    # Step 3: Move pacman towards the right wall (new right wall at x=780)
    pacman.x = 780
    pacman.y = 100
    pacman.move("right", walls)
    # Assert that the pacman's position hasn't changed, as they can't move past the wall
    assert pacman.x == 780  # Should not move beyond the right wall


def test_pacman_respawn():
    WINDOW_HEIGHT = 800
    WINDOW_WIDTH = 600
    pacman = Pacman(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    ghost = Ghost(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, (255, 0, 0))

    assert not ghost.scared

    collision = abs(ghost.x - pacman.x) < 20 and abs(ghost.y - pacman.y) < 20
    assert not collision, "Ghost spawned on pacman - instant death loop"
