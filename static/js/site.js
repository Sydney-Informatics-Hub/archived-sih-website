(function($) {
	$(document).ready(function() {
		/* Integrate TableOfContents */
		$('#TableOfContents > ul > li > ul').each(function () {
			var destHeading = $($('a', this.parentNode).first().attr('href'));
			$(this).addClass('.sectionToc').insertAfter(destHeading);
		});
	})
})(jQuery);
