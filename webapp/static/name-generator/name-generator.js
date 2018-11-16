
var NameGenerator = function() {
    var self = this;
    this.data = {
        begin: [],
        middle: [],
        end: []
    };
    d3.csv('/static/name-generator/data/name_parts.csv', function(row){
        self.data[row.section].push(row.part);
    });
}

NameGenerator.prototype.getRandomName = function() {
    var begin = this.data.begin[Math.floor(Math.random() * this.data.begin.length)];
    var middle= this.data.middle[Math.floor(Math.random() * this.data.middle.length)];
    var end   = this.data.end[Math.floor(Math.random() * this.data.end.length)];
    return begin + middle + end;
}

var NameGeneratorUi = function() {
    var self = this;
    this.nameGenerator = new NameGenerator();

    var characterName = $("<span>");

    var generateName = $("<button>")
        .addClass("btn btn-primary btn-sm nextCharacterInitative")
        .append("Generate Name")
        .on("click", function() {
            var name = self.nameGenerator.getRandomName();
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

    this.container = makeDMToolUi({
        "name": "Name Generator",
        "content": this.content
    });

    $("body").append(this.container);




}
