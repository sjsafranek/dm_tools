
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
    if (!attempt) {attempt=0;}
    this.index += 1;
    if (this.index >= this._order.length) { this.index = 0; }
    if (!this._order[this.index].active) {
        return this.next(attempt++);
    }
    return this._order[this.index];
}
