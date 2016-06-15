$(function() {
	var $reviews = $('.review');
	function showReview(id) {
		$reviews.each(function(index) {
			$(this).css('display', 'none');
		});
		var reviewSelector = '.review[data-id=' + id + ']';
		$(reviewSelector).css('display', 'table-cell');
	}
	$authors = $('.reviews__item');
	$authors.click(function(event) {
		showReview($(this).data('id'));
	});
	showReview(0);
})