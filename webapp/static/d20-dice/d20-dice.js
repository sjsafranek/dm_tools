

var Random = {
    randint: function(min, max) {
        max += 1;
        return Math.floor(Math.random() * (+max - +min)) + +min;
    }
}

var Dice = {

    roll: function(ntimes, nsides, modifier) {
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
    }

}
