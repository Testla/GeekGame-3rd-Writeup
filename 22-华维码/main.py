import json
import os
import sys
import typing

import numpy as np
import PIL.Image

Side_length = 25
Tile_side = 5
PIXEL_SIZE = 10
WHITE = 255
BLACK = 0
UNKNOWN = 128
Fixed_pattern = np.array([[UNKNOWN] * Side_length for _ in range(Side_length)])


def initialize_fixed_pattern() -> None:
    finder_pattern_top_lefts = [
        (0, 0),
        (0, Side_length - 7),
        (Side_length - 7, 0),
    ]
    for row_s, column_s in finder_pattern_top_lefts:
        for i in range(7):
            Fixed_pattern[row_s + i][column_s + 0] = BLACK
            Fixed_pattern[row_s + i][column_s + 6] = BLACK
            Fixed_pattern[row_s + 0][column_s + i] = BLACK
            Fixed_pattern[row_s + 6][column_s + i] = BLACK
        for i in range(5):
            Fixed_pattern[row_s + i + 1][column_s + 1] = WHITE
            Fixed_pattern[row_s + i + 1][column_s + 5] = WHITE
            Fixed_pattern[row_s + 1][column_s + i + 1] = WHITE
            Fixed_pattern[row_s + 5][column_s + i + 1] = WHITE
        for dr in range(2, 5):
            for dc in range(2, 5):
                Fixed_pattern[row_s + dr][column_s + dc] = 0
    # separator
    for i in range(8):
        Fixed_pattern[7][i] = WHITE
        Fixed_pattern[7][-i - 1] = WHITE
        Fixed_pattern[-8][i] = WHITE
        # Fixed_pattern[-8][-i - 1] = WHITE
        Fixed_pattern[i][7] = WHITE
        Fixed_pattern[-i - 1][7] = WHITE
        Fixed_pattern[i][-8] = WHITE
        # Fixed_pattern[-i - 1][-8] = WHITE
    # timing patterns
    for i in range(8, Side_length - 8):
        Fixed_pattern[6][i] = (BLACK, WHITE)[i % 2]
        Fixed_pattern[i][6] = (BLACK, WHITE)[i % 2]
    # alignment patterns
    # hardcode for now
    align_top_row = Side_length - 9
    align_left_column = Side_length - 9
    for i in range(5):
        Fixed_pattern[align_top_row][align_left_column + i] = BLACK
        Fixed_pattern[align_top_row + 4][align_left_column + i] = BLACK
        Fixed_pattern[align_top_row + i][align_left_column] = BLACK
        Fixed_pattern[align_top_row + i][align_left_column + 4] = BLACK
    for i in range(3):
        Fixed_pattern[align_top_row + 1][align_left_column + 1 + i] = WHITE
        Fixed_pattern[align_top_row + 3][align_left_column + 1 + i] = WHITE
        Fixed_pattern[align_top_row + i + 1][align_left_column + 1] = WHITE
        Fixed_pattern[align_top_row + i + 1][align_left_column + 3] = WHITE
    Fixed_pattern[align_top_row + 2][align_left_column + 2] = BLACK


