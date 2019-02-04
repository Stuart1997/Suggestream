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

function setAction(userID) {
    var selectP1 = document.getElementById("selected1").textContent;
    var selectP2 = document.getElementById("selected2").textContent;
    var selectP3 = document.getElementById("selected3").textContent;

    document.getElementById('hreftag').textContent = 'submitted/' + "?genre1=" + selectP1 + "&userid=" + userID;

    if (selectP1 === "A" || selectP2 === "B" || selectP3 === "C") {
        return '';
    } else {
        return 'submitted/' + "?genre1=" + selectP1 + "&genre2=" + selectP2 + "&genre3=" + selectP3 + "&userid=" + userID;
    }

}