$(document).ready(function () {
  $('#user-menu-toggle').on('click', function () {
    $('.user-menu').toggleClass('hidden');
  });

  $('button.save-for-later').on('click', function () {
    const articleId = parseInt($(this).attr('article-id'));
    const currentButton = $(this);
    $.ajax({
      type: 'GET',
      url: '/account/article-save/',
      data: { article_id: articleId },
      success: function (data, status, xhr) {
        if (xhr.status === 201) {
          // Saved successfully
          currentButton.html('<i class="fas fa-bookmark"></i>');
        } else {
          // Unsaved successfully
          currentButton.html('<i class="far fa-bookmark"></i>');
        }
      },
      error: function (jqXhr, textStatus, errorMessage) {
        console.log(errorMessage);
      },
    });
  });

  $('.select-all').on('change', 'input[type="checkbox"]', function () {
    const checked = $(this).prop('checked');
    $(this)
      .parents('.select-all')
      .siblings()
      .each(function () {
        $(this).find('input[type="checkbox"]').prop('checked', checked);
      });
  });

  $('.option').on('change', 'input[type="checkbox"]', function () {
    const checked = $(this).prop('checked');
    if (!checked) {
      $(this)
        .parents('.option')
        .siblings('.select-all')
        .find('input[type="checkbox"]')
        .prop('checked', false);
    }
  });
});
