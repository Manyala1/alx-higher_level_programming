#!/usr/bin/node

const fs = require('fs');

function readAndPrintFile(filePath) {
	fs.readFile(filePath, 'utf', (err, data) => {
		if (err) {
			console.error('Error: ${err.message}');
		} else {
			console.log(data);
		}
	});
}
