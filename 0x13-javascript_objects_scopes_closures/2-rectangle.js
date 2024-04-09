#!/usr/bin/node
// Class rectangle, checks if w and h are numbers greater than zero
module.exports = class Rectangle {
	constructor (w, h) {
		if ((w !== 0 && h !== 0) && (w > 0 && h > 0)) {
			this.width = w;
			this.height = h;
		}
	}
};
