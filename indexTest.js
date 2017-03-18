var express = require("express");
var request = require('request');
var bodyParser = require('body-parser');
var exec =require('child_process').exec;
var pythonShell = require("python-shell");

var pyShell = new pythonShell('controlLED.py');
pyShell.send("END");
pyShell.on('message', function(message) {
	console.log(message);
});
pyShell.end(function(err) {
	if(err) throw err;
	console.log("End of phShell");
});
process.on('SIGINT', function() {
	console.log(" Interrupt");
	pyShell.send("END");
	//setTimeout(function() {process.exit();},1000);
	process.exit();
});
var app = express();
var port = 5000;
var optionsChrome = {
	timeout : 10000,
	killSignal : 'SIGKILL'
};

app.use(bodyParser.urlencoded( {extended : false } ));
app.use(bodyParser.json());

var optionsSmartLamp = {
	uri : "http://218.150.183.150:3000/smartLamp",
	method : "GET",
	headers : { "Content-Type" : "application/x-www-form-urlencoded"},
}

var pythonOptions = {
	mode : "text",
	pythonOptions :['-u']
}


app.get('/', function(req,res) {
	console.log('smart void lamp');
	res.send('Smart Voice Lamp');
});

app.listen(port,function() {
	console.log("create Server");
	
	//1초마다 smartLamp 함수 호출
	setInterval(smartLamp,1000);
});

function smartLamp() {
	//GET 요청 전송
	request(optionsSmartLamp, function(error, response, body) {
		if(body == "empty" ) {
			console.log("no data");
			//pyShell.send("END");
		}
		else {
			console.log(body);

			var work = exec('chromium-browser http://218.150.183.150:3000/tts1.mp3', 
					optionsChrome,function(err, stdout, stderr) {
				if(err) {
					console.log("ERROR");
				}
				console.log(stdout);
			});
			console.log(work.pid);
			work.kill('SIGKILL');
			//pyShell.send(body);
		}
	});
}

