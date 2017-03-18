var PythonShell = require('python-shell');
var pyshell = new PythonShell('script.py');

//pyshell.send("test");
setInterval(test,1000);

pyshell.on('message', function(message) {
	console.log(message);
});

pyshell.end(function(err) {
	if(err) {
		throw err;
	}

	console.log("finished");
});

function test() {
	pyshell.send("test");
}
