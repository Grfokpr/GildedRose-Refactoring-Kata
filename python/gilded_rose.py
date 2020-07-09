# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # Making sure "Sulfuras, Hand of Ragnaros" is immune
            if item.name == 'Sulfuras, Hand of Ragnaros':
                item.quality = 80
                continue
            # Updating quality for "Aged Brie"
            elif item.name == 'Aged Brie':
                self.update_aged_brie(item)
                continue
            # Updating Quality for "Backstage pass"
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.update_backstage_pass(item)
                continue
            elif "Conjured" in item.name:
                self.update_conjured_items(item)
                continue
            else:
                #Updating quality for other items
                self.quality_decreasing(item)

                item.sell_in -= 1

                if item.sell_in < 0:
                    self.quality_decreasing(item)

    def update_conjured_items(self, item):
        # Method to update "Conjured items"
        item.quality -= 2
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality -= 2

    def update_aged_brie(self, item):
        # Method to update "Agied brie"
        self.increase_quality(item)
        item.sell_in -= 1
        if item.sell_in < 0:
            self.increase_quality(item)

    def update_backstage_pass(self, item):
        # Method to update "Backstage pass"
        if item.sell_in < 6:
            item.quality += 3
        elif item.sell_in < 11:
            item.quality += 2
        else:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
        item.quality = min(item.quality, 50)

    def quality_decreasing(self, item):
        # Method to denote quality
        if item.quality > 0:
            item.quality -= 1

    def increase_quality(self, item):
        # Method to increase quality
        if item.quality < 50:
            item.quality += 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
