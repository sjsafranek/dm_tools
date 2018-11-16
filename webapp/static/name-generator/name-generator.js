(function(DM){

    var data = {
        begin: [],
        middle: [],
        end: []
    };

    d3.csv('/static/name-generator/data/name_parts.csv', function(row){
        data[row.section].push(row.part);
    });

    DM.generateRandomName = function() {
        var begin = data.begin[Math.floor(Math.random() * data.begin.length)];
        var middle= data.middle[Math.floor(Math.random() * data.middle.length)];
        var end   = data.end[Math.floor(Math.random() * data.end.length)];
        return begin + middle + end;
    }


    var NameGeneratorUi = function() {
        var self = this;

        var characterName = $("<span>");

        var generateName = $("<button>")
            .addClass("btn btn-primary btn-sm nextCharacterInitative")
            .append("Generate Name")
            .on("click", function() {
                var name = DM.generateRandomName();
                characterName.text(name);
            });

        this.content = $("<div>")
            .append(
                $("<div>")
                    .addClass("form-inline")
                    .append(
                        $("<div>")
                            .addClass("mb-2")
                            .append(
                                generateName
                            ),
                        $("<div>")
                            .addClass("mx-sm-3 mb-2")
                            .append(
                                characterName
                            )
                    )
            );

        this.container = DM.ui.makeDMToolUi({
            "name": "Name Generator",
            "content": this.content
        });

        $("body").append(this.container);
    }

    DM.registerTool("NameGenerator", NameGeneratorUi);

})(DM);