def pixels_to_image(pixels: np.array) -> np.array:
    return np.array(
        [[pixels[i // PIXEL_SIZE][j // PIXEL_SIZE]
        for j in range(pixels.shape[1] * PIXEL_SIZE)]
        for i in range(pixels.shape[0] * PIXEL_SIZE)],
        dtype=np.uint8)

def export(image: np.array, filename: str) -> None:
    with PIL.Image.fromarray(image) as im:
        im.save(filename)


def image_to_pixels(path) -> np.array:
    with PIL.Image.open(path) as im:
        a = np.asarray(im, dtype=np.uint8)
        pixels = np.empty((im.width // PIXEL_SIZE, im.height // PIXEL_SIZE))
        for i, j in np.ndindex(im.height // PIXEL_SIZE, im.width // PIXEL_SIZE):
            pixel = a[
                i * PIXEL_SIZE: (i + 1) * PIXEL_SIZE,
                j * PIXEL_SIZE: (j + 1) * PIXEL_SIZE,]
            pixels[i][j] = WHITE if pixel[0][0] == 1 else BLACK
    return pixels

test_image = 'game1/de2f0abc.png'
print(image_to_pixels(test_image))

def read_tiles(d: str) -> typing.Dict[str, np.array]:
    result = {}
    for filename in os.listdir(d):
        result[filename] = image_to_pixels(os.path.join(d, filename))
    return result


def can_fit(row_s: int, column_s: int, tile: np.array) -> bool:
    for rd in range(Tile_side):
        for cd in range(Tile_side):
            r = row_s + rd
            c = column_s + cd
            fixed = Fixed_pattern[r][c]
            if fixed == UNKNOWN:
                continue
            if fixed != tile[rd][cd]:
                return False
    return True

def result_to_pixels(
    result: typing.List[typing.List[typing.Optional[int]]],
    tiles: typing.Dict[str, np.array],
) -> np.array:
    Unknown_tile = np.array([[UNKNOWN] * Tile_side] * Tile_side)
    pixels = np.empty((Side_length, Side_length))
    for r in range(Side_length // Tile_side):
        for c in range(Side_length // Tile_side):
            tile = Unknown_tile if result[r][c] is None else tiles[result[r][c]]
            for rr in range(Tile_side):
                for cc in range(Tile_side):
                    try:
                        pixels[r * Tile_side + rr][c * Tile_side + cc] = tile[rr][cc]
                    except Exception:
                        print(f'{r=} {c=} {rr=} {cc=}')
                        raise
    return pixels

Num_possibilities = 0

def search(
    row_start: int,
    column_start: int,
    tiles: typing.Dict[str, np.array],
    result: typing.List[typing.List[typing.Optional[int]]],
    to_be_fitted: typing.Set[str],
) -> None:
    global Num_possibilities
    all_done = True
    for l in result:
        if None in l:
            all_done = False
            break
    if all_done:
        # export(pixels_to_image(result_to_pixels(result, tiles)), f'result-{Num_possibilities}.png')
        # with open(f'result-{Num_possibilities}.txt', 'w') as f:
        #     json.dump(result, f)
        Num_possibilities += 1
        return

    # Find the next unknown tile
    row, column = row_start, column_start
    while True:
        if result[row][column] is None:
            break
        column += 1
        if column == Side_length // Tile_side:
            column = 0
            row += 1

    tiles_that_fits = [
        t
        for t in to_be_fitted
        if can_fit(row * Tile_side, column * Tile_side, tiles[t])
    ]
    # print(row, column, to_be_fitted, tiles_that_fits)
    for tile in tiles_that_fits:
        result[row][column] = tile
        to_be_fitted.remove(tile)
        search(
            row + (column + 1) // (Side_length // Tile_side),
            (column + 1) % (Side_length // Tile_side),
            tiles,
            result,
            to_be_fitted
        )
        to_be_fitted.add(tile)
        result[row][column] = None

def main() -> None:
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} game_dir')
        exit(1)
    game_dir = sys.argv[1]

    initialize_fixed_pattern()
    export(pixels_to_image(Fixed_pattern), 'fixed.png')
    tiles = read_tiles(game_dir)
    missing_tile = [
        [BLACK] * 5,
        [BLACK, WHITE, WHITE, WHITE, WHITE],
        [BLACK, WHITE, BLACK, BLACK, BLACK],
        [BLACK, WHITE, BLACK, BLACK, BLACK],
        [BLACK, WHITE, BLACK, BLACK, BLACK],
    ]
    tiles['missing_tile.png'] = missing_tile
    result = [
        [None] * (Side_length // Tile_side)
        for _ in range(Side_length // Tile_side)
    ]
    to_be_fitted = set(tiles.keys())
    for _ in range(10):
        for r in range(Side_length // Tile_side):
            for c in range(Side_length // Tile_side):
                if result[r][c] is not None:
                    continue
                row_s = r * Tile_side
                column_s = c * Tile_side
                tiles_that_fits = [
                    t
                    for t in to_be_fitted
                    if can_fit(row_s, column_s, tiles[t])
                ]
                if len(tiles_that_fits) == 1:
                    result[r][c] = tiles_that_fits[0]
                    to_be_fitted.remove(tiles_that_fits[0])
    print(result)
    export(pixels_to_image(result_to_pixels(result, tiles)), 'result.png')
    search(0, 0, tiles, result, to_be_fitted)
    print(Num_possibilities)

if __name__ == "__main__":
    main()
