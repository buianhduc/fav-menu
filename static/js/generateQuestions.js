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
var answers, questions;
readJSONFile("../js/answers.json", function (text) {
    var data = JSON.parse(text);
    answers = data;

    // console.log(data.length)
});
questions = [
    {
        "id": 1,
        "text": "what are your favourite music?",
        "choices": [
            "Pop",
            "R&B/Soul",
            "EDM"
        ]
    },
    {
        "id": 1,
        "text": "where do your favourite music come from ?",
        "choices": [
            "Việt Nam",
            "US-UK",
            "Hàn Quốc"
        ]
    },
    {
        "id": 1,
        "text": "what are your favourite artists?",
        "choices": []
    }
];



// $("document").ready(function () {
//     for (var question in questions) {
//         if (questions[question].id !== 3) {
//             $("#question-container").append(`
//             <div class = 'container-fluid bg-white rounded mb-0' style = 'margin-top: 5%; padding-top: 10px; padding-left: 30px;'>
//                 <div class='question-and-number'>
//                 <div class='row question-number'>Question ${Number(question) + 1}/3</div>
//                 <div class='row question'>
//                     <h1>${questions[question].text}</h1>
//                 </div>
//                 <div class='row form-check'>
//                 </div>
//             </div>
//             </div>
//             `);
//             // $("document").ready(function() {
//                 for (var i in questions[question].choices) {
//                     var html = `<input type="checkbox" class="form-check-input" id="materialUnchecked">
//                     <label class="form-check-label" for="materialUnchecked">${questions[question].choices[i]}</label>`
//                     $('.form-check')[question].append(html);
//                 }
//             // });
//         }
//     }
// });
