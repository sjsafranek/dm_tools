

var Random = {
    randint: function(min, max) {
        max += 1;
        return Math.floor(Math.random() * (+max - +min)) + +min;
    }
}

var Dice = {

    roll: function(ntimes, nsides, modifier) {
        if (!modifier) {
            modifier = 0;
        }
        var rolls = [];
        for (var i=0; i<ntimes; i++) {
            rolls.push(
                Random.randint(1, nsides) + modifier
            );
        }
        return rolls;
    },

    d2: function(ntimes, modifier) {
        return this.roll(ntimes, 2, modifier);
    },

    d4: function(ntimes, modifier) {
        return this.roll(ntimes, 4, modifier);
    },

    d6: function(ntimes, modifier) {
        return this.roll(ntimes, 6, modifier);
    },

    d8: function(ntimes, modifier) {
        return this.roll(ntimes, 8, modifier);
    },

    d10: function(ntimes, modifier) {
        return this.roll(ntimes, 10, modifier);
    },

    d12: function(ntimes, modifier) {
        return this.roll(ntimes, 12, modifier);
    },

    d20: function(ntimes, modifier) {
        return this.roll(ntimes, 20, modifier);
    },

    d100: function(ntimes, modifier) {
        return this.roll(ntimes, 100, modifier);
    }
}


var DiceUi = function() {
    var self = this

    var rollTimes = $("<input>", {type:"number", min:1, step:1})
        .addClass('form-control form-control-sm')
        .val(1);

    var diceTypeSelector = $("<select>")
        .addClass("form-control form-control-sm")
        .append(
            $('<option>', {value: 'd2'}).append('d2'),
            $('<option>', {value: 'd4'}).append('d4'),
            $('<option>', {value: 'd6'}).append('d6'),
            $('<option>', {value: 'd8'}).append('d8'),
            $('<option>', {value: 'd10'}).append('d10'),
            $('<option>', {value: 'd12'}).append('d12'),
            $('<option>', {value: 'd20'}).append('d20'),
            $('<option>', {value: 'd100'}).append('d100')
        );

    var rollModifier = $("<input>", {type:"number", min:0, step:1})
        .addClass('form-control form-control-sm')
        .val(0);

    var resultsContainer = $("<div>");

    var rollDiceButton = $("<button>")
        .addClass("btn btn-primary btn-sm")
        .append("Roll")
        .on("click", function() {
            resultsContainer.empty();
            var dtype = diceTypeSelector.val();
            var rolls = Dice[dtype](
                parseInt(rollTimes.val()),
                parseInt(rollModifier.val())
            );
            for (var i=0; i<rolls.length; i++) {
                resultsContainer.append(
                    $('<div>').append(rolls[i])
                );
            }
        });

    this.content = $("<div>")
        .append(
            $("<div>")
                .addClass("form-inline")
                .append(
                    rollTimes,
                    diceTypeSelector,
                    rollModifier,
                    rollDiceButton
                ),
            resultsContainer
        );

    this.container = DM.ui.makeDMToolUi({
        "name": "Dice",
        "content": this.content
    });

    $("body").append(this.container);
}


DM.registerTool("Dice", DiceUi);
