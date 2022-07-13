class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if not self.is_quality_increasing(item.name):
                if item.name != "Sulfuras, Hand of Ragnaros" and item.quality >0:
                    item.quality -= 1

            else:
                new_item = self.increase_amount_quality(item)
                item = new_item

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1

    def is_quality_increasing(self, item_name):
        if item_name == "Aged Brie" or item_name =="Backstage passes to a TAFKAL80ETC concert":
            return True
        return False

    def is_item_backstage(self, item):
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            return True
        return False

    def increase_amount_quality(self,item):
        if self.is_item_backstage(item):
            amount_increase = self.amount_increase_backstage(item)
        else:
            amount_increase = 1
        item.quality += amount_increase
        if item.quality > 50:
            item.quality = 50
        return item

    def amount_increase_backstage(self, item):
        if item.sell_in > 10:
            return 1
        elif item.sell_in > 5:
            return 2
        elif item.sell_in >= 0:
            return 3
        else:
            return -item.quality