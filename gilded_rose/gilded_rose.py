class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if not self.is_quality_increasing(item.name):
                if item.name != "Sulfuras, Hand of Ragnaros":
                    new_item = self.decrease_amount_quality(item)
                    item = new_item

            else:
                new_item = self.increase_amount_quality(item)
                item = new_item

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1


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
            amount_increase = self.double_speed_quality(item)
        item.quality += amount_increase
        if item.quality > 50:
            item.quality = 50
        return item

    def amount_increase_backstage(self, item):
        if item.sell_in > 10:
            return 1
        elif item.sell_in > 5:
            return 2
        elif item.sell_in > 0:
            return 3
        else:
            return -item.quality

    def decrease_amount_quality(self,item):
        item.quality -= self.double_speed_quality(item)
        if item.quality < 0:
            item.quality = 0
        return item

    def double_speed_quality(self, item):
        amount_change = 1

        if item.sell_in <= 0:
            amount_change = amount_change * 2

        return amount_change