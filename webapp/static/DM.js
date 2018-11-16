

var DM = {

    tools: {},

    utils: {

        getChallengeRating: function(cr) {
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

    },

    ui: {

        makeDMToolUi: function(options) {

            var $cardBody = $("<div>")
                .addClass("card-body")

            var $minimizeButton = $("<button>")
                .addClass("btn btn-sm btn-default window-minimize")
                .append(
                    $("<i>").addClass("far fa-window-minimize")
                )
                .on("click", function(){
                    $minimizeButton.hide();
                    $maximizeButton.show();
                    $cardBody.slideUp('fast');
                });

            var $maximizeButton = $("<button>")
                .css("display", "none")
                .addClass("btn btn-sm btn-default window-maximize")
                .append(
                    $("<i>").addClass("far fa-window-maximize")
                )
                .on("click", function(){
                    $minimizeButton.show();
                    $maximizeButton.hide();
                    $cardBody.slideDown('fast');
                });

            var $container = $("<div>")
                .addClass("tool-container")
                .append(
                    $("<div>")
                        .addClass("card-header")
                        .append(
                            $("<span>")
                                .addClass("card-title tool-title")
                                .append(options.name),
                            $("<span>")
                                .addClass("window-controls")
                                .append(
                                    $minimizeButton,
                                    $maximizeButton
                                )
                        ),
                    $cardBody
                        .append(
                            options.content
                        )
                );

            $container
                .css({
                    "width": "544px"
                })
                .draggable({
                    containment: "body",
                    scroll: false
                });

            $container
                .on("click", function(){
                    $(".tool-container").removeClass("selected");
                    $container.addClass("selected");
                });

            return $container;
        }


    }

}

DM.registerTool = function(name, obj) {
    this.tools[name] = obj;
}
