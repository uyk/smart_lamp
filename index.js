var express = require("express");
var bodyParser = require("body-parser");
var request = require('request');
var fs = require('fs');
var exec =require('child_process').exec;
var pythonShell = require("python-shell");

var app = express();
var port = 5000;
var defaultColor = [0,0,0];
var newColor = [0,0,0];
var work;
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
			console.log("R : " + defaultColor[0]);
			console.log("G : " + defaultColor[1]);
			console.log("B : " + defaultColor[2]);
		}
		else {
			newColor = body.split(',');
			console.log("R : " + newColor[0]);
			console.log("G : " + newColor[1]);
			console.log("B : " + newColor[2]);

			work = exec('chromium-browser http://218.150.183.150:3000/tts1.mp3', optionsChrome,function(err, stdout, stderr) {
				if(err) {
					console.log("ERROR");
				}
				console.log(stdout);
			});
			console.log(work.pid);
			work.kill('SIGKILL');
			facebook();
		}
	});
}

function facebook() {
	pythonShell.run('facebook.py', pythonOptions, function(err, results) {
		if(err) throw err;
	});
}	
