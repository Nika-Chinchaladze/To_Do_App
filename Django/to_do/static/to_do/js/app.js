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
    // fillInput(this);
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

// function fillInput(control) {
//     var desiredText = $(control).parent().parent().parent().children(".showDiv").children("h5").text();
//     $(control).parent().parent().children(".updateDiv").children("form").children("input").attr("value", desiredText);
// }

// Functionality for css tricks:
$(".addDiv").children("label").css("display", "none");
$("#id_new_task").addClass("addInput");
$("#id_new_task").attr("placeholder", "Add a Task");

$(".updateDiv").children("form").children("label").css("display", "none");
$(".updateDiv").children("form").children("input").addClass("updateClass");

