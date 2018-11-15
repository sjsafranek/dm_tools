

function getChallengeRating(cr) {
    if (0 <= cr && 4 >= cr) {
        return '0-4';
    }
    else if (5 <= cr && 10 >= cr) {
        return '5-10';
    }
    else if (11 <= cr && 16 >= cr) {
        return '11-16';
    }
    else if (17 <= cr) {
        return '17-20';
    }
    return null;
}


var Database = function() {
    this.tables = {};
};

Database.prototype._getRandomWeightedChoice = function(data) {
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

Database.prototype.select = function(table, filter, num) {
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

Database.prototype.getArtOrGemstone = function(_cost, _type) {
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

Database.prototype.getGemstone = function(gp) {
    return this.getArtOrGemstone(gp, 'gemstone');
}

Database.prototype.getArtObject = function(gp) {
    return this.getArtOrGemstone(gp, 'art_object');
}

Database.prototype.getMagicItem = function(table_name) {
    var magic_items = db.magic_items.filter(function(d){ return d.TABLE == table_name; });
    return this._getRandomWeightedChoice(magic_items);
}

Database.prototype.loadTable = function(table_name, filename) {
    var self = this;
    this[table_name] = [];
    d3.csv(filename, function(row){
        self[table_name].push(row);
    });
}




var Treasure = function(opts) {
    this.cp = 0;
    this.sp = 0;
    this.ep = 0;
    this.gp = 0;
    this.pp = 0;
    this.gemstones = [];
    this.art_objects = [];
    this.magic_items = [];
    opts && this._makeTreasure(opts);
}

Treasure.prototype._coins = function(n, d, m) {
    var total = 0;
    for (var i=0; i<n; i++){
        total += Math.floor(Math.random() * (d - 0)) + 0;
    }
    return total*m;
}

Treasure.prototype._makeTreasure = function(opts) {
    this.cp = this._coins(+opts['CP_n'], +opts['CP_d'], +opts['CP_m']);
    this.sp = this._coins(+opts['SP_n'], +opts['SP_d'], +opts['SP_m']);
    this.ep = this._coins(+opts['EP_n'], +opts['EP_d'], +opts['EP_m']);
    this.gp = this._coins(+opts['GP_n'], +opts['GP_d'], +opts['GP_m']);
    this.pp = this._coins(+opts['PP_n'], +opts['PP_d'], +opts['PP_m']);

    if (opts['GEMSTONES_n']) {
        if (0 != +opts['GEMSTONES_n']) {
            this.gemstones = [];

            var num = 0;
            for (var i=0; i<+opts['GEMSTONES_n']; i++) {
                num += Math.floor(Math.random() * (+opts['GEMSTONES_d'] - 0)) + 0;
            }

            for (var i=0; i<num; i++) {
                this.gemstones.push(
                    db.getGemstone(opts['GEMSTONES_c'])
                );
            }
        }
    }

    if (opts['ARTOBJECTS_n']) {
        if (0 != +opts['ARTOBJECTS_n']) {
            this.art_objects = [];

            var num = 0;
            for (var i=0; i<+opts['ARTOBJECTS_n']; i++) {
                num += Math.floor(Math.random() * (+opts['ARTOBJECTS_d'] - 0)) + 0;
            }

            for (var i=0; i<num; i++) {
                this.art_objects.push(
                    db.getArtObject(opts['ARTOBJECTS_c'])
                );
            }
        }
    }

    if (opts['MAGIC_ITEMS_n']) {
        this.magic_items = [];
        var parts_n = opts['MAGIC_ITEMS_n'].split(';');
        var parts_d = opts['MAGIC_ITEMS_d'].split(';');
        var parts_t = opts['MAGIC_ITEMS_t'].split(';');
        for (var i=0; i<parts_n.length; i++) {
            if (0 != +parts_n[i]) {

                var num = 0;
                for (var j=0; j<+parts_n; j++) {
                    num += Math.floor(Math.random() * (+parts_d - 0)) + 0;
                }

                for (var j=0; j<num; j++) {
                    this.magic_items.push(
                        db.getMagicItem(parts_t[i])
                    );
                }

            }
        }
    }

}

Treasure.Individual = function(cr) {
    var CR = getChallengeRating(cr);
    var row = db.select("individual_treasure", {'CR': CR}, 1)[0];
    return new Treasure(row);
}

Treasure.Hoard = function(cr) {
    var CR = getChallengeRating(cr);
    var row = db.select("hoard_treasure", {'CR': CR}, 1)[0];
    return new Treasure(row);
}


var TreasureUi = function() {

    var treasureTypeSelector = $("<select>")
        .addClass("form-control form-control-sm")
        .append(
            $("<option>").append("Individual"),
            $("<option>").append("Hoard")
        );

    var treasureChallengeRatingSelector = $("<select>")
        .addClass("form-control form-control-sm")
        .append(
            (function() {
                var options = [];
                for (var i=1; i<21; i++) {
                    options.push(
                        $("<option>").append(i)
                    );
                }
                return options;
            })()
        );

    var treasureContainer = $("<div>")
        .addClass("treasureContainer");

    var generateTreasureButton = $("<button>")
        .addClass("btn btn-primary btn-sm mb-2")
        .append("Generate")
        .on("click", function(){

            var treasureType = treasureTypeSelector.val();
            var challengeRating = parseInt( treasureChallengeRatingSelector.val() );

            var treasure;
            if ("Individual" == treasureType) {
                treasure = Treasure.Individual(challengeRating);
            } else if ("Hoard" == treasureType) {
                treasure = Treasure.Hoard(challengeRating);
            }
            console.log(treasure);

            var items = [];
            items = ["cp","sp","ep","gp","pp"].map(function(d){
                return {
                    COST: treasure[d] + d,
                    TYPE: "coin",
                    NAME: d
                }
            });
            items = items.concat(treasure.gemstones);
            items = items.concat(treasure.art_objects);
            items = items.concat(treasure.magic_items.map(function(d){
                return {
                    COST: "",
                    TYPE: "magic_item",
                    NAME: d.MAGIC_ITEM
                }
            }));

            treasureContainer.empty();
            treasureContainer.append(
                $("<table>")
                    .addClass("table table-bordered table-sm")
                    .css({"width": "500px"})
                    .append(
                        $("<thead>").append(
                            $("<tr>").append(
                                $("<th>", {scope:"col"}).css({"width": "100px"}).append("Cost"),
                                $("<th>", {scope:"col"}).append("Type"),
                                $("<th>", {scope:"col"}).append("Name")
                            )
                        ),
                        $("<tbody>").append(
                            items.map(function(d){
                                return $("<tr>").append(
                                    $("<td>").append(d.COST),
                                    $("<td>").append(d.TYPE),
                                    $("<td>").append(d.NAME)
                                )
                            })
                        )
                    )
            );

        });

    this.content = $("<div>")
        .append(
            $("<div>")
                .addClass("form-inline")
                .append(
                    $("<div>")
                        .addClass("mb-2")
                        .append(
                            treasureTypeSelector
                        ),
                    $("<div>")
                        .addClass("mx-sm-3 mb-2")
                        .append(
                            treasureChallengeRatingSelector
                        ),
                    generateTreasureButton
                ),
            treasureContainer
        );

    this.container = makeDMToolUi({
        name: "Treasure Generator",
        content: this.content
    });

    $("body").append(this.container);
}
