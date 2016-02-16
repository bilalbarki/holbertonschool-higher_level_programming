var https = require('https');
var myMap = new Map();


var options = {
  hostname: 'api.github.com',
  path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
  headers: {
            'User-Agent': 'Holberton_School',
	    'Authorization': 'token ' + process.env.TOKEN
	   }
}

function streamToString(stream, cb) {
    const chunks = [];
    stream.on('data', (chunk) => {
	chunks.push(chunk);
    });
    stream.on('end', () => {
	cb(chunks.join(''));
    });
}

var req = https.request(options, function(res) {
    streamToString(res, function(jsonString){
	var jsonParse=JSON.parse(jsonString);
	console.log(jsonParse.items[0].full_name);
	console.log('bilal');
	jsonParse.items.map(function(o, i){
	   // console.log(jsonParse.items[i].full_name);
	    var final=[jsonParse.items[i].full_name].join();
	    console.log(final);
	    return 0;

	});
    });
});


req.end();
