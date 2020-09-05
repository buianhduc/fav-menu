function readJSONFile(file, callback) {
    var rawFile = new XMLHttpRequest();
    rawFile.overrideMimeType("application/json");
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function () {
        if (rawFile.readyState === 4 && rawFile.status == "200") {
            callback(rawFile.responseText);
        }
    };
    rawFile.send(null);
}

readJSONFile("../js/answers.json", function (text) {
    var data = JSON.parse(text);
    for (let i in data) {
        if (data[i].country === "Việt Nam") {
            var ans = "<li>" + data[i].name + "</li>";
            $(".choices").append(ans);
        }
    }

    // console.log(data.length)
});
$("document").ready(function () {
    $("button").click(function(){
        $.ajax({url: "../lol.txt", success: function(result){
            $("#question").html(result);
        }});
    });
});
