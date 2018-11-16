
/*

tracker = new InitativeTracker();

tracker.add('stefan', 10);
tracker.add('patrick', 15);
tracker.add('drew', 8);

*/

var InitativeTracker = function() {
    this.index = 0;
    this.characters = {};
    this._order = [];
}

InitativeTracker.prototype.clear = function(){
    this.index = 0;
    this.characters = {};
    this._buildList();
}

InitativeTracker.prototype._buildList = function() {
    this._order = [];
    for (var i in this.characters) {
        this._order.push(
            this.characters[i]
        );
    }
    this._order.sort(function(a,b) {
        return a.initative > b.initative;
    });
}

InitativeTracker.prototype.add = function(character, initative) {
    this.characters[character] = {
        'name': character,
        'active': true,
        'initative': initative
    };
    this._buildList();
}

InitativeTracker.prototype.remove = function(character) {
    this.characters[character].active = false;
    this._buildList();
}

InitativeTracker.prototype.next = function(attempt) {
    if (0 == this._order.length) return null;
    if (!attempt) {attempt=0;}
    if (attempt > this._order.length) return null;
    this.index += 1;
    if (this.index >= this._order.length) { this.index = 0; }
    if (!this._order[this.index].active) {
        attempt++;
        return this.next(attempt);
    }
    return this._order[this.index];
}


var InitativeTrackerUi = function() {
    var self = this

    this.initativeTracker = new InitativeTracker();

    var characterNameInput = $("<input>", {
            'type': 'text',
            'placeholder': 'character name'
        })
        .addClass("form-control form-control-sm");

    var characterInitativeInput = $("<input>", {
        'type': 'number',
        'placeholder': 'initative'
    })
        .addClass("form-control form-control-sm");

    var characterInitativeContainer = $("<div>")
        .addClass("list-group characterInitativeContainer");

    var addCharacterButton = $("<button>")
        .addClass("btn btn-default btn-sm mb-2")
        .append("Add")
        .on("click", function(){
            var characterName = characterNameInput.val();
            if ("" == characterName) return;

            var characterInitative = parseInt(characterInitativeInput.val());
            if (isNaN(characterInitative)) return;

            self.initativeTracker.add(characterName, characterInitative);

            characterInitativeContainer.empty();
            characterInitativeContainer.append(
                self.initativeTracker._order.map(function(d, i){
                    return $("<li>")
                        .addClass("list-group-item d-flex justify-content-between align-items-center " + (d.active ? "" : "disabled") + " " + (self.initativeTracker.index==i ? "list-group-item-primary": ""))
                        .append(
                            d.name,
                            $("<span>").addClass("badge badge-primary badge-pill").append(d.initative),
                            $("<button>")
                                .addClass("btn btn-default btn-sm")
                                .css("float", "right")
                                .append(
                                    $("<i>").addClass("fas fa-times")
                                )
                                .on("click", function(){
                                    self.initativeTracker.remove(d.name);
                                    $(this).parent().removeClass("list-group-item-primary");
                                    $(this).parent().addClass("disabled");
                                })
                        )
                })
            );

            characterNameInput.val("");
            characterInitativeInput.val("");
        });

    var nextCharacterButton = $("<button>")
        .addClass("btn btn-primary btn-sm")
        .append("Next")
        .on("click", function() {
            self.initativeTracker.next();
            characterInitativeContainer.find("li").removeClass("list-group-item-primary");
            var i = self.initativeTracker.index;
            $(characterInitativeContainer.find("li")[i]).addClass("list-group-item-primary");
        });

    var clearInitativeButton = $("<button>")
        .addClass("btn btn-warning btn-sm")
        .append("Clear")
        .on("click", function(){
            self.initativeTracker.clear();
            characterInitativeContainer.empty();
        });

    this.content = $("<div>")
        .append(
            $("<div>")
                .addClass("form-inline")
                .append(
                    $("<div>")
                        .addClass("mb-2")
                        .append(
                            characterNameInput
                        ),
                    $("<div>")
                        .addClass("mx-sm-3 mb-2")
                        .append(
                            characterInitativeInput
                        ),
                    addCharacterButton
                ),
            characterInitativeContainer,
            $("<div>").addClass("initativeControls").append(
                clearInitativeButton,
                nextCharacterButton
            )
        );

    this.container = makeDMToolUi({
        "name": "Initative Tracker",
        "content": this.content
    });

    $("body").append(this.container);
}
