(function(DM){

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
                        DM.getTreasureDatabase().getGemstone(opts['GEMSTONES_c'])
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
                        DM.getTreasureDatabase().getArtObject(opts['ARTOBJECTS_c'])
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
                            DM.getTreasureDatabase().getMagicItem(parts_t[i])
                        );
                    }

                }
            }
        }

    }

    Treasure.Individual = function(cr) {
        var CR = DM.utils.getChallengeRating(cr);
        var row = DM.getTreasureDatabase().select("individual_treasure", {'CR': CR}, 1)[0];
        return new Treasure(row);
    }

    Treasure.Hoard = function(cr) {
        var CR = DM.utils.getChallengeRating(cr);
        var row = DM.getTreasureDatabase().select("hoard_treasure", {'CR': CR}, 1)[0];
        return new Treasure(row);
    }

    DM.Treasure = Treasure;
    DM.getTreasureForIndividual = Treasure.Individual;
    DM.getTreasureForHoard = Treasure.Hoard;



    var TreasureGeneratorUi = function() {

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
                    treasure = DM.Treasure.Individual(challengeRating);
                } else if ("Hoard" == treasureType) {
                    treasure = DM.Treasure.Hoard(challengeRating);
                }

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

        this.container = DM.ui.makeDMToolUi({
            name: "Treasure Generator",
            content: this.content
        });

        $("body").append(this.container);
    }


    DM.registerTool("TreasureGenerator", TreasureGeneratorUi);

})(DM);
