
var App = function() {

    for (var i in DM.tools) {
        this[i] = new DM.tools[i];
    }
    
}
