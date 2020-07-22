<script>

var server = "http://127.0.0.1:5000";
userPreference = {}


function getBotResponse(){

var appdir ='/get';
var data = {}
var rawText = $("#textInput").val();

data['message'] = rawText;
console.log(rawText)


userPreference['Movies'] = rawText;

var userHtml = '<p class = "userText"><span>' + rawText + '</span></p>';
$("#textInput").val("");
$("#chatbox").append(userHtml);
document.getElementById('userInput').scrollIntoView({block:'start',behaviour:'smooth'});
$.ajax({

  						type: "POST",
  						url:server+appdir,
  						data: data,
  						dataType: 'json'
					}).done(function(data) {

showRecommendedMovies(data['reply']);

var botHtml = '<p class ="botText"><span>' + data['reply'] + '</span></p>';
$("#chatbox").append(botHtml);
document.getElementById('userInput').scrollIntoView({block : 'start',behaviour:'smooth'});
});
}


$("#textInput").keypress(function(e) {
if(e.which == 13) {
getBotResponse();
}
});

$("#buttonInput").click(function() {
getBotResponse();
})


$("#ShowBtn").click(function(e) {
    calcMovies()
	location.replace(server+'/showMovies')
})


function calcMovies(){

    $.ajax({

  						type: "POST",
  						url:'/getMovies',
  						data: userPreference,
						datatype: 'json',

  						});
}

function showRecommendedMovies(statement){
if (statement == "Click on the show button to see similar movies!")
    document.getElementById("ShowBtn").style.visibility  = "visible";
}


</script>








