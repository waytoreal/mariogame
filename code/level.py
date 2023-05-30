import pygame
from support import import_csv_layout, import_cut_graphic
from settings import tile_size
from tiles import Tile, StaticTile, Crate, AnimatedTile, Coin

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.world_shift = 0

        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')

        # grass setup
        grass_layout = import_csv_layout(level_data['grass'])
        self.grass_sprites = self.create_tile_group(grass_layout, 'grass')

        # crates
        crate_layout = import_csv_layout(level_data['crates'])
        self.crate_sprite = self.create_tile_group(crate_layout, 'crates')

        # coins
        coin_layout = import_csv_layout(level_data['coins'])
        self.coin_sprite = self.create_tile_group(coin_layout, 'coins')

        # foreground palms
        fg_palm_layout = import_csv_layout(level_data['fg palms'])
        self.fg_palm_sprite = self.create_tile_group(fg_palm_layout, 'fg palms')
    
    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()
        
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type=='terrain':
                        terrain_tile_list = import_cut_graphic('./graphics/terrain/terrain_tiles.png')
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                    
                    if type == 'grass':
                        grass_tile_list = import_cut_graphic('./graphics/decoration/grass/grass.png')
                        tile_surface = grass_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                    
                    if type == 'crates':
                        sprite = Crate(tile_size, x, y)

                    if type == 'coins':
                        if val == '0':
                            sprite = Coin(tile_size, x, y, './graphics/coins/gold')
                        if val == '1':
                            sprite = Coin(tile_size, x, y, './graphics/coins/silver')
                    
                    if type == 'fg palms':
                        sprite = Palm(tile_size, x, y, './graphics/terrain/palm_small')

                    sprite_group.add(sprite)

        return sprite_group

    def run(self):
        # run the entire game / level

        #terrain
        self.terrain_sprites.draw(self.display_surface)
        self.terrain_sprites.update(self.world_shift)
        #grass
        self.grass_sprites.draw(self.display_surface)
        self.grass_sprites.update(self.world_shift)
        #crate
        self.crate_sprite.draw(self.display_surface)
        self.crate_sprite.update(self.world_shift)
        #coins
        self.coin_sprite.draw(self.display_surface)
        self.coin_sprite.update(self.world_shift)