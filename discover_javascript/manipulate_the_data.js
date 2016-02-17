var https = require('https');

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
	jsonParse.items.map(function(o, i){
	    var final=[jsonParse.items[i].full_name].join();
	    console.log(final);
	    return 0;
	});
    });
});


req.end();
