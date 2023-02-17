// Functionality for Drop Down Button:
$(".dropButton").click(function() {
    displaySettings(this);
})


function displaySettings(control) {
    var settingDiv = $(control).parent().parent().children(".settingsDiv");
    if ($(settingDiv).css("display") === "none") {
        $(settingDiv).css("display", "block");
    }
    else {
        $(settingDiv).css("display", "none");
    }
}


// Functionality for update Button:
$(".update").click(function() {
    displayUpdate(this);
})

function displayUpdate(control) {
    var updateDiv = $(control).parent().parent().children(".updateDiv");
    if ($(updateDiv).css("display") === "none") {
        $(updateDiv).css("display", "block");
    }
    else {
        $(updateDiv).css("display", "none");
    }
}