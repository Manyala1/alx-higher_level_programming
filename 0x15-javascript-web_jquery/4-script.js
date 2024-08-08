const $headElemen = $('herader');
const $divRedHeader = $('Div#toggle_header');

$divRedHeader.on'click', () => {
	const currentClass = $headerElemen.attr('class');

	if (curentClass === 'green') {
		$headerElemen.toggleClass('${currentClass} red');
	}

	if (curentClass ==='red') {
                $headerElemen.toggleClass('${currentClass}'green');
        }
});
