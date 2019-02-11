//The selectedValueGenre functions change hidden p tag values to equal the selected genre
//of each dropdown box, these values are used in the setAction function
function selectedValueGenre1() {
    var selectBox = document.getElementById("genres1");
    var selectedValue = selectBox.options[selectBox.selectedIndex].value;
    document.getElementById("selected1").textContent = selectedValue;
}

function selectedValueGenre2() {
    var selectBox = document.getElementById("genres2");
    var selectedValue = selectBox.options[selectBox.selectedIndex].value;
    document.getElementById("selected2").textContent = selectedValue;
}

function selectedValueGenre3() {
    var selectBox = document.getElementById("genres3");
    var selectedValue = selectBox.options[selectBox.selectedIndex].value;
    document.getElementById("selected3").textContent = selectedValue;
}

//Get all of the data for the query and set the form's action to equal the user's inputs
function setAction(userID) {
    var selectP1 = document.getElementById("selected1").textContent;
    var selectP2 = document.getElementById("selected2").textContent;
    var selectP3 = document.getElementById("selected3").textContent;

    //Validation, if any of these happen then the user hasn't selected 3 genres
    if (selectP1 === "A" || selectP2 === "B" || selectP3 === "C") {
        return '';
    } else {
        return 'submitted/' + "?genre1=" + selectP1 + "&genre2=" + selectP2 + "&genre3=" + selectP3 + "&userid=" + userID;
    }
}


function revealClip(source) {
    document.getElementById('stream').src = source;
}

function revealClip2(source) {
    document.getElementById('stream2').src = source;
}