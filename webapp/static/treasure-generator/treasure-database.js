
(function(DM){

    var TreasureDatabase = function() {};

    TreasureDatabase.prototype._getRandomWeightedChoice = function(data) {
        var items = [];
        for (var i=0; i<data.length; i++) {
            var item = data[i];
            if (!item['PROBABILITY']) {
                items.push(item);
            } else if (-1 == item['PROBABILITY'].indexOf('-')) {
                items.push(item);
            } else {
                var parts = item['PROBABILITY'].split('-');
                var begin = +parts[0]-1;
                var end   = +parts[1];
                if ("00" == parts[0]) {
                    begin = 100;
                }
                if ("00" == parts[1]) {
                    end = 100;
                }
                for (var j=begin; j<end; j++) {
                    items.push(item);
                }
            }
        }
        return items[Math.floor(Math.random() * items.length)];
    }

    TreasureDatabase.prototype.select = function(table, filter, num) {
        if (!this[table]) {return [];}
        var rows = this[table].filter(function(d) {
            for (var i in filter) {
                if (filter[i] != d[i]) {
                    return false;
                }
            }
            return true;
        });

        if (!num) return rows;

        var data = [];
        for (var i=0; i<num; i++) {
            data.push(
                this._getRandomWeightedChoice(rows)
            );
        }

        return data;
    }

    TreasureDatabase.prototype.getArtOrGemstone = function(_cost, _type) {
        // normalize gp
        _cost = ""+_cost;
        if (-1 == _cost.indexOf("gp")) {
            _cost = _cost+'gp';
        }
        //.end

        var art_and_gemstones = this.art_and_gemstones.filter(function(d) {return d.COST == _cost;});
        if (0 == art_and_gemstones.length) {
            return null;
        }

        var item = art_and_gemstones[Math.floor(Math.random() * art_and_gemstones.length)];

        return item;
    }

    TreasureDatabase.prototype.getGemstone = function(gp) {
        return this.getArtOrGemstone(gp, 'gemstone');
    }

    TreasureDatabase.prototype.getArtObject = function(gp) {
        return this.getArtOrGemstone(gp, 'art_object');
    }

    TreasureDatabase.prototype.getMagicItem = function(table_name) {
        var magic_items = this.magic_items.filter(function(d){ return d.TABLE == table_name; });
        return this._getRandomWeightedChoice(magic_items);
    }

    TreasureDatabase.prototype.loadTable = function(table_name, filename) {
        var self = this;
        this[table_name] = [];
        d3.csv(filename, function(row){
            self[table_name].push(row);
        });
    }


    var db = new TreasureDatabase();
    db.loadTable("art_and_gemstones", '/static/treasure-generator/data/ART_AND_GEMSTONES.csv');
    db.loadTable("hoard_treasure", '/static/treasure-generator/data/HOARD_TREASURE.csv');
    db.loadTable("individual_treasure", '/static/treasure-generator/data/INDIVIDUAL_TREASURE.csv');
    db.loadTable("magic_items", '/static/treasure-generator/data/MAGIC_ITEMS.csv');

    DM.getTreasureDatabase = function() {
        return db;
    }

})(DM);
