#!/usr/bin/node
$(document).ready(function () {
  $('div#update_header').click(function () {
    $('header').html('New Header!!!');
  });
});