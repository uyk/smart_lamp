var PythonShell = require("python-shell");

var options={
	mode : "text",
	pythonPath : "",
	scriptPath : "",
	pythonOptions : ['-u'],
	args : [0,0,80]
};

PythonShell.run('turnOn.py',options, function(err,results) {
	if(err) throw err;
});
